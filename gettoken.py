#get token
from random import randint
from sys import platform
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys
import json
from time import sleep, strftime
import requests
from time import strftime
from time import sleep
import os
from datetime import datetime
from time import sleep
session = requests.Session()
# thời gian
now = datetime.now()
thu = now.strftime("%A")
ngay = now.strftime("%d")
thang = now.strftime("%m")
nam = now.strftime("%Y")
time = datetime.now().strftime("%H:%M:%S")
# color
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
tim = "\033[1;35m"
xnhat = "\033[1;32m"
hong = "\033[1;95m"
##### Cài Thư Viện #####
try:
    import requests
except:
    os.system("pip install requests")
# thanh nganh
def thanh(so):
    a = "────"*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()
# def mạng
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
# head
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
def clear():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
        os.system("cls")
def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()
khocookie = []
for a in range(1, 999999):
    nhapcookie = input(f"{luc}NHẬP COOKIE THỨ {a}: {vang}")
    if nhapcookie == "":
        break
    khocookie.append(nhapcookie)
file_save = ("token_eaavk.txt")
Write.Print("ĐANG GET TOKEN... \r", Colors.red_to_green)
Write.Print("-"*75,Colors.white_to_red)
def eaavk(cookie):
    head = {
        "Host": "m.facebook.com",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "dnt": "1",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": cookie
    }
    get = requests.get("https://m.facebook.com/dialog/oauth?encrypted_query_string=AeAjv8MAG1mxBW7fHarsgxqBWrErwVj510ZxrxzcU5ohUKyw9Ec2SbWAsOGSXnM1lePxp4L2H_3nOf9DD9NyxeJMVyDCyPZExu9EQ6L0GIcC-z0itodT5plPj4fJs28W-E4hnslLlCnRDQfu8Ho-P0l6vP7-t6xaXIw6VsPq-DZLrOKCPiI6f0tq1CijGzlelkVbqrXF5lqw36Pn4wJ2YHG9OWeNfWfaKNohRvnCxnz7bwffhkXrNxJE_zMhUUfaS0c", headers=head).text
    data = {
        "fb_dtsg": get.split('name="fb_dtsg" value="')[1].split('"')[0],
        "jazoest": get.split('name="jazoest" value="')[1].split('"')[0],
        "scope": get.split('name="scope" value="')[1].split('"')[0],
        "display": "touch",
        "sdk": "",
        "sdk_version": "",
        "domain": "",
        "sso_device": "",
        "state": "",
        "user_code": "",
        "nonce": "",
        "logger_id": get.split('name="logger_id" value="')[1].split('"')[0],
        "auth_type": "",
        "auth_nonce": "",
        "code_challenge": "",
        "code_challenge_method": "",
        "encrypted_post_body": get.split('name="encrypted_post_body" value="')[1].split('"')[0],
        "return_format[]": "access_token"
    }
    head = {
        "Host": "m.facebook.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://m.facebook.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://m.facebook.com/dialog/oauth?encrypted_query_string=AeAjv8MAG1mxBW7fHarsgxqBWrErwVj510ZxrxzcU5ohUKyw9Ec2SbWAsOGSXnM1lePxp4L2H_3nOf9DD9NyxeJMVyDCyPZExu9EQ6L0GIcC-z0itodT5plPj4fJs28W-E4hnslLlCnRDQfu8Ho-P0l6vP7-t6xaXIw6VsPq-DZLrOKCPiI6f0tq1CijGzlelkVbqrXF5lqw36Pn4wJ2YHG9OWeNfWfaKNohRvnCxnz7bwffhkXrNxJE_zMhUUfaS0c",
        "accept-encoding": "gzip, deflate",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": cookie
    }
    url = "https://m.facebook.com/dialog/oauth/skip/submit/" + get.split('/dialog/oauth/skip/submit/')[1].split('"')[0]
    url = url.replace("amp;", "")
    get = requests.post(url, headers=head, data=data).text
    try:
        return get.split('access_token=')[1].split('&')[0]
    except:
        return "die"
a = 0
for i in range(len(khocookie)):
    a = a+1
    cookie = khocookie[i]
    print(f'{luc}TOKEN THỨ {a}:',vang+eaavk(cookie))