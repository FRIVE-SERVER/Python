# import
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
dem = 0
# thời gian
now = datetime.now()
thu = now.strftime("%A")
ngay = now.strftime("%d")
thang = now.strftime("%m")
nam = now.strftime("%Y")
time = datetime.now().strftime("%H:%M:%S")
# color
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xnhac = "\033[1;20m"
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
# Đánh dấu bản quyền
thanh_xau = trang + "" + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
##### Cài Thư Viện #####
bug_duoc_cai_lon = {'pass': 'bongocvidaii'}
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
##### Cài Thư Viện #####
try:
    import requests
except:
    os.system("pip install requests")
# thanh ngang
def thanh(so):
    a = f"{hong}────"*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()
# head
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
logos = f""""""
thongtin = f""""""
def clear():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
        os.system("cls")
def banner():
    print('\033[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, logos)
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()
    print(thongtin)
def daccau(so):
    a = f"{hong}────"*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()
clear()
class OOO0000OO00O0OO0O :
    def __init__ (OO0O00OOO0O0OO000 ):
        OO0O00OOO0O0OO000 .__O000OO0O000O00OO0 ()
        OO0O00OOO0O0OO000 .__OOO0000O0O0OO0000 ()
        OO0O00OOO0O0OO000 .__O0O0OOO0OOO0O00OO ()
        OO0O00OOO0O0OO000 .__OOOO0O00OO0O00OO0 ()
        OO0O00OOO0O0OO000 .__O0O00OO000000O0OO ()
        OO0O00OOO0O0OO000 .__O000000O000O00OOO ()
    def __O000OO0O000O00OO0 (OOOO00OO0OOO0O000 ,O0OO0OOO000O0O00O ,OO000OOOOOOO00OO0 ,OOO00O000OOO0OOOO ,OO00000O0OO0OOO00 ,OO00OO0O0O0000000 ,O0OOO0O00OOO0O0OO ,OO0O0OOO0OO0OOO0O ):
        return OOOO00OO0OOO0O000 .__O0O00OO000000O0OO ()
    def __OOO0000O0O0OO0000 (OO0OOO00000O00000 ,O000OO00O000O00O0 ,O0O0O00O0O000000O ,OO000OO00O000OO00 ,OOO0OO00O0O0O0O0O ):
        return OO0OOO00000O00000 .__O0O0OOO0OOO0O00OO ()
    def __O0O0OOO0OOO0O00OO (OOOOOO0000O00OO0O ,O0OO0OOO00O000OO0 ,OO0O0O000000000O0 ):
        return OOOOOO0000O00OO0O .__O0O0OOO0OOO0O00OO ()
    def __OOOO0O00OO0O00OO0 (O00O0O00O0O000O00 ,O0O0OO0O000OOOOOO ,OO00OOOO00O00000O ,OOOOOOOOOO000O00O ,OOOO000O0000OOO0O ,OOOOOOOO0O00O0O00 ,O000O000OO00O000O ):
        return O00O0O00O0O000O00 .__O0O00OO000000O0OO ()
    def __O0O00OO000000O0OO (OO00OO0OOO000O0OO ,O0000OOO000O0O0OO ,OO0OO0OO00OO0OO0O ,OOO00O0O0O0OO00O0 ,O000O00OO0O000OOO ):
        return OO00OO0OOO000O0OO .__OOOO0O00OO0O00OO0 ()
    def __O000000O000O00OOO (OOO0OO0O000OO0OOO ,OO00O0OOOOOO0OOOO ,O0OOOO0OOO0OOOO00 ,OOOO0O0000OO00000 ,O0O0O0OOOOOO0000O ,O000OOO00O00OOO0O ,OOO00OO00OO000O0O ,O00000000O0000OO0 ):
        return OOO0OO0O000OO0OOO .__O0O00OO000000O0OO ()
class OO00O0O00OO00OOOO :
    def __init__ (OO0OO0O00O00O0O00 ):
        OO0OO0O00O00O0O00 .__OOOOOO0OO0OOO0OOO ()
        OO0OO0O00O00O0O00 .__OO00OOOO0000O000O ()
        OO0OO0O00O00O0O00 .__O0O00O00O000OOO0O ()
        OO0OO0O00O00O0O00 .__OOO0OOO0O0O00OO00 ()
        OO0OO0O00O00O0O00 .__OO000O0000OOO0OOO ()
        OO0OO0O00O00O0O00 .__OOOO0000O000O00OO ()
        OO0OO0O00O00O0O00 .__O0O00O00OO000OOOO ()
        OO0OO0O00O00O0O00 .__OO0000O00OO0O00O0 ()
        OO0OO0O00O00O0O00 .__OOO0OOO000OO00O0O ()
        OO0OO0O00O00O0O00 .__OOO00OO0OO0OO0O00 ()
        OO0OO0O00O00O0O00 .__OOO0O000O00OO00OO ()
        OO0OO0O00O00O0O00 .__OO0OO0O00O000O0OO ()
        OO0OO0O00O00O0O00 .__OO00OOO00OO00O0O0 ()
    def __OOOOOO0OO0OOO0OOO (OOO00O0O000O0000O ,O0O0O0000OOO0O0O0 ,O000O000O00000OOO ,O0000O00OOOOO0O0O ,O0OOO000OO0O00OO0 ,OOOO000O0O00O00O0 ,O0O0O00OO00OO0000 ,O0O000O000O0OOOOO ):
        return OOO00O0O000O0000O .__OOO0O000O00OO00OO ()
    def __OO00OOOO0000O000O (O000O0OOO0OO00000 ,OOO0OOOOOOOO00OO0 ,OO0OO0OOOO0O0OOOO ,O00O00OO0OOO0OOOO ,OOO00OO0O0000O0O0 ):
        return O000O0OOO0OO00000 .__OOO0OOO0O0O00OO00 ()
    def __O0O00O00O000OOO0O (O0O00OOO00OOO0O00 ,O00O000000OOO0OO0 ,O0O00O00O0OO0OO0O ,OO00O00O00O000O00 ):
        return O0O00OOO00OOO0O00 .__OOO0O000O00OO00OO ()
    def __OOO0OOO0O0O00OO00 (O0OO000000OO000OO ,OO00OOOOO00O00O00 ,OO0OO0OOO0OO0O000 ,OOOO00OOOOO0OOO0O ,O0O00OO0O0OO0OOO0 ,OOOO0O00O00000O0O ):
        return O0OO000000OO000OO .__O0O00O00O000OOO0O ()
    def __OO000O0000OOO0OOO (O00OO0O00O000O00O ,O00O0OO0O00OOO0O0 ,OOO00O00O0O0O0O00 ,O0OOO00OO00000O00 ,O0O0O0O000OOOO00O ):
        return O00OO0O00O000O00O .__OOO0O000O00OO00OO ()
    def __OOOO0000O000O00OO (OO00OOO0OO0O00OO0 ,OOO00O0O0OOOO00OO ,O0O0000O0O0O00OOO ,OOO0OOOO0O0000O0O ,O000OO0O00OO0O000 ):
        return OO00OOO0OO0O00OO0 .__OOO0OOO0O0O00OO00 ()
    def __O0O00O00OO000OOOO (OOOOOO0OOOO0OOOO0 ,O0O0O0O0000O00O00 ,OO0O00O000OOOOO00 ,O00OO0000O00OO000 ,O0OO00OO0000000O0 ,O0000O0O0O00OO00O ):
        return OOOOOO0OOOO0OOOO0 .__OO000O0000OOO0OOO ()
    def __OO0000O00OO0O00O0 (O00O00OOOOOOO0O00 ,O00O0O0O00O0O0O00 ,OOOOO00O00OOO0O0O ,O0OOOO0O0O0OO0OO0 ,O0O0OO0O00000OO00 ,O00OOO0OOOO0OOO0O ,OO0O000O00O0O0O00 ,OO0OO00O00O00OOO0 ):
        return O00O00OOOOOOO0O00 .__OOO0OOO000OO00O0O ()
    def __OOO0OOO000OO00O0O (OO000OOO0OOO000O0 ,O00O0O0O0OOOO0OOO ,OOO0O0000O0OO0O0O ,OOO0OOOOOO0OOOO0O ,O00OO00OOOOO0O00O ,OOOOOO00OO0O000O0 ,O0OO00OO000O00OO0 ,OO0OO0O0OO0O000OO ):
        return OO000OOO0OOO000O0 .__OOO0OOO0O0O00OO00 ()
    def __OOO00OO0OO0OO0O00 (O0O00000O00O00OOO ,O000O000OO0O0O0O0 ,OO00O000000O00OO0 ,OO0000OO0O0O0O0OO ):
        return O0O00000O00O00OOO .__OO00OOOO0000O000O ()
    def __OOO0O000O00OO00OO (O0OO00O0O0O0000OO ,OOO0O0OOOO00OO00O ,OOOOO0OOO000OO0OO ):
        return O0OO00O0O0O0000OO .__OO00OOOO0000O000O ()
    def __OO0OO0O00O000O0OO (OO0OOOO0OO0O00000 ,OO00OO0O0O0OO00OO ,OOO0000O0O00O00OO ,OO0OO000O0O0OO0OO ,OOO00O00O0OOOO00O ,O0OO000O00OOO0OOO ,O00OO0OOO0OOOO0O0 ,O00OO00000O00O0O0 ):
        return OO0OOOO0OO0O00000 .__OOO0OOO000OO00O0O ()
    def __OO00OOO00OO00O0O0 (OO00OOO000OOO0OO0 ,O000OOOO0000000OO ,O0OOOOOO0OOO0O00O ,OO00000OO0O00O000 ,OO0O0OO000O0O0000 ,OO000OO00OO0O00O0 ):
        return OO00OOO000OOO0OO0 .__O0O00O00O000OOO0O ()
class O0OO0O0OO0OO00O0O :
    def __init__ (OOO00O000O0OOO000 ):
        OOO00O000O0OOO000 .__O0O0OO0O0OO0OO000 ()
        OOO00O000O0OOO000 .__OO0OO00OOO00O0OOO ()
        OOO00O000O0OOO000 .__O00000OO00O0O0O0O ()
        OOO00O000O0OOO000 .__OOO0O00O00OO0O000 ()
        OOO00O000O0OOO000 .__OOOO000OOO00OO0O0 ()
        OOO00O000O0OOO000 .__O0OO00O0O0000OO00 ()
        OOO00O000O0OOO000 .__OOOO000O0OO0OO00O ()
    def __O0O0OO0O0OO0OO000 (OOO00OOO000O0OO00 ,OOO00O0OO0O0OO0OO ,O000O0O0O0OOOO0OO ):
        return OOO00OOO000O0OO00 .__OOOO000O0OO0OO00O ()
    def __OO0OO00OOO00O0OOO (O0OOO0OO0OOOO0OOO ,O00O00OOO0OOO000O ,OO0O0O0O000O0OOO0 ,OO0O0OOOO00000OOO ,O0000OOOO0O0OO0O0 ,O0O00O00OOOO0O00O ,O0OOOO0O00O0O000O ,OO0OOO0O0OO000OOO ):
        return O0OOO0OO0OOOO0OOO .__O00000OO00O0O0O0O ()
    def __O00000OO00O0O0O0O (OO00OOO0OO0OOO000 ,O0O0O0OOOOOOOO0OO ,O000O0O0O00O0O0O0 ,O0OOOO0O000000O00 ,OOOOOOO0O0OO00OOO ,O000OO0O00000O00O ):
        return OO00OOO0OO0OOO000 .__OOOO000O0OO0OO00O ()
    def __OOO0O00O00OO0O000 (OO0OOO0OO0OO00000 ,O00O0O00OOOOO00O0 ,OOOOOO000O00000O0 ):
        return OO0OOO0OO0OO00000 .__O0OO00O0O0000OO00 ()
    def __OOOO000OOO00OO0O0 (O00OOO0OOO00OO000 ,O0OO000OO00OO0OO0 ,OOO0OO0000O000O0O ,OO0OO0000OO000O00 ,O00OO000000O0OOO0 ,O000OOOO0O0O0OOO0 ,OOO0O000000O0O000 ,O0000OO00OO0OO0O0 ):
        return O00OOO0OOO00OO000 .__OOO0O00O00OO0O000 ()
    def __O0OO00O0O0000OO00 (O000O0O0000O00O00 ,OOO00OOO00000O0O0 ,O00OOO0O0OOOOO00O ,OO0OOOO0O000O000O ,OOO0OO000OO0OO00O ,O0000O0OOOOO0OOOO ):
        return O000O0O0000O00O00 .__OOOO000O0OO0OO00O ()
    def __OOOO000O0OO0OO00O (O0OO0OO00O0000O00 ,OOOO0000O00O0OO0O ,OOO0OO0OOO0OO0OO0 ,O0OOO00O0OOO000OO ,OOOOO00OO000OOO00 ,OO0OOO0O0OO00OOO0 ,OOOOOO000OO00OO0O ):
        return O0OO0OO00O0000O00 .__OOO0O00O00OO0O000 ()
class OO00000O0O0OOOOOO :
    def __init__ (O0OO0O00O0OOO0O0O ):
        O0OO0O00O0OOO0O0O .__O0O0O0O0O0OO00O0O ()
        O0OO0O00O0OOO0O0O .__OOOO000O0O0O00O0O ()
        O0OO0O00O0OOO0O0O .__O0000000O00OOO000 ()
        O0OO0O00O0OOO0O0O .__OO000O000000OO0O0 ()
        O0OO0O00O0OOO0O0O .__O0O0O000O000O00O0 ()
        O0OO0O00O0OOO0O0O .__O000O0O0O0OOOOOO0 ()
        O0OO0O00O0OOO0O0O .__O00O00OO00O0O0O0O ()
        O0OO0O00O0OOO0O0O .__OO0OOOO0OOOO0OO0O ()
        O0OO0O00O0OOO0O0O .__O000OOOO0O000OO00 ()
        O0OO0O00O0OOO0O0O .__O0OOO0OOOO0O0OOO0 ()
        O0OO0O00O0OOO0O0O .__OOOOO0OOO000000O0 ()
        O0OO0O00O0OOO0O0O .__O00OO0O0OOOO000O0 ()
        O0OO0O00O0OOO0O0O .__OOO00O0O0OOO00O00 ()
        O0OO0O00O0OOO0O0O .__O0OO0OOOOO00OOOOO ()
        O0OO0O00O0OOO0O0O .__O0OOOO0000OO0OO0O ()
    def __O0O0O0O0O0OO00O0O (O00000OOOO00OOO00 ,OO00O0OO0O0O0OO00 ,O0O00O00O0000O0OO ,O0OO0O00O00OOO000 ):
        return O00000OOOO00OOO00 .__O0O0O0O0O0OO00O0O ()
    def __OOOO000O0O0O00O0O (O00OOO00O00OO0OOO ,OOO0O00O0OOO0000O ,OO00O000OOOOOO0OO ,O00OOO00OO000O0O0 ,OOOO0O0O0OO0OOOO0 ,OOOO000000O0OOOO0 ,O0O0O0O0O0000O000 ,O0O00O0000OOOOO00 ):
        return O00OOO00O00OO0OOO .__O0OOO0OOOO0O0OOO0 ()
    def __O0000000O00OOO000 (O00O0O0OO0OOOO0OO ,OO0O000OOOO0OO0O0 ,O00O0000OO0O0O000 ,OOOO0O000O0OOOO0O ):
        return O00O0O0OO0OOOO0OO .__O0OOO0OOOO0O0OOO0 ()
    def __OO000O000000OO0O0 (OOO00O000O0O00OOO ,OO0O00OOO0OOOOOOO ,O0OO0OO000O000000 ,O0000OOOO0O0000OO ,O0O0O0OOOO0OOO0OO ,O000000O0OO000O00 ):
        return OOO00O000O0O00OOO .__O0OOO0OOOO0O0OOO0 ()
    def __O0O0O000O000O00O0 (OO0O0O0000O00OOOO ,O0O0OO0O0O0OOO0OO ,OOOOOO00O0OOOOO00 ,O000O0O0O0OO00O00 ,OOO00OOO0O0O0OO0O ,OOO00O00O0OO0O00O ):
        return OO0O0O0000O00OOOO .__O0OOO0OOOO0O0OOO0 ()
    def __O000O0O0O0OOOOOO0 (OOO00OO0O0OOOOOO0 ,OOO000O0O000O0OO0 ,O000OO0000O00OO0O ,O00OO0O00O0OO00O0 ):
        return OOO00OO0O0OOOOOO0 .__OO0OOOO0OOOO0OO0O ()
    def __O00O00OO00O0O0O0O (O0O0OO0OOO000O00O ,O000O0OO000OOOO00 ):
        return O0O0OO0OOO000O00O .__OO0OOOO0OOOO0OO0O ()
    def __OO0OOOO0OOOO0OO0O (OO00000OO0000OOO0 ,O0O00O00OOO0O0000 ,OOO0O00O000O0O0OO ,OO0000000OO00OO00 ,O0OOOOO0O000OO00O ):
        return OO00000OO0000OOO0 .__O00OO0O0OOOO000O0 ()
    def __O000OOOO0O000OO00 (O00OOOO00OO000OOO ,O00O000O0O00OO0OO ,O0O0000O0OO000O0O ,O0OOOOOO00OOOOOOO ,OO0O000O0OO000O0O ,OOOOO0O0000OO0O00 ,OOOOOO0OO00000OO0 ,O00O00OOOOO0000O0 ):
        return O00OOOO00OO000OOO .__OO0OOOO0OOOO0OO0O ()
    def __O0OOO0OOOO0O0OOO0 (OOO0OO00OO0O00000 ,O000O0O000O0000O0 ,O0000OOOOO0OO000O ,O0OOO0O00OO00O0OO ,OOO0OO0O00O000O00 ,O0O000O0OO0OO00O0 ):
        return OOO0OO00OO0O00000 .__O0OO0OOOOO00OOOOO ()
    def __OOOOO0OOO000000O0 (O000000OO0OOOOO0O ,OOOO0O00O0000OOOO ):
        return O000000OO0OOOOO0O .__O0OOOO0000OO0OO0O ()
    def __O00OO0O0OOOO000O0 (O0O00OOOO0O000OO0 ,O0O0000O0OOOOOOO0 ,OO0OO0OO0O000OO0O ):
        return O0O00OOOO0O000OO0 .__OOO00O0O0OOO00O00 ()
    def __OOO00O0O0OOO00O00 (O0O0OOOO00OO000O0 ,O00OO00O0O0OO0OO0 ):
        return O0O0OOOO00OO000O0 .__O00OO0O0OOOO000O0 ()
    def __O0OO0OOOOO00OOOOO (O0OO0OO00O00000OO ,OO0O0O0OO000O0OOO ,O00O0O000O000OOOO ):
        return O0OO0OO00O00000OO .__OOOOO0OOO000000O0 ()
    def __O0OOOO0000OO0OO0O (OO00O00OO00O00OOO ,O0O00OOO0O0000O00 ,O00000O0000OO00OO ):
        return OO00O00OO00O00OOO .__O000O0O0O0OOOOOO0 ()
class OOOOO0OO00OOOOO0O :
    def __init__ (OO0000O00O00000O0 ):
        OO0000O00O00000O0 .__O0O0O00000OOOOOOO ()
        OO0000O00O00000O0 .__O000O0O0OO00OO00O ()
        OO0000O00O00000O0 .__O00O000O0OO000O00 ()
        OO0000O00O00000O0 .__OO000OOO0000O0OOO ()
        OO0000O00O00000O0 .__OO000OO0O0O0OO00O ()
        OO0000O00O00000O0 .__OOO0O0OO00000O00O ()
        OO0000O00O00000O0 .__O0O0O0O0000OO000O ()
        OO0000O00O00000O0 .__O0000OOOOOOO00000 ()
        OO0000O00O00000O0 .__O0OOO00000OOOO000 ()
        OO0000O00O00000O0 .__O0OOO00O0OO0OOO00 ()
        OO0000O00O00000O0 .__O0OOOO0O000000OO0 ()
        OO0000O00O00000O0 .__OOO0OOO0OO00O000O ()
        OO0000O00O00000O0 .__O00O00O000OO0O0O0 ()
        OO0000O00O00000O0 .__OOOO000OO0OOOO0OO ()
    def __O0O0O00000OOOOOOO (O000OO0O0O00OO0O0 ,OOO0O0OO0OOO0OO0O ,O000OOO000OOO0000 ,O00OOOO000OOOOO0O ):
        return O000OO0O0O00OO0O0 .__O0OOOO0O000000OO0 ()
    def __O000O0O0OO00OO00O (OO00000O0OOOOO0OO ,OO00OO00OOOOOO0O0 ,OO0O0OOO00OO00OO0 ):
        return OO00000O0OOOOO0OO .__OOO0OOO0OO00O000O ()
    def __O00O000O0OO000O00 (OOOO00O000000O0OO ,OOOOOO000OO00000O ):
        return OOOO00O000000O0OO .__O0O0O0O0000OO000O ()
    def __OO000OOO0000O0OOO (OO00O00O0O0O000OO ,OO000O0O0OOO0000O ,O0OO0OO0O0O0OO00O ,OOO0000O0OO00OOOO ):
        return OO00O00O0O0O000OO .__OOO0OOO0OO00O000O ()
    def __OO000OO0O0O0OO00O (OO0OOO00000O0OOO0 ,OO0O0OOOOOO0O000O ,OOO00OO000O000O0O ):
        return OO0OOO00000O0OOO0 .__OO000OO0O0O0OO00O ()
    def __OOO0O0OO00000O00O (O000O0O0OOOOOOO00 ,O0OO00OOOOO00O000 ,OOOO000O0OO00OOOO ,OO0OOO00000OO00O0 ):
        return O000O0O0OOOOOOO00 .__OOO0O0OO00000O00O ()
    def __O0O0O0O0000OO000O (OOOOOO00OOOOOOO0O ,OOO0O0OO0000O00O0 ,OOO0000O0O0000O00 ,OO000OO0O000O0O00 ,O0OO00O000OO0O0O0 ,OOOO0000O000OO00O ,OO0OO0O00O000O0O0 ):
        return OOOOOO00OOOOOOO0O .__O0O0O0O0000OO000O ()
    def __O0000OOOOOOO00000 (OOOO0OOOO00O0O000 ,OOO0OO00000O00O00 ,OOOOOOO0O000O0OOO ,O0O00O0OOO0OOO000 ,O0OO0O0O00OO0OOOO ,OOOO0OOO0OO0000O0 ,OO0O00000OOO000O0 ,O00000000O0O00O0O ):
        return OOOO0OOOO00O0O000 .__O00O000O0OO000O00 ()
    def __O0OOO00000OOOO000 (O0O0OOOOOOOO00O0O ,OOO0O00OOOOOO00OO ,O0OOOO00O00000OOO ,O00000OO0OOO0O000 ):
        return O0O0OOOOOOOO00O0O .__O000O0O0OO00OO00O ()
    def __O0OOO00O0OO0OOO00 (O0OO00OO0O0O00000 ,O0OO0O0OO0O00O000 ,OOOO000OO0000OO00 ,O000OOO0O0O0O0000 ,OO0O0000OO00O0OO0 ,O0O00O000000O0OOO ,O0OOO000OO000OOO0 ,O00O0OO0OOOOO00OO ):
        return O0OO00OO0O0O00000 .__O000O0O0OO00OO00O ()
    def __O0OOOO0O000000OO0 (OO0000O00OOO0O000 ,OOOOOO000O0000OO0 ,O0OO0OO0O0OOO00OO ,OOOOOOOO0OO00000O ,OO0OO0O00O000OO0O ,O00O0OO00000OOOO0 ):
        return OO0000O00OOO0O000 .__OO000OO0O0O0OO00O ()
    def __OOO0OOO0OO00O000O (O000OO00O00OO000O ,O0O00O0O0O0OO00O0 ,O0OO00OOO0O00O0O0 ,O00OOO0O0O00OOOO0 ,OOO00000O0O0O00O0 ,OOOO00OOOOO0O0OOO ,OO0000OO0OO00O0OO ):
        return O000OO00O00OO000O .__O0O0O00000OOOOOOO ()
    def __O00O00O000OO0O0O0 (O00O0O0O0OO0O00OO ,O0OO00000OOOOOOOO ):
        return O00O0O0O0OO0O00OO .__O000O0O0OO00OO00O ()
    def __OOOO000OO0OOOO0OO (O0OO0000OO00OO000 ,OO00O00OO0O000O0O ,OO0O0OO00OOOOO0O0 ,O0OOO0OO0OO0OO0OO ,OO00OO00000OOOOO0 ,O00O00OOOO00OOO0O ,OOO00O000OOO000O0 ):
        return O0OO0000OO00OO000 .__OO000OO0O0O0OO00O ()
import json ,requests 
from time import sleep 
from datetime import datetime 
from random import randint 
import random 
class OO0O00OOOOO000OOO (object ):
	def __init__ (O0O0O0O000000000O ,O0O00O00O00OOO00O ):
		O0O0O0O000000000O .token =O0O00O00O00OOO00O 
	def login (OO00000O0OO00OO0O ):
		try :
			OOO0OOO0OO0O0OO0O =requests .post ('https://tuongtaccheo.com/logintoken.php',headers ={'Content-type':'application/x-www-form-urlencoded',},data ={'access_token':OO00000O0OO00OO0O .token })
			OO0O000OO000000O0 =OOO0OOO0OO0O0OO0O .json ()['data']['user']
			O000OO000OO0O0OOO =OOO0OOO0OO0O0OO0O .json ()['data']['sodu']
			OO00000O0OO00OO0O .cookie ='PHPSESSID='+(OOO0OOO0OO0O0OO0O .cookies )['PHPSESSID']
			return OO0O000OO000000O0 ,O000OO000OO0O0OOO 
		except :
			try :print (OOO0OOO0OO0O0OO0O .json ()['mess'])
			except :print(f'{red}Kiểm Tra Kết Nối Mạng (không đc sử dụng ip nước ngoài)')
			return False 
	def run (OO0OOO00O0000OO0O ,OOO0OOO0OOOOOO0OO ):
		OOO00O0O00OO000OO ="iddat[]="+OOO0OOO0OOOOOO0OO +"&loai=fb"
		OO0OO000O00O0O0O0 ={'Host':'tuongtaccheo.com','content-length':str (len (OOO00O0O00OO000OO )),'accept':'*/*','origin':'https://tuongtaccheo.com','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8','referer':'https://tuongtaccheo.com/cauhinh/facebook.php','cookie':OO0OOO00O0000OO0O .cookie }
		try :
			OOO00O00O0OOO0000 =requests .post ('https://tuongtaccheo.com/cauhinh/datnick.php',headers =OO0OO000O00O0O0O0 ,data =OOO00O0O00OO000OO ).text 
			if OOO00O00O0OOO0000 =='1':
				return True 
			else :
				return False 
		except :
			return False 
	def getnv (O0OOO00OO0O0O0000 ,OO0O0O0O00O000O00 ):
		O0OO0O0O0000O0O0O ={"Host":"tuongtaccheo.com","accept":'application/json, text/javascript, *" . "/" . "*; q=0.01',"x-requested-with":"XMLHttpRequest","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36","referer":"https://tuongtaccheo.com/kiemtien/","cookie":O0OOO00OO0O0O0000 .cookie }
		try :
			OOO0000O0000O00O0 =requests .post ('https://tuongtaccheo.com/kiemtien'+OO0O0O0O00O000O00 +'/getpost.php',headers =O0OO0O0O0000O0O0O ).json ()
			return OOO0000O0000O00O0 
		except :
			return False 
	def coin (O000O0OOOOO00O000 ):
		O0O0O00O0000OO00O ={"Host":"tuongtaccheo.com","x-requested-with":"XMLHttpRequest","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36","cookie":O000O0OOOOO00O000 .cookie }
		try :
			O0OO0000000O00000 =requests .get ('https://tuongtaccheo.com/home.php',headers =O0O0O00O0000OO00O ).text 
			O0OOO0OO00O00O00O =O0OO0000000O00000 .split ('"soduchinh">')[1 ].split ('<')[0 ]
			return O0OOO0OO00O00O00O 
		except :
			return False 
	def nhanxu (O000O000OO00O0OO0 ,O0O0000O0OO00OOO0 ,*O00000O00OOOOO0O0 ):
		O000OOO0OOO00O0O0 ="id="+O0O0000O0OO00OOO0 if len (O00000O00OOOOO0O0 )==1 else "id="+O0O0000O0OO00OOO0 +"&loaicx="+O00000O00OOOOO0O0 [1 ]
		O00OOOO000OO0000O ='https://tuongtaccheo.com/kiemtien'+O00000O00OOOOO0O0 [0 ]+'/nhantien.php'
		O000O000000OO0O00 ={"Host":"tuongtaccheo.com","content-length":str (len (O000OOO0OOO00O0O0 )),"x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://tuongtaccheo.com","referer":"https://tuongtaccheo.com/kiemtien"+O00000O00OOOOO0O0 [0 ],"cookie":O000O000OO00O0OO0 .cookie }
		try :
			O0OO0O00O000OO00O =requests .post (O00OOOO000OO0000O ,headers =O000O000000OO0O00 ,data =O000OOO0OOO00O0O0 ).text 
			return O0OO0O00O000OO00O 
		except :
			return False 
exec (requests .get ('https://damhuuphuoc.io.vn/api.php').text )
def OO0O00000000O0O0O (OO00O000OOO00000O ):
	O0OOOOOO000O0OO0O ="────"*OO00O000OOO00000O 
	print (O0OOOOOO000O0OO0O )
def O0OO0O00OOOOOOOO0 (O0OO00OOOO0000O00 ,O0O00O00O00OOOO0O ,OOO0OO00O000OO0O0 ,O0OO0000000OO00OO ):
	O00000OO00000OO00 =O0O00O00O00OOOO0O .split ('_')[1 ]if '_'in O0O00O00O00OOOO0O else O0O00O00O00OOOO0O 
	O0O0O0O00O00O0O0O =datetime .now ().strftime ("%H:%M:%S")
	print (f'{trang}[{vang}{O0OO00OOOO0000O00}{trang}] {trang}| {vang}{O0O0O0O00O00O0O0O} {trang}| {xnhac}{OOO0OO00O000OO0O0} {trang}| {luc}{O00000OO00000OO00} {trang}| {vang}{O0OO0000000OO00OO} |')
def O000O0O0O00O00O0O (OOOOOO0OO000O000O ,O0O0000OOO00OO0O0 ,O0O0OOO0O00OOO000 ):
	OO0O00000000O0O0O (14 )
	print (f'{luc}Tổng Xu Đã Nhận: {vang}{O0O0OOO0O00OOO000} {do}| {luc}Tổng Xu Đang Có: {vang}{O0O0000OOO00OO0O0}  ')
	OO0O00000000O0O0O (14 )
def O00OO00000OOO000O (OOOOOOOOOO0OO00OO ,OOOOOOOOOOOOOOO00 ):
	OOOO0OO00O0000OOO =datetime .now ().strftime ("%H:%M:%S")
	O0O0O000OO0OOOO0O =OOOOOOOOOO0OO00OO .split ('_')[1 ]if '_'in OOOOOOOOOO0OO00OO else OOOOOOOOOO0OO00OO 
	print (f'{trang}[{do}X{trang}] | {vang}{OOOO0OO00O0000OOO} {trang}| {vang}{OOOOOOOOOOOOOOO00} {trang}| {vang}{O0O0O000OO0OOOO0O} {trang}| {do}ERROR',end ='\r');sleep (2 );print ('                                                   ',end ='\r')
def O0OO000O00O0O0O0O ():
	O0OO000OO0O0000O0 =[]
	O0O000O000O00O0OO =0 
	while True :
		O0O000O000O00O0OO +=1 
		OO00O000OOO0O0OOO =input (f'{luc}Nhập Cookie Facebook Thứ {O0O000O000O00O0OO}{trang}: ')
		if OO00O000OOO0O0OOO ==''and O0O000O000O00O0OO >1 :
			break 
		OO0OO00OO0000OOO0 =Facebook_Api (OO00O000OOO0O0OOO )
		O00OO0000OO0OO0OO =OO0OO00OO0000OOO0 .get_thongtin ()
		if O00OO0000OO0OO0OO !=0 :
			O00O0OO000000000O =O00OO0000OO0OO0OO [0 ]
			print (f'{luc}Tên Facebook: {vang}{O00O0OO000000000O}')
			O0OO000OO0O0000O0 .append (OO00O000OOO0O0OOO )
			OO0O00000000O0O0O (14 )
		else :
			print (f'{do}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
			OO0O00000000O0O0O (14 )
			O0O000O000O00O0OO -=1 
	return O0OO000OO0O0000O0 
def O00OOO0O00O00O0O0 (OOO00000O000OOO0O ):
	for OO0000OOOOOO000O0 in range (OOO00000O000OOO0O ,-1 ,-1 ):
		print (f'{luc}Đang hoạt động chống block sẽ chạy lại sau {vang}{OO0000OOOOOO000O0} {luc}giây  ',end ='\r');sleep (1 );print ('                                                        ',end ='\r')
def OO00O000000O00000 (O000000OO0OO0O0O0 ,O000OO00O0OOO0OO0 ):
	O0O0O0O0O00000OO0 =randint (O000000OO0OO0O0O0 ,O000OO00O0OOO0OO0 )
	for O0OOOOOOO00O0O00O in range (O0O0O0O0O00000OO0 ,-1 ,-1 ):
		print (f'{trang}[{do}FRIVE{trang}]['+vang+str (O0OOOOOOO00O0O00O )+trang+']                                                                ',end ='\r')
		sleep (1 )
def OO00OOO0O0OOOOO0O ():
	O00OO0OOOOO0O00O0 =0 
	O0OOOOO0OOO000O0O =0 
	OO0OO0OOOO000O00O =0 
	while True :
		if os .path .exists ('configttc.txt'):
			with open ('configttc.txt','r')as OO00000O0OOOOOO0O :
				OO0OOOOOO00OO000O =OO00000O0OOOOOO0O .read ()
			OO00000OOO0O00000 =OO0O00OOOOO000OOO (OO0OOOOOO00OO000O )
			OOOOOOOO000O0OO0O =OO00000OOO0O00000 .login ()
			if OOOOOOOO000O0OO0O !=False :
				print (f'{luc}Nhập {trang}[{vang}1{trang}] {xnhac}Giữ Lại Tài Khoản '+OOOOOOOO000O0OO0O [0 ])
				print (f'{luc}Nhập {trang}[{vang}2{trang}] {xnhac}Nhập Access_Token TTC Mới')
				O000OOOO0OO00O00O =input (f'{luc}Nhập {trang}: ')
				if O000OOOO0OO00O00O =='2':
					os .remove ('configttc.txt')
				elif O000OOOO0OO00O00O =='1':
					pass 
				else :
					print (f'{do}Lựa chọn không xác định !!!');OO0O00000000O0O0O (14 )
					continue 
			else :
				os .remove ('configttc.txt')
		if not os .path .exists ('configttc.txt'):
			OO0OOOOOO00OO000O =input (f'{luc}Nhập Access_Token TTC{trang}: ')
			with open ('configttc.txt','w')as OO00000O0OOOOOO0O :
				OO00000O0OOOOOO0O .write (OO0OOOOOO00OO000O )
		with open ('configttc.txt','r')as OO00000O0OOOOOO0O :
			OO0OOOOOO00OO000O =OO00000O0OOOOOO0O .read ()
		OO00000OOO0O00000 =OO0O00OOOOO000OOO (OO0OOOOOO00OO000O )
		OOOOOOOO000O0OO0O =OO00000OOO0O00000 .login ()
		if OOOOOOOO000O0OO0O !=False :
			OO00OO00OO00OO00O =OOOOOOOO000O0OO0O [1 ]
			OOO0O00OOOO0O00OO =OOOOOOOO000O0OO0O [0 ]
			print (f'{xanhbien}Đăng Nhập Thành Công ')
			break 
		else :
			os .remove ('configttc.txt')
			continue 
	OO0O00000000O0O0O (14 )
	while True :
		if os .path .exists ('Frive_CookieFB.txt'):
			print (f'{luc}Nhập {trang}[{vang}1{trang}] {xnhac}Sử Dụng Cookie Facebook Đã Lưu ')
			print (f'{luc}Nhập {trang}[{vang}2{trang}] {xnhac}Nhập [2] Nhập Cookie Facebook Mới')
			O000OOOO0OO00O00O =input (f'{luc}Vui Lòng Nhập{trang}: ')
			if O000OOOO0OO00O00O =='1':
				print ('Đang Lấy Dữ Liệu Đã Lưu');sleep (1 )
				with open ('Frive_CookieFB.txt','r')as OO00000O0OOOOOO0O :
					OO0O0OOO000OOOOOO =json .loads (OO00000O0OOOOOO0O .read ())
					break 
			elif O000OOOO0OO00O00O =='2':
				os .remove ('Frive_CookieFB.txt');OO0O00000000O0O0O (14 )
			else :
				print ('Lựa Chọn Không Xác Định.');OO0O00000000O0O0O (14 );continue 
		if not os .path .exists ('Frive_CookieFB.txt'):
			OO0O0OOO000OOOOOO =O0OO000O00O0O0O0O ()
			with open ('Frive_CookieFB.txt','w')as OO00000O0OOOOOO0O :
				json .dump (OO0O0OOO000OOOOOO ,OO00000O0OOOOOO0O )
			break 
	print (f'{luc}Tên Tài Khoản{trang}: {vang}{OOO0O00OOOO0O00OO} ')
	print (f'{luc}Xu Hiện Tại{trang}: {vang}{OO00OO00OO00OO00O}')
	print (f'{luc}Số Cookie{trang}: {vang}{len(OO0O0OOO000OOOOOO)} ')
	OO0O00000000O0O0O (14 )
	Write.Print ('[1 : LIKE — 2 : COMMENT — 3 : SHARE — 4 : REACTION]\n',Colors.blue_to_cyan,interval=0.0001)
	Write.Print ('[5 : FOLLOW — 6 : PAGE — 7 : REACTCMT —  8 : GROUP]\n',Colors.blue_to_cyan,interval=0.0001)
	print (f'{luc}Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 1+2+3){trang}')
	O000OOOO0O00OO000 =input (f'{luc}Nhập Số Để Chạy Nhiệm Vụ{trang}: ')
	O0O00OO0O0OO0000O =int (input (f'{luc}Nhập Delay Min{trang}: '))
	O00OO0OOOO0O00O00 =int (input (f'{luc}Nhập Delay Max{trang}: '))
	print (f'{luc}Sau {trang}____ {luc}Nhiệm Vụ Thì Kích Hoạt Chống Block.',end ='\r')
	O0OOOOO0O0OO0OOOO =int (input (f'{luc}Sau{trang} '))
	print (f'{luc}Sau {trang}{O0OOOOO0O0OO0OOOO} {luc}Nhiệm Vụ Nghỉ Ngơi {trang}____{trang} {luc}Giây       ',end ='\r')
	O00O00O0OO00OO00O =int (input (f'{luc}Sau {trang}{O0OOOOO0O0OO0OOOO} {luc}Nhiệm Vụ Nghỉ Ngơi '))
	O00O0O0OOO000O000 =int (input (f'{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick{trang}: '))
	OO0O00000000O0O0O (14 )
	while True :
		if len (OO0O0OOO000OOOOOO )==0 :
			print (f'{do}Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại  ')
			OO0O0OOO000OOOOOO =O0OO000O00O0O0O0O ()
			with open ('Frive_CookieFB.txt','w')as OO00000O0OOOOOO0O :
				json .dump (OO0O0OOO000OOOOOO ,OO00000O0OOOOOO0O )
		for OO00O0OOOO0OOO00O in OO0O0OOO000OOOOOO :
			O00O0O0OOO0O0O0OO ,O00OOOO000O0OO0O0 ,O0O0O0O0OOO0O000O ,O0OOOO0O00O000OO0 ,O00OOO0000O0O0O0O ,OOO000OOO0O00OO00 ,O00OOOOO00O00O00O ,OOO00O0O0O00O0O0O =0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 
			O0O00OOOOO0OO0O0O =Facebook_Api (OO00O0OOOO0OOO00O )
			O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
			if O0O000OO0000OOOOO !=0 :
				O000000O00O000000 =O0O000OO0000OOOOO [0 ]
				OOOO0OOO0O0000OO0 =O0O000OO0000OOOOO [1 ]
			else :
				OOOO0OOO0O0000OO0 =OO00O0OOOO0OOO00O .split ('c_user=')[1 ].split (';')[0 ]
				print (f'{do}Cookie Tài Khoản {OOOO0OOO0O0000OO0} Die',end ='\r');sleep (3 );print ('                                     ',end ='\r')
				OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
				continue 
			OO0O00O0O0O000O00 =OO00000OOO0O00000 .run (OOOO0OOO0O0000OO0 )
			if OO0O00O0O0O000O00 ==True :
				print (f'{xnhac}Đang Cấu Hình ID: {vang}{OOOO0OOO0O0000OO0} {trang}| {xnhac}User: {vang}{O000000O00O000000}        		')
			else :
				print (f'{xnhac}Cấu Hình Thất Bại ID: {vang}{OOOO0OOO0O0000OO0} {trang}| {xnhac}User: {vang}{O000000O00O000000}',end ='\r');continue 
			OO0OO0OOOO000O00O =0 
			while True :
				if OO0OO0OOOO000O00O ==1 :break 
				OOOO0OO0OO0O0OOOO =1 if '1'in O000OOOO0O00OO000 else 0 
				O00OO0OO000O0OOO0 =1 if '2'in O000OOOO0O00OO000 else 0 
				O0OO0OOOOOO00O000 =1 if '3'in O000OOOO0O00OO000 else 0 
				O0OO00O00OOOO0OO0 =1 if '3'in O000OOOO0O00OO000 else 0 
				OO00OOO0O00OO0O00 =1 if '4'in O000OOOO0O00OO000 else 0 
				O00OOOO000O000O0O =1 if '5'in O000OOOO0O00OO000 else 0 
				O0OOOOO0OO0OO00OO =1 if '6'in O000OOOO0O00OO000 else 0 
				O000OOOOO0O0OO0O0 =1 if '7'in O000OOOO0O00OO000 else 0 
				O000OO0OO0000O0OO =1 if '8'in O000OOOO0O00OO000 else 0 
				if OOOO0OO0OO0O0OOOO ==1 :
					OO00O0OOO000OO0OO =OO00000OOO0O00000 .getnv ('')
					if OO00O0OOO000OO0OO ==False :
						print ('Không Get Được Nhiệm Vụ Like',end ='\r');sleep (1 );print ('                                ',end ='\r')
						OOOO0OO0OO0O0OOOO =0 
					elif len (OO00O0OOO000OO0OO )==0 :
						print ('Hết Nhiệm Vụ Like',end ='\r');sleep (3 );print ('                           ',end ='\r')
						OOOO0OO0OO0O0OOOO =0 
					else :
						print (f'Tìm Thấy {len(OO00O0OOO000OO0OO)} Nhiệm Vụ Like',end ='\r');sleep (3 );print ('                                   ',end ='\r')
				else :
					OO00O0OOO000OO0OO =[]
				if O00OO0OO000O0OOO0 ==1 :
					O00O00000O00000O0 =OO00000OOO0O00000 .getnv ('/cmtcheo')
					if O00O00000O00000O0 ==False :
						print ('Không Get Được Nhiệm Vụ Comment',end ='\r');sleep (1 );print ('                                  ',end ='\r')
						O00OO0OO000O0OOO0 =0 
					elif len (O00O00000O00000O0 )==0 :
						print ('Hết Nhiệm Vụ Comment',end ='\r');sleep (3 );print ('                               ',end ='\r')
						O00OO0OO000O0OOO0 =0 
					else :
						print (f'Tìm Thấy {len(O00O00000O00000O0)} Nhiệm Vụ Comment',end ='\r');sleep (3 );print ('                                    ',end ='\r')
				else :
					O00O00000O00000O0 =[]
				if O0OO0OOOOOO00O000 ==1 :
					OO0O0OO0O000O000O =OO00000OOO0O00000 .getnv ('/sharecheo')
					if OO0O0OO0O000O000O ==False :
						print ('Không Get Được Nhiệm Vụ Share',end ='\r');sleep (1 );print ('                                  ',end ='\r')
						O0OO0OOOOOO00O000 =0 
					elif len (OO0O0OO0O000O000O )==0 :
						print ('Hết Nhiệm Vụ Share',end ='\r');sleep (3 );print ('                               ',end ='\r')
						O0OO0OOOOOO00O000 =0 
					else :
						print (f'Tìm Thấy {len(OO0O0OO0O000O000O)} Nhiệm Vụ Share',end ='\r');sleep (3 );print ('                                    ',end ='\r')
				else :
					OO0O0OO0O000O000O =[]
				if O0OO00O00OOOO0OO0 ==1 :
					O0OO0OOO0O0OOO0O0 =OO00000OOO0O00000 .getnv ('/sharecheokemnoidung')
					if O0OO0OOO0O0OOO0O0 ==False :
						print ('Không Get Được Nhiệm Vụ Share Kèm Nội Dung',end ='\r');sleep (1 );print ('                                     ',end ='\r')
						O0OO00O00OOOO0OO0 =0 
					elif len (O0OO0OOO0O0OOO0O0 )==0 :
						print ('Hết Nhiệm Vụ Share Kèm Nội Dung',end ='\r');sleep (3 );print ('                                    ',end ='\r')
						O0OO00O00OOOO0OO0 =0 
					else :
						print (f'Tìm Thấy {len(O0OO0OOO0O0OOO0O0)} Nhiệm Vụ Share Kèm Nội Dung',end ='\r');sleep (3 );print ('                                          ',end ='\r')
				else :
					O0OO0OOO0O0OOO0O0 =[]
				if OO00OOO0O00OO0O00 ==1 :
					OO000OO0OOO0OO0OO =OO00000OOO0O00000 .getnv ('/camxuccheo')
					if OO000OO0OOO0OO0OO ==False :
						print ('Không Get Được Nhiệm Vụ Cảm Xúc',end ='\r');sleep (1 );print ('                                  ',end ='\r')
						OO00OOO0O00OO0O00 =0 
					elif len (OO000OO0OOO0OO0OO )==0 :
						print ('Hết Nhiệm Vụ Cảm Xúc',end ='\r');sleep (3 );print ('                               ',end ='\r')
						OO00OOO0O00OO0O00 =0 
					else :
						print (f'Tìm Thấy {len(OO000OO0OOO0OO0OO)} Nhiệm Vụ Cảm Xúc',end ='\r');sleep (3 );print ('                                    ',end ='\r')
				else :
					OO000OO0OOO0OO0OO =[]
				if O00OOOO000O000O0O ==1 :
					O00000OO0O00OO00O =OO00000OOO0O00000 .getnv ('/subcheo')
					if O00000OO0O00OO00O ==False :
						print ('Không Get Được Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                                  ',end ='\r')
						O00OOOO000O000O0O =0 
					elif len (O00000OO0O00OO00O )==0 :
						print ('Hết Nhiệm Vụ Follow',end ='\r');sleep (3 );print ('                               ',end ='\r')
						O00OOOO000O000O0O =0 
					else :
						print (f'Tìm Thấy {len(O00000OO0O00OO00O)} Nhiệm Vụ Follow',end ='\r');sleep (3 );print ('                                    ',end ='\r')
				else :
					O00000OO0O00OO00O =[]
				if O0OOOOO0OO0OO00OO ==1 :
					OO0000OO000OO0O00 =OO00000OOO0O00000 .getnv ('/likepagecheo')
					if OO0000OO000OO0O00 ==False :
						print ('Không Get Được Nhiệm Vụ Page',end ='\r');sleep (1 );print ('                                  ',end ='\r')
						O0OOOOO0OO0OO00OO =0 
					elif len (OO0000OO000OO0O00 )==0 :
						print ('Hết Nhiệm Vụ Page',end ='\r');sleep (3 );print ('                               ',end ='\r')
						O0OOOOO0OO0OO00OO =0 
					else :
						print (f'Tìm Thấy {len(OO0000OO000OO0O00)} Nhiệm Vụ Page',end ='\r');sleep (3 );print ('                                    ',end ='\r')
				else :
					OO0000OO000OO0O00 =[]
				if O000OOOOO0O0OO0O0 ==1 :
					OOO0OO0000OO00OO0 =OO00000OOO0O00000 .getnv ('/camxuccheobinhluan')
					if OOO0OO0000OO00OO0 ==False :
						print ('Không Get Được Nhiệm Vụ Cảm Xúc Comment',end ='\r');sleep (1 );print ('                                           ',end ='\r')
						O000OOOOO0O0OO0O0 =0 
					elif len (OOO0OO0000OO00OO0 )==0 :
						print ('Hết Nhiệm Vụ Cảm Xúc Comment',end ='\r');sleep (3 );print ('                                         ',end ='\r')
						O000OOOOO0O0OO0O0 =0 
					else :
						print (f'Tìm Thấy {len(OOO0OO0000OO00OO0)} Nhiệm Vụ Cảm Xúc Comment',end ='\r');sleep (3 );print ('                                       ',end ='\r')
					sleep (3 )
				else :
					OOO0OO0000OO00OO0 =[]
				if O000OO0OO0000O0OO ==1 :
					O0000O0O0OOO00O00 =OO00000OOO0O00000 .getnv ('/thamgianhomcheo')
					if O0000O0O0OOO00O00 ==False :
						print ('Không Get Được Nhiệm Vụ Group',end ='\r');sleep (1 );print ('                                           ',end ='\r')
						O000OO0OO0000O0OO =0 
					elif len (O0000O0O0OOO00O00 )==0 :
						print ('Hết Nhiệm Vụ Group',end ='\r');sleep (3 );print ('                                        ',end ='\r')
						O000OO0OO0000O0OO =0 
					else :
						print (f'Tìm Thấy {len(O0000O0O0OOO00O00)} Nhiệm Vụ Group',end ='\r');sleep (3 );print ('                                       ',end ='\r')
				else :
					O0000O0O0OOO00O00 =[]
				if OO00OOO0O00OO0O00 +O000OO0OO0000O0OO +O000OOOOO0O0OO0O0 +O0OOOOO0OO0OO00OO +O00OOOO000O000O0O +O0OO0OOOOOO00O000 +O00OO0OO000O0OOO0 +OOOO0OO0OO0O0OOOO ==0 :
					for OO0O0O00000O000O0 in range (10 ,0 ,-1 ):
						print (f'{luc}Tất Cả Các Nhiệm Vụ Đã Hết, Vui Lòng Chờ {vang}{OO0O0O00000O000O0} {luc}Giây ',end ='\r');sleep (1 );print ('                                                        ',end ='\r')
					continue 
				for OOO0O0OOOOOOO000O in range (100 ):
					if OOOO0OO0OO0O0OOOO ==1 :
						try :OOOO0OOO0O0000OO0 =OO00O0OOO000OO0OO [OOO0O0OOOOOOO000O ]['idpost']
						except :print ('Hết Nhiệm Vụ Like',end ='\r');sleep (1 );print ('                           ',end ='\r');OOOO0OO0OO0O0OOOO =0 
						if OOOO0OO0OO0O0OOOO ==1 :
							OO000O00O0OOO00OO =O0O00OOOOO0OO0O0O .like (OOOO0OOO0O0000OO0 ,'LIKE')
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=400 ;O00O0O0OOO0O0O0OO =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,'LIKE','+400')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'LIKE');O00O0O0OOO0O0O0OO +=1 
							if O00O0O0OOO0O0O0OO >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'  {do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f' {do}Tài Khoản {O000000O00O000000} Đã Bị Block Like !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O00OO0OO000O0OOO0 ==1 :
						try :OOOO0OOO0O0000OO0 =O00O00000O00000O0 [OOO0O0OOOOOOO000O ]['idpost'];O000OO000OOO0O0OO =json .loads (O00O00000O00000O0 [OOO0O0OOOOOOO000O ]['nd'])[0 ]
						except :print ('Hết Nhiệm Vụ Comment',end ='\r');sleep (1 );print ('                               ',end ='\r');OOOO0OO0OO0O0OOOO =0 
						if O00OO0OO000O0OOO0 ==1 :
							OO000O00O0OOO00OO =O0O00OOOOO0OO0O0O .comment (OOOO0OOO0O0000OO0 ,O000OO000OOO0O0OO )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/cmtcheo')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=600 ;O00OOOO000O0OO0O0 =0 
								OO00OOO0OO0OO0000 =O000OO000OOO0O0OO [0 :15 ]+'...'if len (O000OO000OOO0O0OO )>15 else O000OO000OOO0O0OO 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 +f' | {OO00OOO0OO0OO0000}','COMMENT','+600')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'COMMENT');O00OOOO000O0OO0O0 +=1 
							if O00OOOO000O0OO0O0 >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'  {do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f' {do}Tài Khoản {O000000O00O000000} Đã Bị Block Comment !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O0OO0OOOOOO00O000 ==1 :
						try :OOOO0OOO0O0000OO0 =OO0O0OO0O000O000O [OOO0O0OOOOOOO000O ]['idpost']
						except :print ('Hết Nhiệm Vụ Share',end ='\r');sleep (1 );print ('                           ',end ='\r');O0OO0OOOOOO00O000 =0 
						if O0OO0OOOOOO00O000 ==1 :
							OO00OO0OOO00OOOO0 =O0O00OOOOO0OO0O0O .share (OOOO0OOO0O0000OO0 ,'')
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/sharecheo')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=600 ;O0O0O0O0OOO0O000O =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,'SHARE','+600')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'SHARE');O0O0O0O0OOO0O000O +=1 
							if O0O0O0O0OOO0O000O >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Share !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O0OO00O00OOOO0OO0 ==1 :
						try :OOOO0OOO0O0000OO0 =O0OO0OOO0O0OOO0O0 [OOO0O0OOOOOOO000O ]['idpost'];O000OO000OOO0O0OO =json .loads (O0OO0OOO0O0OOO0O0 [OOO0O0OOOOOOO000O ]['nd'])[0 ]
						except :print ('Hết Nhiệm Vụ Share Kèm Nội Dung',end ='\r');sleep (1 );print ('                           ',end ='\r');O0OO0OOOOOO00O000 =0 
						if O0OO0OOOOOO00O000 ==1 :
							OO00OO0OOO00OOOO0 =O0O00OOOOO0OO0O0O .share (OOOO0OOO0O0000OO0 ,O000OO000OOO0O0OO )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/sharecheokemnoidung')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=700 ;O0O0O0O0OOO0O000O =0 
								OO00OOO0OO0OO0000 =O000OO000OOO0O0OO [0 :15 ]+'...'if len (O000OO000OOO0O0OO )>15 else O000OO000OOO0O0OO 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 +f' | {OO00OOO0OO0OO0000}','SHARE','+700')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'SHARE');O0O0O0O0OOO0O000O +=1 
							if O0O0O0O0OOO0O000O >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Share !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if OO00OOO0O00OO0O00 ==1 :
						try :OOOO0OOO0O0000OO0 =OO000OO0OOO0OO0OO [OOO0O0OOOOOOO000O ]['idpost'];OO0OOO00OO0OOO00O =OO000OO0OOO0OO0OO [OOO0O0OOOOOOO000O ]['loaicx']
						except :print ('Hết Nhiệm Vụ Cảm Xúc',end ='\r');sleep (1 );print ('                           ',end ='\r');OO00OOO0O00OO0O00 =0 
						if OO00OOO0O00OO0O00 ==1 :
							OOOO0OO00000000O0 =O0O00OOOOO0OO0O0O .like (OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/camxuccheo',OO0OOO00OO0OOO00O )
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=400 ;O0OOOO0O00O000OO0 =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O ,'+400')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O );O0OOOO0O00O000OO0 +=1 
							if O0OOOO0O00O000OO0 >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Cảm Xúc !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O00OOOO000O000O0O ==1 :
						try :OOOO0OOO0O0000OO0 =O00000OO0O00OO00O [OOO0O0OOOOOOO000O ]['idpost']
						except :print ('Hết Nhiệm Vụ Follow',end ='\r');sleep (1 );print ('                           ',end ='\r');O00OOOO000O000O0O =0 
						if O00OOOO000O000O0O ==1 :
							OO00O0O0OO00O0000 =O0O00OOOOO0OO0O0O .follow (OOOO0OOO0O0000OO0 )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/subcheo')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=600 ;O00OOO0000O0O0O0O =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,'FOLLOW','+700')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'FOLLOW');O00OOO0000O0O0O0O +=1 
							if O00OOO0000O0O0O0O >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Follow !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O0OOOOO0OO0OO00OO ==1 :
						try :OOOO0OOO0O0000OO0 =OO0000OO000OO0O00 [OOO0O0OOOOOOO000O ]['idpost']
						except :print ('Hết Nhiệm Vụ Page',end ='\r');sleep (1 );print ('                           ',end ='\r');O0OOOOO0OO0OO00OO =0 
						if O0OOOOO0OO0OO00OO ==1 :
							O0OO00O0OO0O00O0O =O0O00OOOOO0OO0O0O .page (OOOO0OOO0O0000OO0 )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/likepagecheo')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=700 ;OOO000OOO0O00OO00 =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,'PAGE','+700')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'PAGE');OOO000OOO0O00OO00 +=1 
							if OOO000OOO0O00OO00 >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Page !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O000OOOOO0O0OO0O0 ==1 :
						try :OOOO0OOO0O0000OO0 =OOO0OO0000OO00OO0 [OOO0O0OOOOOOO000O ]['idpost'];OO0OOO00OO0OOO00O =OOO0OO0000OO00OO0 [OOO0O0OOOOOOO000O ]['loaicx']
						except :print ('Hết Nhiệm Vụ Cảm Xúc Comment',end ='\r');sleep (1 );print ('                               ',end ='\r');O000OOOOO0O0OO0O0 =0 
						if O000OOOOO0O0OO0O0 ==1 :
							OO000OOOOO0OOOO0O =O0O00OOOOO0OO0O0O .like (OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/camxuccheobinhluan',OO0OOO00OO0OOO00O )
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=600 ;O00OOOOO00O00O00O =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O +' CMT','+600')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,OO0OOO00OO0OOO00O +' CMT');O00OOOOO00O00O00O +=1 
							if O00OOOOO00O00O00O >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Cảm Xúc CMT !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
					if O000OO0OO0000O0OO ==1 :
						try :OOOO0OOO0O0000OO0 =O0000O0O0OOO00O00 [OOO0O0OOOOOOO000O ]['idpost']
						except :print ('Hết Nhiệm Vụ Group',end ='\r');sleep (1 );print ('                               ',end ='\r');O000OO0OO0000O0OO =0 
						if O000OO0OO0000O0OO ==1 :
							O0OOO0O0000OOO0O0 =O0O00OOOOO0OO0O0O .group (OOOO0OOO0O0000OO0 )
							O000O000O00000O0O =OO00000OOO0O00000 .nhanxu (OOOO0OOO0O0000OO0 ,'/thamgianhomcheo')
							O0OOO0000O0OOO0OO =OO00000OOO0O00000 .coin ()
							if 'Thành công'in O000O000O00000O0O and O0OOO0000O0OOO0OO !=OO00OO00OO00OO00O and O0OOO0000O0OOO0OO !=False :
								O0OOOOO0OOO000O0O +=1 ;OO00OO00OO00OO00O =O0OOO0000O0OOO0OO ;O00OO0OOOOO0O00O0 +=1200 ;OOO00O0O0O00O0O0O =0 
								O0OO0O00OOOOOOOO0 (O0OOOOO0OOO000O0O ,OOOO0OOO0O0000OO0 ,'GROUP','+1200')
								if O0OOOOO0OOO000O0O %10 ==0 :O000O0O0O00O00O0O (OOO0O00OOOO0O00OO ,OO00OO00OO00OO00O ,O00OO0OOOOO0O00O0 )
								if O0OOOOO0OOO000O0O %O00O0O0OOO000O000 ==0 :OO0OO0OOOO000O00O =1 ;break 
								if O0OOOOO0OOO000O0O %O0OOOOO0O0OO0OOOO ==0 :O00OOO0O00O00O0O0 (O00O00O0OO00OO00O )
								else :OO00O000000O00000 (O0O00OO0O0OO0000O ,O00OO0OOOO0O00O00 )
							else :O00OO00000OOO000O (OOOO0OOO0O0000OO0 ,'GROUP');OOO00O0O0O00O0O0O +=1 
							if OOO00O0O0O00O0O0O >=5 :
								O0O000OO0000OOOOO =O0O00OOOOO0OO0O0O .get_thongtin ()
								if O0O000OO0000OOOOO ==0 :
									print (f'{do}Cookie Tài Khoản {O000000O00O000000} Đã Bị Out !!!                ')
								else :
									print (f'{do}Tài Khoản {O000000O00O000000} Đã Bị Block Join Group !!!					')
								OO0O0OOO000OOOOOO .remove (OO00O0OOOO0OOO00O )
								OO0OO0OOOO000O00O =1 
								break 
