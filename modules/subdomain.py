import dns.resolver
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed

WORDLIST = [
    "www", "mail", "ftp", "smtp", "pop", "imap", "webmail", "cpanel", "whm",
    "admin", "portal", "api", "dev", "staging", "test", "beta", "app",
    "vpn", "remote", "rdp", "ssh", "git", "gitlab", "jenkins", "jira",
    "confluence", "wiki", "docs", "cdn", "assets", "static", "media",
    "blog", "shop", "store", "help", "support", "kb", "status", "monitor",
    "dashboard", "panel", "backend", "intranet", "internal", "corp",
    "ns1", "ns2", "mx", "mx1", "mx2", "smtp1", "smtp2", "mail2",
    "m", "mobile", "wap", "img", "images", "video", "stream",
    "db", "database", "mysql", "postgres", "redis", "elastic",
    "old", "new", "v1", "v2", "backup", "archive", "secure",
    "auth", "login", "sso", "oauth", "id", "accounts",
    "cloud", "s3", "storage", "files", "download", "upload"
]


def check_subdomain(sub, domain):
    target = f"{sub}.{domain}"
    try:
        answers = dns.resolver.resolve(target, "A", lifetime=3)
        ips = [r.to_text() for r in answers]
        return (target, ips)
    except Exception:
        return None


def run_subdomain_discovery(target):
    # Skip if target looks like an IP
    parts = target.split(".")
    if len(parts) == 4 and all(p.isdigit() for p in parts):
        print(f"{Fore.YELLOW}  [!] Subdomain discovery skipped for IP targets.{Style.RESET_ALL}")
        return {}

    results = {}
    found = []

    print(f"{Fore.CYAN}  [*] Bruteforcing {len(WORDLIST)} subdomains...{Style.RESET_ALL}")

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(check_subdomain, sub, target): sub for sub in WORDLIST}
        for future in as_completed(futures):
            result = future.result()
            if result:
                subdomain, ips = result
                found.append((subdomain, ips))
                print(f"  {Fore.GREEN}[+]{Style.RESET_ALL} {Fore.WHITE}{subdomain:<45}{Style.RESET_ALL} → {Fore.YELLOW}{', '.join(ips)}{Style.RESET_ALL}")
                results[subdomain] = ips

    if not found:
        print(f"{Fore.RED}  [-] No subdomains discovered.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}  [✓] Found {len(found)} subdomains.{Style.RESET_ALL}")

    return results
