import os
from pystyle import Write,Colors
try:
    from time import sleep
    import requests,threading,os
    import pyfiglet, os
except:
  os.system("pip install python-time")
  os.system("pip install requests")
  os.system("pip install threaded")
  os.system("pip install pyfiglet")
# =========================== [ MÀU ] ===========================
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"


def clear():
        if os.name=='nt':os.system('cls')
        else:os.system('clear')

    
clear()
uid = input(f'{luc}NHẬP ID BÀI VIẾT{trang}: ')
token_fb = input(f'{luc}NHẬP TOKEN CHỨA PAGE{trang}: ')

clear()
def shareao(num):
    getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}").json()['data']
    for tach in getTokenPage:
        uid_page=tach['id']
        access_token_page=tach['access_token']
        buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}").text
        if "error" in buff:
            print(f'{luc}ID: {vang}{uid_page}{trang} | {xanhbien}SHARE THẤT BẠI')
        else:
            print(f'{luc}ID: {vang}{uid_page}{trang} | {xanhbien}SHARE THÀNH CÔNG')




while True:
        t1 = threading.Thread(target=shareao, args=(10,))
        t1.start()

        sleep(0.1)
        