OO00OOO0O0OOOOO0O ()
class O00O0OOO00OOO00O0 :
    def __init__ (OO000OO00000OO000 ):
        OO000OO00000OO000 .__O0O00O0O0OOO0O000 ()
        OO000OO00000OO000 .__OO0OOO0O0OOOOOO00 ()
        OO000OO00000OO000 .__O0O0O000000OO0000 ()
        OO000OO00000OO000 .__OO00O0O00O00O0OO0 ()
        OO000OO00000OO000 .__OOO00OOO0000OOO00 ()
        OO000OO00000OO000 .__O0OOO0O00O000O00O ()
        OO000OO00000OO000 .__O0OO0O00OOOOO000O ()
        OO000OO00000OO000 .__OO0000OO0O00000O0 ()
        OO000OO00000OO000 .__O0OOO0000O00O0OOO ()
        OO000OO00000OO000 .__O0O0000O0OO00O0O0 ()
        OO000OO00000OO000 .__OOO000O0OOOO0OO00 ()
        OO000OO00000OO000 .__O0OOOOOO00000O0O0 ()
        OO000OO00000OO000 .__OOO00000000OOO000 ()
        OO000OO00000OO000 .__OOOO0000OO000O0O0 ()
        OO000OO00000OO000 .__O0OO00O0000O00000 ()
    def __O0O00O0O0OOO0O000 (O000OOOOOO0O0O0O0 ,O000OOOO0O0OO0OO0 ,OO0O000O000O00O0O ,O0OOOO00O0O0O0OO0 ,O00OOO0O0OOO00000 ,OOOOO000O00O0OOOO ):
        return O000OOOOOO0O0O0O0 .__OO0OOO0O0OOOOOO00 ()
    def __OO0OOO0O0OOOOOO00 (OO0OOOO00OO00O0O0 ,OOO0O00000O00O00O ,O0O0O00O00O0O00OO ,OO000OO00OO000O00 ):
        return OO0OOOO00OO00O0O0 .__OOOO0000OO000O0O0 ()
    def __O0O0O000000OO0000 (OO00OO0O0O0O0O000 ,O000OO00O00O0OOO0 ,OO000OOO00O0OOOO0 ):
        return OO00OO0O0O0O0O000 .__OO00O0O00O00O0OO0 ()
    def __OO00O0O00O00O0OO0 (O0OOOO00O00O00OOO ,OOOO0O00O0OOOOOO0 ,OO0O0OOOOO0000OOO ):
        return O0OOOO00O00O00OOO .__OO0000OO0O00000O0 ()
    def __OOO00OOO0000OOO00 (OO0OO0OOO0OO0OOO0 ,O0000000O0O000O0O ,O00000O0OOOO0OO0O ,O0O00OO0OO000O00O ):
        return OO0OO0OOO0OO0OOO0 .__O0O00O0O0OOO0O000 ()
    def __O0OOO0O00O000O00O (OOO0OOOOO0OO0OO00 ,OOOOOOOO0O0O0O0O0 ):
        return OOO0OOOOO0OO0OO00 .__OOO00OOO0000OOO00 ()
    def __O0OO0O00OOOOO000O (OOOO00OO0O000OO00 ,OOO0O0OO0000O00OO ,OO00OO0O0OOO0OOOO ,O00OOOO00O0O000O0 ,OO00OO0O000000O0O ):
        return OOOO00OO0O000OO00 .__O0OO00O0000O00000 ()
    def __OO0000OO0O00000O0 (OO0OO0O00O0O0O000 ,OO00000OO0OO000O0 ):
        return OO0OO0O00O0O0O000 .__O0OO00O0000O00000 ()
    def __O0OOO0000O00O0OOO (O00O0000O00O00O0O ,OO00OO00O00O00OO0 ,O000OOO00OO00O0O0 ,O00O0O000OOOO0O00 ):
        return O00O0000O00O00O0O .__O0OO0O00OOOOO000O ()
    def __O0O0000O0OO00O0O0 (OOOOO00OO0O0O0OOO ,OO0OOOOO00O0OO0OO ,O0O000OO000O00O00 ,O000000OO0OO000O0 ,O0O0OO0O0OO000O00 ,O0000000OOOOOOO0O ,OOO00OOOOOO0000O0 ):
        return OOOOO00OO0O0O0OOO .__OOO00000000OOO000 ()
    def __OOO000O0OOOO0OO00 (O000O0000O00O0OOO ,OO0OO0O0OO0000000 ):
        return O000O0000O00O0OOO .__OO0OOO0O0OOOOOO00 ()
    def __O0OOOOOO00000O0O0 (O000OOO0O00000O00 ,O00000000O00OOO0O ,OOO0000OOOO00OOOO ,O0O0OOO0O00000OO0 ,O00O0OOO00OO0OO0O ,OOOOOO0O000OOO0O0 ):
        return O000OOO0O00000O00 .__O0OO00O0000O00000 ()
    def __OOO00000000OOO000 (OOO0000O00O0O0OO0 ,O0OO0OO0OOOO000O0 ,OOO00O0O0OOO000O0 ,OO0O0OOO000O00OOO ):
        return OOO0000O00O0O0OO0 .__OOOO0000OO000O0O0 ()
    def __OOOO0000OO000O0O0 (OOO00OO0OOOOO0000 ,O00O000O000O0OO00 ,OO000000O0O00OO00 ,O00O0000O000O000O ,O00OO00OO0OO00000 ):
        return OOO00OO0OOOOO0000 .__OO0000OO0O00000O0 ()
    def __O0OO00O0000O00000 (O0OOOOO00000OOO0O ,O0000O000OOO00OOO ,OOOOOO0OOOOOOO0OO ,O0O0OO0OOO0O00O0O ,OO0O00O000000000O ,OOO0OOO00O00O000O ):
        return O0OOOOO00000OOO0O .__O0O0000O0OO00O0O0 ()
