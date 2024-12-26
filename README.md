# PakSimLookup

## Overview
PakSimLookup is a Python-based tool designed to extract information using either a mobile number (starting with 92) or a CNIC (without dashes). It provides details such as Mobile Number, Name, CNIC, and Address. This tool is intended to assist in identifying individuals and addressing abusive behavior or misconduct.

## Disclaimer
**⚠️The author of this tool is not responsible for any misuse or illegal activities** carried out using this tool. It is solely the responsibility of the user to ensure compliance with local laws and regulations. This tool is intended for ethical use only, such as for identifying abusers.

---

## Features
-  Fetch details using a **mobile number** (must start with 92).
-  Fetch details using a **CNIC** (without dashes).

---

## Requirements
- Python 3.x
- VPN connection (recommended: OpenVPN🔒)

---

## VPN Installation
Vpn is required to make connection with database. OpenVPN is highly recommended for its reliability and ease of use. I have provided configuration file for vpn connection you can use that file. Below are the commands to install Python and OpenVPN in Windows and Linux:

### 💻 Windows (PowerShell)
To install Python and OpenVPN, run the following commands in your powershell:
```powershell
winget install python
winget install OpenVPNTechnologies.OpenVPNConnect
```

### 🐧 Linux (Terminal)
To install OpenVPN, run the following command:
```bash
apt update && apt-get upgrade
apt install openvpn -y
```

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/0kraven/PakSimLookup.git
   ```
2. Navigate to the tool’s directory:
   ```bash
   cd PakSimLookup
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
Run the following commands from your terminal:

### Using Mobile Number
```bash
python3 paksimlookup.py --number 923001234567
```

### Using CNIC
```bash
python3 paksimlookup.py --cnic 1234512345671
```

### Example Output
```
+----------------------------------------------------+
| Mobile       | Name     | CNIC          | Address  |
+--------------+----------+---------------+----------+
| 923001234567 | abcdef   | 1234512345671 |   xyz    |
+----------------------------------------------------+
```


## Author
- GitHub: [Okraven](https://github.com/0kraven)
---

## Legal Disclaimer
⚖️PakSimLookup is provided "as is" without any guarantees or warranties. Users are strictly prohibited from using this tool for illegal activities, including but not limited to unauthorized access to private information. By using this tool, you agree to take full responsibility for your actions.

---

## Contribution
🌟Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
[MIT License](LICENSE)

