# ReconX - OSINT & Reconnaissance Framework

![ReconX Banner](https://img.shields.io/badge/Version-2.0-cyan?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)

**Built by FBI_Soldier | Team RedX**

An interactive, modular OSINT & reconnaissance CLI tool for authorized security professionals. Conduct passive information gathering with a beautiful terminal interface.

---

## 🎯 Features

✅ **6 Comprehensive Recon Modules:**
- WHOIS Lookup — Domain registration, registrar, nameservers
- DNS Enumeration — A, AAAA, MX, NS, TXT, SOA, CNAME, PTR records
- Subdomain Discovery — Concurrent wordlist brute-force with DNS queries
- Port Scan & Banner Grab — TCP service detection with banner grabbing
- Email Harvesting — Page scraping + role-based email guesses
- HTTP Fingerprinting — Headers, security audit, tech stack detection

✅ **Interactive Menu System** — Navigate easily through organized menus

✅ **Flexible Execution:**
- Run individual modules
- Run all modules at once
- Custom module selection
- Save results as JSON or TXT reports

✅ **Passive Reconnaissance** — No exploitation, minimal footprint

✅ **Professional Output** — Colored terminal UI with detailed results

---

## 📦 Installation

### Requirements
- Python 3.8+
- Linux/Kali/macOS

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/reconx.git
cd reconx

# Run installer
chmod +x install.sh
./install.sh

# Launch
python3 reconx.py
```

### Manual Installation

```bash
pip3 install -r requirements.txt --break-system-packages
python3 reconx.py
```

---

## 🚀 Usage

### Interactive Mode (Default)

```bash
python3 reconx.py
```

Follow the menu prompts:
1. **Select Target** — Enter domain or IP
2. **Run Reconnaissance** — Choose modules
3. **View Results** — See findings in real-time
4. **Export Results** — Save as JSON or TXT

### Example Workflow

```
[MAIN MENU]
1. Select Target → example.com
2. Run Reconnaissance
   ├─ Module 1: WHOIS Lookup
   ├─ Module 2: DNS Enumeration
   ├─ Module 3: Subdomain Discovery
   ├─ Module 4: Port Scan & Banner Grab
   ├─ Module 5: Email Harvesting
   └─ Module 6: HTTP Fingerprinting
3. View Results → See all findings
4. Export Results → Save report.json
```

---

## 📋 Module Details

### WHOIS Lookup
Retrieves domain registration information from public WHOIS databases.
```
Domain Name, Registrar, Creation/Expiration Dates, Nameservers, Organization, Country
```

### DNS Enumeration
Queries DNS records for comprehensive domain intelligence.
```
A, AAAA, MX, NS, TXT, SOA, CNAME, PTR records
```

### Subdomain Discovery
Brute-forces subdomains using a curated wordlist (60+ common entries) with concurrent DNS queries.
```
www, mail, ftp, api, dev, staging, cdn, backup, etc.
```

### Port Scan & Banner Grab
TCP connect scans on common ports with service detection and banner grabbing.
```
Default: 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443
Customizable via settings
```

### Email Harvesting
Scrapes public pages and generates common role-based email addresses.
```
admin@, security@, info@, contact@, support@, etc.
```

### HTTP Fingerprinting
Analyzes HTTP responses for security headers, technology detection, and web server info.
```
Server identification, security header audit, tech stack detection, cookie analysis
```

---

## 🔐 Passive Reconnaissance

All modules are **completely passive**:
- ✅ No exploitation
- ✅ No vulnerability scanning
- ✅ No data exfiltration
- ✅ Standard protocol behavior only
- ✅ Minimal system footprint

**Legal Notice:** Ensure you have written authorization before testing any system you do not own.

---

## 📊 Output Examples

### Console Output
```
════════════════════════════════════════════════════════════
  [+] PORT SCAN & BANNER GRAB
════════════════════════════════════════════════════════════

  [*] Resolved example.com → 172.66.147.243
  [*] Scanning 14 ports...

  Port  Service    State    Banner
    80  HTTP       OPEN     HTTP/1.1 200 OK
   443  HTTPS      OPEN     HTTP/1.1 200 OK

  [✓] 2 open port(s) found.
```

### JSON Export
```json
{
  "target": "example.com",
  "scan_time": "2026-06-24T21:15:32.123456",
  "modules": {
    "WHOIS Lookup": { ... },
    "DNS Enumeration": { ... },
    "Port Scan & Banner Grab": { ... }
  }
}
```

### TXT Export
```
============================================================
  ReconX Scan Report
  Target  : example.com
  Time    : 2026-06-24T21:15:32.123456
============================================================

[WHOIS LOOKUP]
...

[DNS ENUMERATION]
...

[PORT SCAN & BANNER GRAB]
...
```

---

## 🛠️ Dependencies

```
python-whois     - WHOIS domain lookups
dnspython        - DNS queries
requests         - HTTP requests
colorama         - Terminal colors
tabulate         - Table formatting
```

Install all:
```bash
pip3 install -r requirements.txt --break-system-packages
```

---

## 📁 Project Structure

```
reconx/
├── reconx.py                 # Main interactive application
├── install.sh                # Linux installer script
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
├── modules/
│   ├── whois_lookup.py      # WHOIS module
│   ├── dns_enum.py          # DNS module
│   ├── subdomain.py         # Subdomain discovery
│   ├── port_scan.py         # Port scanning
│   ├── email_harvest.py     # Email harvesting
│   └── http_fingerprint.py  # HTTP fingerprinting
└── utils/
    └── reporter.py          # Report generation
```

---

## 💡 Tips & Tricks

### Custom Port Scanning
Modify default ports in settings menu or edit `reconx.py`:
```python
self.default_ports = "22,80,443,8080,9200,6379"
```

### Skip Slow Modules
Use Custom Module Selection to skip:
- Subdomain Discovery (can be slow on large wordlists)
- Port Scanning (depends on target responsiveness)

### Batch Scanning
Run multiple targets by repeating:
1. Select Target
2. Run Modules
3. Export Results
4. Return to main menu and repeat

### Integration with Other Tools
Export to JSON and parse with:
```bash
cat report.json | jq '.modules."DNS Enumeration"'
```

---

## 🤝 Contributing

Contributions welcome! Ideas:
- Additional recon modules (Shodan API, SSL cert analysis, etc.)
- Performance optimizations
- New export formats (CSV, HTML)
- Additional wordlists for subdomain brute-force

---

## ⚖️ Legal & Ethics

**ReconX is for authorized security testing only:**

✅ Use with explicit written permission
✅ Follow responsible disclosure practices
✅ Comply with local laws and regulations
✅ Respect privacy and data protection laws

❌ Do NOT use on systems you don't own or have permission to test
❌ Do NOT use for malicious purposes
❌ Do NOT violate any laws

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👤 Author

**FBI_Soldier**  
Team: **RedX**

---

## 🙌 Acknowledgments

Built for the cybersecurity community. Designed for authorized penetration testers, security researchers, and CTF competitors.

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review module source code

---

**Made with ❤️ for the infosec community**

Stay ethical. Stay safe. 🔐