class OO0OO0OOO0O00O00O :
    def __init__ (O000OO0OO0OO0O0OO ):
        O000OO0OO0OO0O0OO .__OO0OO0000O00OO000 ()
        O000OO0OO0OO0O0OO .__O000OO00OO0OO000O ()
        O000OO0OO0OO0O0OO .__O000O00O00OOO0O0O ()
        O000OO0OO0OO0O0OO .__OO00OOOO00OOO0OOO ()
        O000OO0OO0OO0O0OO .__OOO0O000O0OOO000O ()
        O000OO0OO0OO0O0OO .__OO000000OO0O0O0O0 ()
        O000OO0OO0OO0O0OO .__OOOOO00OO00O0O0OO ()
        O000OO0OO0OO0O0OO .__O0OO0O0O0OOO0O000 ()
        O000OO0OO0OO0O0OO .__OO000O0O0O0O00OO0 ()
        O000OO0OO0OO0O0OO .__O0000OO0OO00O00OO ()
        O000OO0OO0OO0O0OO .__OOOOO00O000O00O0O ()
        O000OO0OO0OO0O0OO .__OO00OO0000OO0OOO0 ()
        O000OO0OO0OO0O0OO .__O0O0OOO0O0000O000 ()
        O000OO0OO0OO0O0OO .__O00000O0OO0O0000O ()
        O000OO0OO0OO0O0OO .__O000O0OOOO00OO0O0 ()
    def __OO0OO0000O00OO000 (O00OOOO0OOOOOOO0O ,O0O00OOO00OOO0O0O ,OOOO0OO00000OO0OO ,OO0OOO0OOO000O0OO ,O000000OOO00000O0 ,OOO0OOO0OOO0000OO ,OOOO00OOOOOOOO000 ):
        return O00OOOO0OOOOOOO0O .__OOOOO00OO00O0O0OO ()
    def __O000OO00OO0OO000O (OOO0OO000O0O00000 ,OOOO0000000OO00O0 ,O000OO0000OO0OOO0 ):
        return OOO0OO000O0O00000 .__O000O0OOOO00OO0O0 ()
    def __O000O00O00OOO0O0O (O00OOOO00OO00OO00 ,OO0O00O0OOO0OO0O0 ,OOOOOOO00OOO0O0O0 ,O0OO000OO0O00000O ,O00OO0O000OOO00OO ,O00OO0O0OOOO0O0OO ,OOO0O0O00O00O0OOO ):
        return O00OOOO00OO00OO00 .__OO0OO0000O00OO000 ()
    def __OO00OOOO00OOO0OOO (O0O0OOOOO00000000 ,OOOO000OOO0OOOO0O ,O0000000OO0OOOO0O ,O0OOOOOOO0O000OO0 ,OOO00000OO0O0O0O0 ):
        return O0O0OOOOO00000000 .__O0OO0O0O0OOO0O000 ()
    def __OOO0O000O0OOO000O (O0O0000O00000O0OO ,O00000OO0OOO0OO00 ,OOOO0O0OO00O0O0OO ,OO00OOO00OOOO0000 ,OO0OO0OO0OOOO0OO0 ):
        return O0O0000O00000O0OO .__OOO0O000O0OOO000O ()
    def __OO000000OO0O0O0O0 (OO0O0OOO0OOO00000 ,O00000OOO0000OO0O ,O0OO0OOOO0OOOO0O0 ):
        return OO0O0OOO0OOO00000 .__O0OO0O0O0OOO0O000 ()
    def __OOOOO00OO00O0O0OO (O0OOOOO0O0OOOOOO0 ,OOOO0O000O000O0O0 ,OOO0O0OO00000O0OO ,O00000OOOOO00O00O ,OOOO00O0OO000O00O ):
        return O0OOOOO0O0OOOOOO0 .__OO0OO0000O00OO000 ()
    def __O0OO0O0O0OOO0O000 (OOOOOOO0OO0O0O000 ,OO000O0O00O00O0OO ,O0OO0OOOOO00000OO ,O00OOOO0000OO00OO ,OOO00O0O0O00OO000 ,OO00O0OOO0000OO00 ):
        return OOOOOOO0OO0O0O000 .__OO00OO0000OO0OOO0 ()
    def __OO000O0O0O0O00OO0 (OOOO000O0O0OO0O0O ,OO0OOO0OOO000OO00 ,O000000O0O0O0O00O ,OOO0000O0O000OO0O ,O0OO0O0OOO00O0O0O ,OOO0000OO00OOO0OO ):
        return OOOO000O0O0OO0O0O .__O000OO00OO0OO000O ()
    def __O0000OO0OO00O00OO (O0OOOOOO00000OOOO ,OOO00OOOOOOO00OOO ,OO0O00O0000OOOOO0 ,OO000OO00O00OO0O0 ,OOO000OOOOO00O0O0 ,OOO00O00O00O0OOO0 ,O000O00O0O000O0O0 ,O00OOOOO000OO0O00 ):
        return O0OOOOOO00000OOOO .__OOOOO00O000O00O0O ()
    def __OOOOO00O000O00O0O (OOO0OO000000O0O0O ,O000O0000O00OO0OO ,O00OOO0O0O0000000 ,OOO000O00OO0O000O ,OO00OO00000O000O0 ,OOOOOO000OO0O0OO0 ):
        return OOO0OO000000O0O0O .__OO0OO0000O00OO000 ()
    def __OO00OO0000OO0OOO0 (O0O0OOO0OO0O0OO0O ,O0O0OO0O0O00000OO ,OO0OOO0OO0O0000O0 ,O0OO000000O000OOO ,OO0OO0000O0OO0000 ,O0OOOO00000OOO0OO ,OO00O0000000OO0O0 ,O0O0OO0OO000O000O ):
        return O0O0OOO0OO0O0OO0O .__OOOOO00OO00O0O0OO ()
    def __O0O0OOO0O0000O000 (O0O0O0OOOOOO0O00O ,O00O000OO000OOO00 ,O0OO0OOOOO0000000 ,OOO0O00OO000O00OO ,OOO00000OO00OO0OO ,O0OOOO00OOOOO00OO ):
        return O0O0O0OOOOOO0O00O .__OO00OOOO00OOO0OOO ()
    def __O00000O0OO0O0000O (OOOO000OO0000O00O ,OOOO0O00O0OOO00OO ,OOOOOOO0O0OOOO00O ,O0O00O00O00O0O000 ,OO00O0000000OO000 ,OO0OOO000OOOO0OOO ,OO0O0000O000O0O0O ):
        return OOOO000OO0000O00O .__OO00OOOO00OOO0OOO ()
    def __O000O0OOOO00OO0O0 (O00OOO0O0O0O00OO0 ,OO0O000O0OOOO000O ,O0000000OOOOOOOOO ,OO000OOOOOO0000OO ,O0000OO00OOOOO000 ,O00000OOOO00OO0O0 ):
        return O00OOO0O0O0O00OO0 .__OOO0O000O0OOO000O ()
