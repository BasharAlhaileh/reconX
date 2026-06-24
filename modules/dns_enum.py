import dns.resolver
import dns.reversename
from colorama import Fore, Style
from tabulate import tabulate


RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "SOA", "CNAME", "PTR"]


def run_dns_enum(target):
    results = {}
    rows = []

    # Check if it's an IP (reverse DNS)
    try:
        parts = target.split(".")
        if len(parts) == 4 and all(p.isdigit() for p in parts):
            rev = dns.reversename.from_address(target)
            answers = dns.resolver.resolve(rev, "PTR")
            for r in answers:
                print(f"{Fore.GREEN}  PTR  {Fore.WHITE}{r.to_text()}{Style.RESET_ALL}")
            results["PTR"] = [r.to_text() for r in answers]
            return results
    except Exception:
        pass

    for rtype in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(target, rtype, lifetime=5)
            records = []
            for rdata in answers:
                val = rdata.to_text()
                records.append(val)
                rows.append([f"{Fore.CYAN}{rtype}{Style.RESET_ALL}", val[:80]])
            results[rtype] = records
        except Exception:
            pass

    if rows:
        print(tabulate(rows, headers=[f"{Fore.YELLOW}Type{Style.RESET_ALL}", f"{Fore.YELLOW}Value{Style.RESET_ALL}"], tablefmt="plain"))
    else:
        print(f"{Fore.RED}  [-] No DNS records found.{Style.RESET_ALL}")

    return results
