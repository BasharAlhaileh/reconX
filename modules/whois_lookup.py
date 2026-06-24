import whois
from colorama import Fore, Style
from tabulate import tabulate


def run_whois(target):
    results = {}
    try:
        w = whois.whois(target)
        fields = {
            "Domain Name":     w.domain_name,
            "Registrar":       w.registrar,
            "Creation Date":   w.creation_date,
            "Expiration Date": w.expiration_date,
            "Updated Date":    w.updated_date,
            "Name Servers":    w.name_servers,
            "Status":          w.status,
            "Emails":          w.emails,
            "Org":             w.org,
            "Country":         w.country,
        }
        rows = []
        for k, v in fields.items():
            if v:
                if isinstance(v, list):
                    v = ", ".join(str(x) for x in v[:3])
                results[k] = str(v)
                rows.append([f"{Fore.YELLOW}{k}{Style.RESET_ALL}", str(v)[:80]])

        print(tabulate(rows, tablefmt="plain"))
    except Exception as e:
        print(f"{Fore.RED}[-] WHOIS failed: {e}{Style.RESET_ALL}")
        results["error"] = str(e)
    return results