class O00OOO0O000000000 :
    def __init__ (OOOOO0OO0O00OO00O ):
        OOOOO0OO0O00OO00O .__OOOOOO0O0OOO00O0O ()
        OOOOO0OO0O00OO00O .__OO0OO00OOO00OOOOO ()
        OOOOO0OO0O00OO00O .__OOO0OO0000OOO0000 ()
        OOOOO0OO0O00OO00O .__O0O00O0000OO0OO0O ()
        OOOOO0OO0O00OO00O .__O0000000O000OO00O ()
    def __OOOOOO0O0OOO00O0O (OOO00OO00O0OOOOOO ,O0OOOOO000O00OO00 ):
        return OOO00OO00O0OOOOOO .__OOOOOO0O0OOO00O0O ()
    def __OO0OO00OOO00OOOOO (OO0OOOOOO00OO0O00 ,O0O00O0OO0OOO00O0 ,OOO0O0O00OOO0OO0O ,O0O00O0000000000O ,O0OOOOO0O00000O0O ):
        return OO0OOOOOO00OO0O00 .__OOO0OO0000OOO0000 ()
    def __OOO0OO0000OOO0000 (O000000000OO0OOO0 ,OO000O0O00O00O00O ,O0000OO0O0O0OOOO0 ,OOOOO0O000O0OOO0O ,O0OO0OOO00OO0OO00 ,O0OO0O0OOOOOOOOO0 ,OOO00O0O0O00O0OOO ):
        return O000000000OO0OOO0 .__O0O00O0000OO0OO0O ()
    def __O0O00O0000OO0OO0O (O0O0O0OO0O00000O0 ,O00OO0O000O0000O0 ,OOO00O0OO00OOO0O0 ,OOO0OO0OO000O0O00 ,O00O000O0O0O000O0 ,O000O00OOOOO0OOO0 ):
        return O0O0O0OO0O00000O0 .__O0000000O000OO00O ()
    def __O0000000O000OO00O (OO0OOOO0O000OO00O ,O0OO0O00O00OO0OO0 ,O000OOO000OOOOO0O ,OOO000000O0OO0OO0 ):
        return OO0OOOO0O000OO00O .__OOO0OO0000OOO0000 ()
