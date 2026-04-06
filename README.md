# 📡 netcheck

A simple CLI tool for Wi-Fi network monitoring and scanning. Built on top of `airmon-ng` and `airodump-ng` from the `aircrack-ng` suite.

> ⚠️ **For educational and personal use only.** Only use on networks you own or have explicit permission to test.

---

## Features

- Enable / disable monitor mode on any Wi-Fi interface
- Full network scan — lists all visible access points
- Targeted scan — focus on a specific BSSID and channel
- Colorized terminal output via `colorama`

---

## Requirements

- Linux (tested on Debian / PiOS Lite)
- Python 3.x
- `aircrack-ng` suite installed (`airmon-ng`, `airodump-ng`)
- Root / sudo privileges

---

## Installation
```bash
git clone https://github.com/TRINIT82/netcheck.git
cd netcheck
pip install -r requirements.txt
```

---

## Usage

### Option 1 — run directly
```bash
sudo python3 main.py
```

### Option 2 — via shell script
```bash
chmod +x run.sh
sudo ./run.sh
```

---

## Menu
Wi-Fi Monitor

1. Start Monitoring
2. Stop Monitoring

<--------------------------------->

3. Start Scan
4. Targeted Scan

5. Exit

**Start Monitoring** — enables monitor mode on a specified interface (e.g. `wlan0mon`)  
**Stop Monitoring** — disables monitor mode  
**Start Scan** — runs `airodump-ng` to list all nearby networks  
**Targeted Scan** — scans a specific BSSID on a specific channel  

---

## Stack

- Python 3
- `colorama`
- `aircrack-ng` (`airmon-ng`, `airodump-ng`)
- Bash

---

## Disclaimer

This tool is intended for use on your own networks or in controlled environments where you have permission. Unauthorized network scanning may be illegal in your jurisdiction.
