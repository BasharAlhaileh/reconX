import re
import requests
from colorama import Fore, Style

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ReconX/1.0)"
}

SOURCES = [
    "http://{domain}",
    "https://{domain}",
    "https://{domain}/contact",
    "https://{domain}/about",
    "https://{domain}/team",
]


def scrape_emails_from_url(url):
    emails = set()
    try:
        resp = requests.get(url, headers=HEADERS, timeout=5, verify=False)
        found = EMAIL_RE.findall(resp.text)
        for e in found:
            # Filter out false positives
            if not any(e.endswith(ext) for ext in [".png", ".jpg", ".gif", ".css", ".js"]):
                emails.add(e.lower())
    except Exception:
        pass
    return emails


def run_email_harvest(target):
    # Skip for bare IPs
    parts = target.split(".")
    if len(parts) == 4 and all(p.isdigit() for p in parts):
        print(f"{Fore.YELLOW}  [!] Email harvesting skipped for IP targets.{Style.RESET_ALL}")
        return {}

    results = {}
    all_emails = set()

    print(f"{Fore.CYAN}  [*] Scraping target pages for email addresses...{Style.RESET_ALL}")

    for template in SOURCES:
        url = template.format(domain=target)
        emails = scrape_emails_from_url(url)
        if emails:
            for email in emails:
                if email not in all_emails:
                    print(f"  {Fore.GREEN}[+]{Style.RESET_ALL} {Fore.WHITE}{email}{Style.RESET_ALL}  ← {Fore.CYAN}{url}{Style.RESET_ALL}")
                all_emails.update(emails)

    # Common role-based emails to report as potential targets
    ROLES = ["admin", "security", "info", "contact", "support", "abuse", "webmaster", "noc", "it"]
    domain = target.lstrip("www.")
    suggested = [f"{r}@{domain}" for r in ROLES]

    if all_emails:
        results["harvested"] = list(all_emails)
        print(f"\n{Fore.GREEN}  [✓] {len(all_emails)} email(s) found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}  [-] No emails scraped directly. Showing common role-based guesses:{Style.RESET_ALL}")
        for s in suggested:
            print(f"  {Fore.YELLOW}[~]{Style.RESET_ALL} {s}")
        results["suggested"] = suggested

    return results