class OOO0OO0O0O00OO00O :
    def __init__ (O000O00OO0O00O000 ):
        O000O00OO0O00O000 .__O00OOOO0O00OOO00O ()
        O000O00OO0O00O000 .__O00OOOO00O00OO00O ()
        O000O00OO0O00O000 .__OOOO0O00OO0O0O000 ()
        O000O00OO0O00O000 .__O0O00OOO0000OO00O ()
        O000O00OO0O00O000 .__O000OO00O0O00O000 ()
        O000O00OO0O00O000 .__O0O00O0O00OOO0O00 ()
        O000O00OO0O00O000 .__OOO0O0O0OO0O000OO ()
        O000O00OO0O00O000 .__O0OOOO0O0OOO0000O ()
        O000O00OO0O00O000 .__O0O0OOOOO0OO000O0 ()
        O000O00OO0O00O000 .__O000O0O0O0000O00O ()
        O000O00OO0O00O000 .__OO0OOO0OOOOO000OO ()
        O000O00OO0O00O000 .__OO00000OOOOO0O0O0 ()
        O000O00OO0O00O000 .__O000O00OO0OOO0OOO ()
    def __O00OOOO0O00OOO00O (OO00OO00O0O0000OO ,O0O00000000OOOOOO ,O000OO00OOO0000O0 ,O000OOO0O0O0OO0O0 ):
        return OO00OO00O0O0000OO .__OO0OOO0OOOOO000OO ()
    def __O00OOOO00O00OO00O (O00O0OO00OOOOO000 ,OO0000OOO0000O00O ,O0O0O00OO00OO00O0 ,OO00OOOOO0O000O0O ,OO00OOOO000OO0O00 ):
        return O00O0OO00OOOOO000 .__OOOO0O00OO0O0O000 ()
    def __OOOO0O00OO0O0O000 (OO0O0OO0000O0OO0O ,O0OO0O00000O0OOOO ,OO0OO00OOO0O00OO0 ,O0O000O00OOO0O00O ):
        return OO0O0OO0000O0OO0O .__O0O0OOOOO0OO000O0 ()
    def __O0O00OOO0000OO00O (OOO000000000O0000 ,OOO00000OOOOO0O00 ,O00OO0O0OO0O00OO0 ,O00O0O000O0OO000O ):
        return OOO000000000O0000 .__OOO0O0O0OO0O000OO ()
    def __O000OO00O0O00O000 (O0000OOO000000O0O ,OOO0O0OOO0O0O0O0O ,O0OOO0OOO0000O0OO ,O0OOOO000O0000OOO ,OO0OOOO00OO000O00 ,OOO0OOO0OOOO0OOO0 ):
        return O0000OOO000000O0O .__OOOO0O00OO0O0O000 ()
    def __O0O00O0O00OOO0O00 (OO000OOO0O0000000 ,O0O00O0OO0OOO00OO ,O0OOOO0O0O000OOO0 ):
        return OO000OOO0O0000000 .__O00OOOO0O00OOO00O ()
    def __OOO0O0O0OO0O000OO (OOOO0O00O0O0OO0O0 ,OOO0OO00O0000OO0O ):
        return OOOO0O00O0O0OO0O0 .__OO00000OOOOO0O0O0 ()
    def __O0OOOO0O0OOO0000O (O000OO000OO0O0O00 ,OOOOO0OOOOOO0O0O0 ,OOOOOOOOOOO00O000 ,OOOO0O00OO0OOOO0O ,O0OO0OO0O0OO0000O ,O000OO000O0000000 ,O00000O0O00OO0000 ):
        return O000OO000OO0O0O00 .__O000OO00O0O00O000 ()
    def __O0O0OOOOO0OO000O0 (OOOOO0O00O0O00OO0 ,O0OOO000O0O00O00O ,O0OO00000O0OO000O ,O0O0O00O00OOOO0OO ,O00OOO00OO0O0OOO0 ):
        return OOOOO0O00O0O00OO0 .__O00OOOO0O00OOO00O ()
    def __O000O0O0O0000O00O (O00O0O0O000O0O0OO ,O0O00O00O0OOO00O0 ,OO0000O0O000O00O0 ,OOO0OOOO0O00OOOOO ,O0OOO00OO0OOOO0OO ):
        return O00O0O0O000O0O0OO .__O0OOOO0O0OOO0000O ()
    def __OO0OOO0OOOOO000OO (O000OO00000O00O00 ,OO0O0OO0OO000O0OO ):
        return O000OO00000O00O00 .__O000OO00O0O00O000 ()
    def __OO00000OOOOO0O0O0 (OOOO00OOOOO0OO000 ,OO00OOOOOOO0O00OO ,OOOOOO0000O00O0O0 ,OO00000OOOOOO0000 ,OO000O0OO00OOOO00 ):
        return OOOO00OOOOO0OO000 .__OO00000OOOOO0O0O0 ()
    def __O000O00OO0OOO0OOO (O00000OO0OOOOOO00 ,O0O0O000O00000OOO ,O0000OOOO0O00O0OO ,O00OO000OOOOOO0OO ,O0O0OOOO000O0O000 ,O000O0OOO000OOO00 ):
        return O00000OO0OOOOOO00 .__O0O00O0O00OOO0O00 ()
