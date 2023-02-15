import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

script_version = '1.0'
window_title = f"WARP+ by Aiko (version {script_version})"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' +
          window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print(
    "[*] Fix error - Call : Aiko#sociu"
)
print("")
print(f"[-] Version: {script_version}")
print("--------")
print(
    "[+] ID WARP Take at the app 1.1.1.1: Settings > Advanced > Diagnostics > ID")

# Update ID WARP here
referrer = '15cdbfd4-98da-4565-9f7b-b63a77aec04c'

def progressBar():
	animation = [
	    "[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]",
	    "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
	    "[■■■■■■■■□□]", "[■■■■■■■■■□]"
	]
	progress_anim = 0
	save_anim = animation[progress_anim % len(animation)]
	percent = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Wait for feedback...  " + save_anim +
			                 f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Completed orders ... [■■■■■■■■■■] 100%")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)


def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
	try:
		install_id = genString(22)
		body = {
		    "key": "{}=".format(genString(43)),
		    "install_id": install_id,
		    "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
		    "referrer": referrer,
		    "warp_enabled": False,
		    "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
		    "type": "Android",
		    "locale": "en_EN"
		}
		data = json.dumps(body).encode('utf8')
		headers = {
		    'Content-Type': 'application/json; charset=UTF-8',
		    'Host': 'api.cloudflareclient.com',
		    'Connection': 'Keep-Alive',
		    'Accept-Encoding': 'gzip',
		    'User-Agent': 'okhttp/3.12.1'
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print("")
		print(error)


g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("[*] Note: Run on the Action of github")
	print("")
	sys.stdout.write("\r[+] Sending orders...   [□□□□□□□□□□] 0%")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print(f"\n[-] ID: {referrer}")
		print(f"[:)] Add +{g}GB data WARP+ go to your warp key")
		print(f"[#] Result: {g} Ok | {b} No")
		for i in range(20, 0, -1):
			sys.stdout.write(f"\r[*] After {i} second, The command will be sent...")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[:(] Error connecting to the server.")
		print(f"[#] Result: {g} Ok | {b} No")
		for i in range(20, 0, -1):
			sys.stdout.write(f"\r[*] Try again {i}s...")
			sys.stdout.flush()
			time.sleep(1)
