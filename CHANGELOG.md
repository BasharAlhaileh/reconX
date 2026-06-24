# Changelog

All notable changes to ReconX will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0] - 2026-06-24

### Added
- Interactive terminal menu system with full navigation
- 6 comprehensive reconnaissance modules:
  - WHOIS Lookup (domain registration info)
  - DNS Enumeration (A, AAAA, MX, NS, TXT, SOA, CNAME, PTR)
  - Subdomain Discovery (concurrent DNS brute-force)
  - Port Scan & Banner Grab (TCP service detection)
  - Email Harvesting (page scraping + role-based guesses)
  - HTTP Fingerprinting (headers, security audit, tech detection)
- JSON and TXT report export functionality
- Settings menu for target management
- Results viewer with module summary
- Custom module selection
- Run all modules at once
- Colored terminal output with professional formatting
- Linux installer script (install.sh)
- Comprehensive error handling
- Concurrent processing for speed optimization

### Features
- Completely passive reconnaissance (no exploitation)
- FBI_Soldier & Team RedX branding
- Support for both domain and IP targets
- Customizable port scanning
- Professional CLI interface
- Real-time results display

### Documentation
- Comprehensive README.md
- MIT License
- CONTRIBUTING.md guidelines
- This CHANGELOG

---

## [1.0] - 2026-06-20

### Initial Release
- Basic CLI interface
- Core recon modules
- Command-line argument parsing
- Simple output formatting

---

## Planned Features (Future Releases)

### [2.1] - Planned
- [ ] Shodan API integration
- [ ] SSL/TLS certificate analysis
- [ ] Reverse DNS lookups
- [ ] CNAME flattening detection
- [ ] Performance improvements

### [3.0] - Planned
- [ ] HTML report generation
- [ ] API mode (non-interactive)
- [ ] Proxy support
- [ ] Custom wordlist support
- [ ] Batch file input
- [ ] Database storage option

---

## Known Issues

None currently reported. Please open an issue if you find any bugs.

---

## Security Notices

### v2.0
- All reconnaissance is passive
- No exploitation attempted
- Standard protocol behavior only
- Requires authorization before use on any system

---

## Contributors

- **FBI_Soldier** - Creator & Lead Developer
- **Team RedX** - Project Team

---

For detailed changes, see commits on GitHub.