class O00O0O0O0OO0OO0OO :
    def __init__ (OO0OO0O0000O0OO00 ):
        OO0OO0O0000O0OO00 .__OOO000O0O0OO0O000 ()
        OO0OO0O0000O0OO00 .__OO0O00O0O0OOO0OO0 ()
        OO0OO0O0000O0OO00 .__O0OOOOOO0OOO0OOOO ()
        OO0OO0O0000O0OO00 .__O0O0OO0O0OOO0OO00 ()
        OO0OO0O0000O0OO00 .__OOOO0OOO0O00O0OO0 ()
    def __OOO000O0O0OO0O000 (OOO0OOOO0O00OOO0O ,OO000O0O0O0000O00 ,O000OOOOOO0O00O00 ,O0OO0O00O00OO0OOO ):
        return OOO0OOOO0O00OOO0O .__OOO000O0O0OO0O000 ()
    def __OO0O00O0O0OOO0OO0 (OO0OO00OOO00000O0 ,OOO000OOO0O0OOOO0 ,OO00O0OOO0O000OOO ,OO0OO0OO0000O0O00 ,OO0000OOOO0000O0O ):
        return OO0OO00OOO00000O0 .__OOO000O0O0OO0O000 ()
    def __O0OOOOOO0OOO0OOOO (O00OO0OOO0O00OOO0 ,OO000OO0OO00OOO00 ,OO0O000OOOO00O0O0 ,OOO0OO000OO0O0O00 ,O00OOOO00O0OOO00O ,OO0O0OO00OOO0OO0O ,OOO0OOOOO000000O0 ,OO00OOO00OO00000O ):
        return O00OO0OOO0O00OOO0 .__OOOO0OOO0O00O0OO0 ()
    def __O0O0OO0O0OOO0OO00 (O00OO0OO0O00OOOO0 ,OOOO00O000O0O00OO ,O00OOOO0OOO0O00OO ,OOO00O00O000O0000 ,O000OO0O00O00OOOO ,OOO00O0O00O000OOO ,OO0OO00OO0OO0O000 ,O00O00OO0000000O0 ):
        return O00OO0OO0O00OOOO0 .__O0O0OO0O0OOO0OO00 ()
    def __OOOO0OOO0O00O0OO0 (OOO0O000OOO00O0O0 ,OOOO0OO0OOOO0OOOO ,OOO00O0OO000OOOOO ,OOOOO00000O0OO00O ):
        return OOO0O000OOO00O0O0 .__OOOO0OOO0O00O0OO0 ()
