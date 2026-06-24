# Contributing to ReconX

Thank you for your interest in contributing to ReconX! We welcome contributions from security researchers, developers, and the cybersecurity community.

## Code of Conduct

- Be respectful and professional
- Follow ethical hacking practices
- Respect intellectual property and privacy
- Report security vulnerabilities responsibly
- No malicious or harmful code

## How to Contribute

### 1. Fork the Repository
```bash
git clone https://github.com/your-username/reconx.git
cd reconx
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Keep code clean and well-documented
- Follow Python PEP 8 style guide
- Add comments for complex logic
- Test thoroughly before submitting

### 3. Commit & Push
```bash
git add .
git commit -m "Add: description of changes"
git push origin feature/your-feature-name
```

### 4. Create Pull Request
- Provide clear description of changes
- Reference any related issues
- Include testing instructions
- Add yourself to contributors list if desired

## Feature Ideas

### Priority High
- [ ] Shodan API integration
- [ ] SSL/TLS certificate analysis
- [ ] Reverse DNS lookups
- [ ] HTML report generation

### Priority Medium
- [ ] CNAME flattening detection
- [ ] MX record validation
- [ ] Web technologies database (like Wappalyzer)
- [ ] Batch file input support

### Priority Low
- [ ] Proxy support
- [ ] Custom wordlist support
- [ ] API mode (non-interactive)
- [ ] Performance benchmarks

## Bug Reports

Found a bug? Open an issue with:
- Detailed description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages/logs

## Code Standards

### Module Template
```python
def run_module_name(target):
    """
    Description of what the module does.
    
    Args:
        target (str): Domain or IP address
        
    Returns:
        dict: Results dictionary
    """
    results = {}
    try:
        # Module logic here
        pass
    except Exception as e:
        results["error"] = str(e)
    return results
```

### Error Handling
- Always wrap in try/except
- Return error in results dict
- Use appropriate logging
- Don't exit/crash the program

### Output Format
- Use Colors from colorama
- Keep tables aligned with tabulate
- Provide user feedback for long operations
- Clear success/error messages

## Testing

Before submitting:
```bash
# Test your module
python3 -c "from modules.your_module import run_module; run_module('example.com')"

# Run full tool
python3 reconx.py
```

## Security Considerations

- No hardcoded credentials
- No dangerous shell commands
- Validate all user inputs
- Handle exceptions gracefully
- Document security assumptions

## Documentation

- Update README.md for new features
- Add module documentation
- Include usage examples
- Document dependencies

## Questions?

- Check existing issues
- Review source code
- Open a discussion

---

**Thank you for helping make ReconX better!** 🔐
