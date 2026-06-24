import requests
import re
from colorama import Fore, Style
from tabulate import tabulate
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS_UA = {"User-Agent": "Mozilla/5.0 (compatible; ReconX/1.0)"}

TECH_SIGNATURES = {
    "WordPress":    [r"wp-content", r"wp-includes", r"WordPress"],
    "Joomla":       [r"Joomla!", r"/components/com_"],
    "Drupal":       [r"Drupal", r"/sites/default/files"],
    "Laravel":      [r"laravel_session", r"XSRF-TOKEN"],
    "Django":       [r"csrfmiddlewaretoken", r"django"],
    "React":        [r"react\.js", r"react\.min\.js", r"__REACT"],
    "Angular":      [r"ng-version", r"angular\.js"],
    "Vue.js":       [r"vue\.js", r"vue\.min\.js"],
    "jQuery":       [r"jquery", r"jQuery"],
    "Bootstrap":    [r"bootstrap\.css", r"bootstrap\.min\.css"],
    "Nginx":        [r"nginx"],
    "Apache":       [r"Apache"],
    "IIS":          [r"Microsoft-IIS", r"ASP\.NET"],
    "Cloudflare":   [r"cloudflare", r"cf-ray", r"__cfduid"],
    "AWS":          [r"x-amz-", r"amazonaws\.com"],
    "PHP":          [r"\.php", r"X-Powered-By: PHP"],
    "ASP.NET":      [r"ASP\.NET", r"__VIEWSTATE"],
}

INTERESTING_HEADERS = [
    "Server", "X-Powered-By", "X-Frame-Options", "X-XSS-Protection",
    "Content-Security-Policy", "Strict-Transport-Security",
    "X-Content-Type-Options", "Access-Control-Allow-Origin",
    "CF-Ray", "X-Cache", "Via", "Set-Cookie"
]

SECURITY_HEADERS = {
    "X-Frame-Options": "Clickjacking protection",
    "X-XSS-Protection": "XSS filter",
    "X-Content-Type-Options": "MIME sniffing protection",
    "Content-Security-Policy": "CSP",
    "Strict-Transport-Security": "HSTS",
    "Referrer-Policy": "Referrer control",
    "Permissions-Policy": "Feature policy",
}


def run_http_fingerprint(target):
    results = {}
    parts = target.split(".")
    is_ip = len(parts) == 4 and all(p.isdigit() for p in parts)

    urls = [f"https://{target}", f"http://{target}"]

    resp = None
    used_url = None
    for url in urls:
        try:
            resp = requests.get(url, headers=HEADERS_UA, timeout=6, verify=False, allow_redirects=True)
            used_url = url
            break
        except Exception:
            continue

    if not resp:
        print(f"{Fore.RED}  [-] Could not connect to target.{Style.RESET_ALL}")
        return results

    print(f"{Fore.CYAN}  [*] Connected: {Fore.WHITE}{used_url} → {resp.status_code}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  [*] Final URL: {Fore.WHITE}{resp.url}{Style.RESET_ALL}\n")

    # --- HTTP Headers ---
    print(f"{Fore.YELLOW}  [ HTTP Headers ]{Style.RESET_ALL}")
    header_rows = []
    for h in INTERESTING_HEADERS:
        val = resp.headers.get(h)
        if val:
            header_rows.append([f"{Fore.CYAN}{h}{Style.RESET_ALL}", val[:80]])
            results.setdefault("headers", {})[h] = val
    if header_rows:
        print(tabulate(header_rows, tablefmt="plain"))

    # --- Security headers check ---
    print(f"\n{Fore.YELLOW}  [ Security Headers Audit ]{Style.RESET_ALL}")
    sec_rows = []
    for h, desc in SECURITY_HEADERS.items():
        present = h in resp.headers
        status = f"{Fore.GREEN}✓ PRESENT{Style.RESET_ALL}" if present else f"{Fore.RED}✗ MISSING{Style.RESET_ALL}"
        sec_rows.append([f"{Fore.WHITE}{h}{Style.RESET_ALL}", desc, status])
    print(tabulate(sec_rows, tablefmt="plain"))

    # --- Tech Detection ---
    print(f"\n{Fore.YELLOW}  [ Technology Detection ]{Style.RESET_ALL}")
    detected = []
    body = resp.text
    all_headers_str = str(resp.headers).lower()

    for tech, patterns in TECH_SIGNATURES.items():
        for pat in patterns:
            if re.search(pat, body, re.IGNORECASE) or re.search(pat, all_headers_str, re.IGNORECASE):
                detected.append(tech)
                break

    if detected:
        for t in detected:
            print(f"  {Fore.GREEN}[+]{Style.RESET_ALL} {t}")
        results["technologies"] = detected
    else:
        print(f"  {Fore.YELLOW}[-] No common technologies detected.{Style.RESET_ALL}")

    # --- Cookie analysis ---
    if resp.cookies:
        print(f"\n{Fore.YELLOW}  [ Cookies ]{Style.RESET_ALL}")
        cookie_rows = []
        for c in resp.cookies:
            flags = []
            if c.secure: flags.append(f"{Fore.GREEN}Secure{Style.RESET_ALL}")
            if c.has_nonstandard_attr("HttpOnly"): flags.append(f"{Fore.GREEN}HttpOnly{Style.RESET_ALL}")
            if not c.secure: flags.append(f"{Fore.RED}!Secure{Style.RESET_ALL}")
            cookie_rows.append([f"{Fore.CYAN}{c.name}{Style.RESET_ALL}", str(c.value)[:30], " ".join(flags)])
        print(tabulate(cookie_rows, headers=["Name", "Value", "Flags"], tablefmt="plain"))

    return results
