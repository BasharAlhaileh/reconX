import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
from tabulate import tabulate

COMMON_BANNERS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL",
    3389: "RDP", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
}


def grab_banner(host, port, timeout=2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
            banner = banner.split("\n")[0][:60]
        except Exception:
            banner = ""
        s.close()
        return banner
    except Exception:
        return ""


def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        result = s.connect_ex((host, port))
        s.close()
        if result == 0:
            banner = grab_banner(host, port)
            service = COMMON_BANNERS.get(port, "unknown")
            return (port, service, banner)
    except Exception:
        pass
    return None


def run_port_scan(target, ports_str):
    results = {}
    try:
        ports = [int(p.strip()) for p in ports_str.split(",") if p.strip().isdigit()]
    except Exception:
        ports = list(COMMON_BANNERS.keys())

    # Resolve hostname to IP if needed
    try:
        ip = socket.gethostbyname(target)
        if ip != target:
            print(f"{Fore.CYAN}  [*] Resolved {target} → {ip}{Style.RESET_ALL}")
    except Exception:
        ip = target

    print(f"{Fore.CYAN}  [*] Scanning {len(ports)} ports on {ip}...{Style.RESET_ALL}\n")

    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    open_ports.sort(key=lambda x: x[0])

    if open_ports:
        rows = []
        for port, service, banner in open_ports:
            rows.append([
                f"{Fore.GREEN}{port}{Style.RESET_ALL}",
                f"{Fore.CYAN}{service}{Style.RESET_ALL}",
                f"{Fore.WHITE}OPEN{Style.RESET_ALL}",
                f"{Fore.YELLOW}{banner[:50] if banner else '-'}{Style.RESET_ALL}"
            ])
            results[str(port)] = {"service": service, "banner": banner}

        print(tabulate(rows,
            headers=[
                f"{Fore.YELLOW}Port", "Service", "State", f"Banner{Style.RESET_ALL}"
            ],
            tablefmt="plain"
        ))
        print(f"\n{Fore.GREEN}  [✓] {len(open_ports)} open port(s) found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}  [-] No open ports found.{Style.RESET_ALL}")

    return results
