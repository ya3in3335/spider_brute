#!/bin/bash

# مسح الشاشة وعرض بانر
clear
echo -e "\e[1;31m"
figlet "SPIDER BRUTE"
echo -e "\e[1;33m⚡ Preparing the setup for Timo's tool..."
echo -e "\e[1;34m=====================================================\e[0m"

# تحديث النظام
echo -e "\e[1;32m[+] Updating system...\e[0m"
sudo apt update && sudo apt full-upgrade -y

# تثبيت Python و pip
echo -e "\e[1;32m[+] Installing Python and pip...\e[0m"
sudo apt install -y python3 python3-pip

# تثبيت أدوات مهمة لتفادي مشاكل الترجمة
echo -e "\e[1;32m[+] Installing build essentials...\e[0m"
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

# تثبيت Tor
echo -e "\e[1;32m[+] Installing Tor...\e[0m"
sudo apt install -y tor

# تثبيت أدوات الطرفية (figlet, termcolor, إلخ)
echo -e "\e[1;32m[+] Installing Python libraries via apt if available...\e[0m"
sudo apt install -y python3-requests python3-stem python3-paramiko python3-pyfiglet python3-termcolor

# بعض المكتبات غير موجودة على apt، نثبتها بـ pip
echo -e "\e[1;32m[+] Installing missing libraries with pip...\e[0m"
python3 -m pip install --break-system-packages requests stem paramiko pyfiglet termcolor

# تثبيت figlet لعرض الشعار
sudo apt install -y figlet

# تشغيل خدمة Tor
echo -e "\e[1;32m[+] Starting Tor service...\e[0m"
sudo service tor start

# التحقق من التثبيت
echo -e "\n\e[1;36m[✔] Verifying installation..."
python3 -c "import requests, stem, paramiko, pyfiglet, termcolor; print('✅ All Python modules loaded successfully!')"

echo -e "\n\e[1;32m[✔] All done. Run the tool now with:\e[1;33m\npython3 ssp.py\n\e[0m"
