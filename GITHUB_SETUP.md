# 🚀 How to Upload ReconX to GitHub

Complete step-by-step guide to create your GitHub repository.

---

## Step 1: Create GitHub Account (if needed)

1. Go to https://github.com
2. Click "Sign up"
3. Fill in email, password, username
4. Verify email address

---

## Step 2: Create a New Repository

1. Log in to GitHub
2. Click **+** icon (top right) → **New repository**
3. Fill in details:
   - **Repository name:** `reconx`
   - **Description:** `OSINT & Reconnaissance Framework - Built by FBI_Soldier | Team RedX`
   - **Visibility:** Public (so others can find it)
   - **Initialize with:** ✅ Add .gitignore (Python)
   - **License:** MIT License

4. Click **Create repository**

---

## Step 3: Get Repository URL

After creating, you'll see:
```
https://github.com/your-username/reconx.git
```

Copy this URL (you'll need it).

---

## Step 4: Setup Git Locally

### First Time Setup

```bash
# Configure Git with your GitHub info
git config --global user.name "Your Name"
git config --global user.email "your-email@github.com"

# Generate SSH key (optional but recommended)
ssh-keygen -t ed25519 -C "your-email@github.com"
```

### Add SSH Key to GitHub (Optional)

1. Copy your SSH public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to GitHub → Settings → SSH and GPG keys
3. Click "New SSH key"
4. Paste your key

---

## Step 5: Upload ReconX Code

### Option A: Using Command Line (Recommended)

```bash
# Navigate to your reconx directory
cd /path/to/reconx

# Initialize Git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: ReconX OSINT Framework v2.0"

# Add remote repository
git remote add origin https://github.com/your-username/reconx.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Option B: Drag & Drop (If you prefer GUI)

1. Go to your GitHub repo
2. Click "Add file" → "Upload files"
3. Drag and drop your reconx folder contents
4. Click "Commit changes"

---

## Step 6: Verify Upload

After pushing, check your GitHub repo:

```
✅ README.md
✅ LICENSE
✅ CONTRIBUTING.md
✅ CHANGELOG.md
✅ QUICKSTART.md
✅ install.sh
✅ requirements.txt
✅ reconx.py
✅ modules/
   ├── whois_lookup.py
   ├── dns_enum.py
   ├── subdomain.py
   ├── port_scan.py
   ├── email_harvest.py
   └── http_fingerprint.py
✅ utils/
   └── reporter.py
✅ .github/workflows/
   └── python-tests.yml
```

---

## Step 7: Add GitHub Topics (Optional)

1. Go to repo Settings
2. Scroll to "Repository topics"
3. Add tags:
   - `osint`
   - `reconnaissance`
   - `penetration-testing`
   - `security-tools`
   - `python`
   - `ctf`
   - `infosec`

---

## Step 8: Create GitHub Release

1. Go to repo → **Releases** (right sidebar)
2. Click "Create a new release"
3. Fill in:
   - **Tag version:** `v2.0`
   - **Release title:** `ReconX v2.0 - Initial Release`
   - **Description:**
     ```
     # ReconX v2.0 Release

     Initial production release of ReconX OSINT Framework.

     ## Features
     - 6 comprehensive recon modules
     - Interactive terminal interface
     - JSON/TXT report export
     - Completely passive reconnaissance
     - FBI_Soldier & Team RedX branding

     ## What's New
     - WHOIS Lookup module
     - DNS Enumeration (A, AAAA, MX, NS, TXT, SOA, CNAME, PTR)
     - Subdomain Discovery (concurrent brute-force)
     - Port Scan & Banner Grab
     - Email Harvesting
     - HTTP Fingerprinting & Security Audit

     ## Installation
     ```bash
     git clone https://github.com/your-username/reconx.git
     cd reconx
     chmod +x install.sh
     ./install.sh
     ```

     For more info, see README.md

     Built by FBI_Soldier | Team RedX
     ```

4. Check "This is a pre-release" if needed
5. Click "Publish release"

---

## Step 9: Setup GitHub Actions (CI/CD)

Already included! Your `.github/workflows/python-tests.yml` will:
- Run on every push
- Test Python 3.8+
- Lint code
- Check imports
- Run security checks

Check status: **Actions** tab in your repo

---

## Step 10: Add Badges to README

Your README already has them, but here's how to customize:

```markdown
![ReconX Banner](https://img.shields.io/badge/Version-2.0-cyan?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/your-username/reconx?style=flat-square)
```

---

## Step 11: Share Your Project

### Social Media Post Template

```
🔐 Excited to release ReconX - a professional OSINT & reconnaissance framework!

✅ 6 comprehensive recon modules
✅ Interactive terminal interface  
✅ Completely passive reconnaissance
✅ Perfect for pentesting & CTF competitions

Built by @FBI_Soldier | Team RedX

GitHub: github.com/your-username/reconx

#cybersecurity #osint #infosec #penetrationtesting #python #hacking #ctf
```

### Reddit Post (r/SecurityCraft, r/Python, r/cybersecurity)

**Title:** ReconX - Open Source OSINT Framework (Interactive CLI)

**Body:**
```
Hi everyone! I just released ReconX, a professional OSINT & reconnaissance 
framework built by FBI_Soldier and Team RedX.

Features:
- 6 recon modules (WHOIS, DNS, Subdomains, Port Scan, Email, HTTP Fingerprinting)
- Beautiful interactive terminal menu
- JSON/TXT report export
- Completely passive (no exploitation)
- Perfect for pentesting & CTF competitions

GitHub: https://github.com/your-username/reconx

Feedback and contributions welcome!
```

---

## Step 12: GitHub Settings & Protection

### Branch Protection (Optional)

1. Settings → Branches
2. Add rule for `main` branch
3. Require pull request reviews
4. Require status checks to pass

### Collaborators

To invite teammates:
1. Settings → Collaborators
2. Add GitHub usernames

---

## Making Future Updates

```bash
# After making changes locally:
git add .
git commit -m "Feature: Add description"
git push origin main

# Create new release:
git tag -a v2.1 -m "Version 2.1"
git push origin v2.1
```

---

## File Structure Your Repo Should Have

```
your-username/reconx/
├── README.md                          ← Main documentation
├── QUICKSTART.md                      ← Getting started guide
├── CONTRIBUTING.md                    ← Contribution guidelines
├── CHANGELOG.md                       ← Version history
├── LICENSE                            ← MIT License
├── .gitignore                         ← Git ignore rules
├── .github/
│   └── workflows/
│       └── python-tests.yml          ← CI/CD pipeline
├── reconx.py                          ← Main application
├── requirements.txt                   ← Dependencies
├── install.sh                         ← Linux installer
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain.py
│   ├── port_scan.py
│   ├── email_harvest.py
│   └── http_fingerprint.py
└── utils/
    └── reporter.py
```

---

## Common GitHub Commands

```bash
# Clone your repo
git clone https://github.com/your-username/reconx.git

# Check status
git status

# Stage changes
git add .

# Commit with message
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create a branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Merge branch
git merge feature/new-feature

# View commit history
git log --oneline

# Create a tag for release
git tag -a v2.1 -m "Version 2.1 release"
```

---

## Troubleshooting

### "Permission denied (publickey)"
- Generate SSH key: `ssh-keygen -t ed25519 -C "your-email@github.com"`
- Add to GitHub Settings → SSH Keys
- Or use HTTPS instead of SSH

### "fatal: not a git repository"
- Run `git init` in your repo directory

### "Updates were rejected"
- Pull first: `git pull origin main`
- Then push: `git push origin main`

### Large files rejected
- GitHub has 100MB file limit
- Delete from git history or use Git LFS

---

## Next Steps

1. ✅ Create GitHub account
2. ✅ Create repository
3. ✅ Push ReconX code
4. ✅ Create v2.0 release
5. ✅ Share on social media
6. ✅ Get community feedback
7. ✅ Plan future features (Shodan, SSL certs, etc.)

---

## GitHub Repository URL

After uploading:
```
https://github.com/your-username/reconx
```

Share this link! 🚀

---

## Final Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to main branch
- [ ] README displays correctly
- [ ] LICENSE file present
- [ ] Topics added
- [ ] Release v2.0 created
- [ ] GitHub Actions running
- [ ] Shared on social media

---

**Congratulations! Your ReconX project is now open source!** 🎉

Built by FBI_Soldier | Team RedX