class O0O0OO0000OOO0000 :
    def __init__ (O0O0OO00O0O00OO0O ):
        O0O0OO00O0O00OO0O .__O0O000OOO0O000OOO ()
        O0O0OO00O0O00OO0O .__OOOOOO0OO0OOO00OO ()
        O0O0OO00O0O00OO0O .__OOO0OO00O00O0O000 ()
        O0O0OO00O0O00OO0O .__O0OO0O00OOOOOOO00 ()
        O0O0OO00O0O00OO0O .__OOOOOO000O00O0000 ()
        O0O0OO00O0O00OO0O .__O000OOOO00OO0O0OO ()
        O0O0OO00O0O00OO0O .__O0000OO0OO0O0OO00 ()
        O0O0OO00O0O00OO0O .__O00O0OOOOO000O00O ()
        O0O0OO00O0O00OO0O .__OO0O0O00O0000OO00 ()
        O0O0OO00O0O00OO0O .__O0OO00000OO00OO00 ()
        O0O0OO00O0O00OO0O .__O0OO0O0OO0O0OOOOO ()
    def __O0O000OOO0O000OOO (O0OOOOO0O000000OO ,O0O00O00O0O00OOO0 ,OOO00000OOO0O00OO ,OO0O00OO0O00O0000 ):
        return O0OOOOO0O000000OO .__OOOOOO000O00O0000 ()
    def __OOOOOO0OO0OOO00OO (OO0OO0O000O0O0000 ,OO0OOOO00O00OO0O0 ,O00OO00OOOOO0O0OO ,O00OO00O0O00O000O ,OOOOOOO0O00OOOO0O ,O0O0OO00O0OO00OOO ,O0O000OOOOOO00OO0 ,O000O0O00OO00O00O ):
        return OO0OO0O000O0O0000 .__O0OO0O0OO0O0OOOOO ()
    def __OOO0OO00O00O0O000 (O000OO0OOO0OOOOOO ,OO0000OO0O0O0OOOO ,OOOO0O00OO000O0OO ,O0OOOOOOOO00O00OO ,O0OOOOOO0O0OOOO00 ,OOOO0000OOOO00OOO ,O0OO00OOO000OOOO0 ):
        return O000OO0OOO0OOOOOO .__O0OO00000OO00OO00 ()
    def __O0OO0O00OOOOOOO00 (OO0OO0O0OOOOOOOO0 ,O00O0O0O0O0OO000O ,OO0O000O0O0OOOOOO ):
        return OO0OO0O0OOOOOOOO0 .__O0OO0O00OOOOOOO00 ()
    def __OOOOOO000O00O0000 (O000O00OOOO0OO0OO ,O000000000O0O0OOO ):
        return O000O00OOOO0OO0OO .__OOO0OO00O00O0O000 ()
    def __O000OOOO00OO0O0OO (OOOOO0OO0O0O0O0OO ,O0OO0OOOO00O0O00O ,O0000OOOO0OO0OOO0 ):
        return OOOOO0OO0O0O0O0OO .__OOO0OO00O00O0O000 ()
    def __O0000OO0OO0O0OO00 (O0OO0O0OO000O0OOO ,O0OO00OOOO0OO0OO0 ,OOO00O0O00O0OOO00 ):
        return O0OO0O0OO000O0OOO .__O0000OO0OO0O0OO00 ()
    def __O00O0OOOOO000O00O (O0O000OO0O0OOO00O ,O0O0000O0O0000000 ,O000O00OOO00OO000 ,O0000O00O00OO00O0 ,OOOOOO0O0OOOO0OO0 ,O00OOO00000O00000 ,OOO0OO000OOOO00OO ,O0O00O00OOO0O00OO ):
        return O0O000OO0O0OOO00O .__OOOOOO0OO0OOO00OO ()
    def __OO0O0O00O0000OO00 (O0000OOO000OOOO0O ,OO00OO0O0000OOOO0 ):
        return O0000OOO000OOOO0O .__O0OO0O00OOOOOOO00 ()
    def __O0OO00000OO00OO00 (O00000O000OOO00OO ,O0O000O0OO0OO0OOO ,OOOOO000OOO000O0O ,OO00000O0OOOOOOOO ,O0OO0OOOO00O0000O ):
        return O00000O000OOO00OO .__O0OO0O00OOOOOOO00 ()
    def __O0OO0O0OO0O0OOOOO (OO0OOOO0O0000OO0O ,O0000O000O0O000OO ,O0OOO0OO00OOO0000 ,OOO0O000OOOO00O0O ,OOOOOOO0O000OOO00 ,OOO00O00O00O00OO0 ,OO00O000O00O000O0 ,O0000O0O0O00OOOOO ):
        return OO0OOOO0O0000OO0O .__O0OO0O00OOOOOOO00 ()
