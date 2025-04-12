#!/bin/bash

# مسح الشاشة وعرض بانر
clear
echo -e "\e[1;31m"
figlet "SPIDER BRUTE"
echo -e "\e[1;33m⚡ Preparing the setup for Timo's tool..."
echo -e "\e[1;34m=====================================================\e[0m"

# تحديث النظام
#!/bin/bash

echo -e "\e[33m[+] Updating system and installing dependencies...\e[0m"
sudo apt update && sudo apt upgrade -y

# تثبيت بايثون والأدوات اللازمة
sudo apt install -y python3 python3-pip python3-venv tor figlet

# إنشاء virtual environment لتجنب مشاكل pip
echo -e "\e[33m[+] Creating Python virtual environment...\e[0m"
python3 -m venv venv_spider
source venv_spider/bin/activate

# تثبيت المكتبات داخل البيئة الافتراضية
echo -e "\e[33m[+] Installing Python libraries...\e[0m"
pip install requests stem paramiko pyfiglet termcolor

echo -e "\e[32m[✔] All tools and libraries installed successfully!\e[0m"
echo -e "\e[36m[!] To run the script, use: source venv_spider/bin/activate && python3 your_script.py\e[0m"
