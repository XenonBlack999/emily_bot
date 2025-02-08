# Emily - Your AI Assistant for Cybersecurity

## Overview
Penetration Testing Helper Bot is a Python-based tool that simplifies common penetration testing workflows. This helper bot can:
- Scan websites for vulnerabilities.
- Provide a list of necessary penetration testing engines/tools suitable for the scanned target.
- Generate easy-to-understand results to help new penetration testers feel comfortable using it.

This project is ideal for students, professionals, or anyone looking to automate portions of their ethical hacking and security assessment tasks.

## Features

- Website Scanner:
  - Analyze websites for:
    - Open Ports
    - Exposed Services
    - Basic Vulnerability Checks
- List Pen-Testing Engines:
  - Suggest appropriate tools (e.g., Nmap, Nikto, OWASP ZAP) based on findings.
- User-Friendly Design:
  - Makes it easy for beginners to navigate through complex penetration testing processes.
- Extensible:
  - Add new engines and features for advanced users.

---
## Requirements

- Python 3.x
- Required Python packages:
  - nmap (install using pip install python-nmap)
  - ipaddress (included in Python standard library)

## Installation

1. Clone this repository or download the script.
2. Install the required packages:
   ```bash
   pip install python-nmap
   
