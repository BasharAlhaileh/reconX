# Quick Start Guide - ReconX

Get up and running with ReconX in 2 minutes.

## Prerequisites

- Python 3.8 or higher
- Linux, Kali, or macOS
- Internet connection

Check your Python version:
```bash
python3 --version
```

## Installation

### Option 1: Using Installer (Recommended)

```bash
# 1. Clone or download the repo
git clone https://github.com/your-username/reconx.git
cd reconx

# 2. Make installer executable
chmod +x install.sh

# 3. Run installer
./install.sh

# 4. Answer prompts during installation
```

### Option 2: Manual Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/reconx.git
cd reconx

# 2. Install Python dependencies
pip3 install -r requirements.txt --break-system-packages

# 3. Make main script executable (optional)
chmod +x reconx.py

# 4. Run the tool
python3 reconx.py
```

## First Run

```bash
python3 reconx.py
```

You'll see the ReconX banner and main menu:

```
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗
...
  OSINT & Reconnaissance Framework v2.0
  Built by: FBI_Soldier | Team: RedX
```

## Basic Workflow

### Step 1: Select a Target
```
[MAIN MENU]
1 → Select Target
[?] Enter choice: 1
[?] Enter target (domain or IP): example.com
[✓] Target set: example.com
```

### Step 2: Run Reconnaissance
```
[MAIN MENU]
2 → Run Reconnaissance
[?] Enter choice: 2

[SELECT MODULE]
1 → WHOIS Lookup
2 → DNS Enumeration
3 → Subdomain Discovery
4 → Port Scan & Banner Grab
5 → Email Harvesting
6 → HTTP Fingerprinting
7 → Run All Modules
...
```

### Step 3: View Results
```
[MAIN MENU]
3 → View Results
[?] Enter choice: 3

Shows summary of all modules run:
- Target: example.com
- Modules: 6
- Findings from each module
```

### Step 4: Export Results
```
[MAIN MENU]
4 → Export Results
[?] Enter choice: 4

[EXPORT RESULTS]
1 → JSON Format
2 → Text Format

[?] Enter filename: myreport
[✓] Report exported to: myreport.json
```

## Common Tasks

### Run a Single Module

```
1. Select Target → example.com
2. Run Reconnaissance
   [?] Enter choice: 4  (Port Scan)
```

### Run Custom Modules

```
2. Run Reconnaissance
   [?] Enter choice: 8  (Custom Selection)
   [?] Run WHOIS Lookup? [y/n]: y
   [?] Run DNS Enumeration? [y/n]: y
   [?] Run Subdomain Discovery? [y/n]: n
   ...
```

### Run All Modules at Once

```
2. Run Reconnaissance
   [?] Enter choice: 7  (Run All Modules)
```

## Module Descriptions

| Module | Time | Use Case |
|--------|------|----------|
| WHOIS | Fast | Domain ownership info |
| DNS | Fast | Mail servers, nameservers |
| Subdomains | Slow | Find hidden services |
| Port Scan | Slow | Open service detection |
| Email | Fast | Organizational contacts |
| HTTP Fingerprint | Fast | Web server tech stack |

**Tip:** Skip slow modules (3, 4) if you're in a hurry.

## Tips & Tricks

### Change Target Mid-Session
```
5. Settings → 1. Change Target
```

### Clear Previous Results
```
5. Settings → 2. Clear Results
```

### View Configuration
```
5. Settings → 3. View Configuration
```

### Troubleshooting

**"Command not found"**
```bash
# Make sure you're in the reconx directory
cd /path/to/reconx
python3 reconx.py
```

**"ModuleNotFoundError"**
```bash
# Reinstall dependencies
pip3 install -r requirements.txt --break-system-packages
```

**"Permission denied" on install.sh**
```bash
chmod +x install.sh
./install.sh
```

## Example: Complete Recon Session

```bash
# Start the tool
python3 reconx.py

# Follow these inputs:
[?] Enter choice: 1
[?] Enter target: google.com
[?] Press Enter...

[?] Enter choice: 2
[?] Enter choice: 7  (Run all modules)
[?] Press Enter...

# Wait for all modules to complete
[?] Enter choice: 3  (View results)
[?] Press Enter...

[?] Enter choice: 4  (Export)
[?] Enter choice: 1  (JSON)
[?] Enter filename: google_recon
[?] Enter choice: 0  (Exit)
```

## File Output

After exporting, you'll have:
- `google_recon.json` - Machine-readable results
- Can be processed with `jq` or imported into tools

## Next Steps

- Read the full [README.md](README.md)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for extending the tool
- Review module source code in `modules/`
- Open issues on GitHub

## Need Help?

- **Installation issues:** Check Python version, dependencies
- **Runtime errors:** Check target format (domain vs IP)
- **Slow performance:** Skip subdomain discovery or port scan
- **No results:** Target may not respond or DNS may be blocking

## Legal Reminder

✅ Always get written authorization before testing systems you don't own
✅ Follow responsible disclosure practices
✅ Comply with local laws and regulations

---

**Enjoy exploring with ReconX!** 🔐

Built by FBI_Soldier | Team RedX