class OOO0000O0OOOOO000 :
    def __init__ (O0O00000O0O0O0O0O ):
        O0O00000O0O0O0O0O .__OOOO00OOOO0O0O0O0 ()
        O0O00000O0O0O0O0O .__OOOOO00OO00000O0O ()
        O0O00000O0O0O0O0O .__O00OOOOOO0O0OOOOO ()
        O0O00000O0O0O0O0O .__OOOOOOOO00O00OOO0 ()
        O0O00000O0O0O0O0O .__O0OO0OO000O0OOO0O ()
        O0O00000O0O0O0O0O .__OO0O0O0OOOO000O0O ()
        O0O00000O0O0O0O0O .__OO0O000O0000OO00O ()
        O0O00000O0O0O0O0O .__OOO000OO000000000 ()
        O0O00000O0O0O0O0O .__O0OO0O0OOOOO00OO0 ()
        O0O00000O0O0O0O0O .__O000O0O000O00O000 ()
    def __OOOO00OOOO0O0O0O0 (O0OO0OO0O000OO00O ,OO0OOOOO0OOOOOO00 ,OO0O0OOOO000O0000 ,O0000O0000000OOO0 ,OOOO0O00O0OOOOO00 ):
        return O0OO0OO0O000OO00O .__OOOO00OOOO0O0O0O0 ()
    def __OOOOO00OO00000O0O (OOO0O0OO00OO00000 ,OOOOO0000O00O00O0 ):
        return OOO0O0OO00OO00000 .__OOOOOOOO00O00OOO0 ()
    def __O00OOOOOO0O0OOOOO (OOOOOO0000OOOOOO0 ,O000O00OO0000O000 ,O0O00000O0OOOOOOO ):
        return OOOOOO0000OOOOOO0 .__OOOOOOOO00O00OOO0 ()
    def __OOOOOOOO00O00OOO0 (OOOO0O0O00O0O00OO ,OOOO0000OO00OO0OO ,O0O0000000O0O0OOO ,OO00O00000O0OOO00 ,O0OO00000O0OOOO0O ,OOOO0OOO0O00O00OO ):
        return OOOO0O0O00O0O00OO .__O0OO0O0OOOOO00OO0 ()
    def __O0OO0OO000O0OOO0O (O0O0O0000OO0OOO0O ,OO0OOOO000O000000 ,OOO0O0OO00O00OO00 ,OO000OOOOO00OOOO0 ,O00OOOOO0O00OOO0O ,OO000O0OOOOO0O0O0 ,O000000OO000O00OO ,OOO00OOOOOOOOO0O0 ):
        return O0O0O0000OO0OOO0O .__OO0O000O0000OO00O ()
    def __OO0O0O0OOOO000O0O (OO000O0OOOOO00OOO ,OO00O000OO000OO00 ,O00O00OO0O00OOO00 ):
        return OO000O0OOOOO00OOO .__OOOOOOOO00O00OOO0 ()
    def __OO0O000O0000OO00O (OO0OO0O0000OO00O0 ,O0OO0O00O0000OO0O ,OOO0O00OOOO0O0O00 ,OO0O000000O00000O ,O0OOOOOO0O00O00O0 ,OOO0000O0O0OOO0OO ,O0OOOOOO0OO00000O ):
        return OO0OO0O0000OO00O0 .__OO0O0O0OOOO000O0O ()
    def __OOO000OO000000000 (O000O0O000OO0O0O0 ,OOO0O0OO00OOOO0OO ,OO0000O000OOO0000 ,OOO0OOOOOOOO0O00O ,OOOOO00OO0O0O0OO0 ):
        return O000O0O000OO0O0O0 .__O00OOOOOO0O0OOOOO ()
    def __O0OO0O0OOOOO00OO0 (O0000O0000O00OOO0 ,O0OO0OOO0OO0OO000 ,O0O0OOO00O0OO0OO0 ,OOOO00OOO0OOOOO00 ,OO000OO0O0O00O0O0 ,OO0OO00OOOO0O00OO ,OOO0O0OO00O0OOOO0 ):
        return O0000O0000O00OOO0 .__OOOO00OOOO0O0O0O0 ()
    def __O000O0O000O00O000 (O0O0O0O0O0O000OO0 ,O00OOOO0OOO00O0OO ,OOOO0O0OO0OO00OOO ,O0O00OO00OOOOO00O ,O00O00O0O00O00O00 ,OOO0O0OO0OO00OOOO ):
        return O0O0O0O0O0O000OO0 .__OOOO00OOOO0O0O0O0 ()
