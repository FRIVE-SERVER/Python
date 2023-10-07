import re, requests, json, random, base64, time, os, datetime, sys, socket
from urllib.parse import quote
from bs4 import BeautifulSoup
from sys import platform
from time import sleep,strftime
from pystyle import Write,Colors
from datetime import datetime
from pystyle import Colors, Colorate
from datetime import date
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\e[35m"
hong = "\033[1;95m"
thanh_xau=red+"["+vang+"⟨⟩"+red+"]"+trang +"➩"+luc
ip = requests.post('https://api.proxyscrape.com/ip.php').text
def clear ():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
	    os.system("cls")
def network():
    try :
        socket.create_connection(("1.1.1.1",53 ))
        return True 
    except OSError :
        pass
    return False
def banner():
      clear()
      t=(f'                   {Colorate.Horizontal(Colors.green_to_cyan,   "         ███████╗██████╗ ██╗██╗   ██╗███████╗")}')
      t_1=(f'                   {Colorate.Horizontal(Colors.green_to_cyan, "         ██╔════╝██╔══██╗██║██║   ██║██╔════╝")}')
      t_2=(f'                   {Colorate.Horizontal(Colors.green_to_cyan, "         █████╗  ██████╔╝██║██║   ██║█████╗")}')
      t_3=(f'                   {Colorate.Horizontal(Colors.green_to_cyan, "         ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ")}')
      t_4=(f'                   {Colorate.Horizontal(Colors.green_to_cyan, "         ██║     ██║  ██║██║ ╚████╔╝ ███████╗")}')
      t_5=(f'                   {Colorate.Horizontal(Colors.green_to_cyan, "         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝")}')
      t_6=(f'                        {Colorate.Horizontal(Colors.blue_to_cyan, "CopyRight: © FRIVE 2023 | Tool Version: 1.0")}\n')
      print(f'{t}\n{t_1}\n{t_2}\n{t_3}\n{t_4}\n{t_5}\n{t_6}')

clear()
banner()
print(f'{red}╔═══════════╦═══════════════════════════════════════╦══════════════════╦═══════════════════╗')
print(f'{red}║   {vang}ORDER   {red}║                {vang}MENU TOOL              {red}║      {vang}STATUS      {red}║      {vang}VERSION      {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║     {vang}1     {red}║     {lamd}TOOL TRAO ĐỔI SUB FACEBOOK        {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║     {vang}2     {red}║     {lamd}TOOL TRAO ĐỔI SUB FACEBOOK        {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║     {vang}3     {red}║     {lamd}TOOL TRAO ĐỔI SUB INSTAGRAM       {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║     {vang}4     {red}║       {lamd}TOOL TRAO ĐỔI SUB TIKTOK        {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╩═══════════════════╣')
print(f'{red}║     {vang}5     {red}║    {lamd}TOOL TRAO ĐỔI SUB FACEBOOK PRO5    {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╩═══════════════════╣')
print(f'{red}║     {vang}6     {red}║   {lamd}TOOL TRAO ĐỔI SUB TIKTOK MAX SPEED  {red}║      {luc}ONLINE      {red}║       {lamd}[1.0]       {red}║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╩═══════════════════╣')
print(f'{red}║     {vang}7     {red}║               {lamd}QUAY LẠI                {red}║          {luc}ADMIN: {vang}FRIVE {red}- {vang}TOOL         {red}║')
print(f'{red}╠═══════════╩═══════════════════════════════════════╩══════════════════════════════════════╣')
print(f'{red}║                          {red}[{vang}LƯU Ý{red}] {lamd}LỰA CHỌN THÌ NHẬP SỐ NHA {red}[{lamd}1{red}-{vang}>{lamd}7{red}]                         {red}║')
print(f'{red}╚══════════════════════════════════════════════════════════════════════════════════════════╝')
print(f'')
print(f'{red}╔════[{tim}FRIVE{vang}-{lamd}TOOL{red}]')
print(f'{red}║')
chon = input(f'{red}╚════════⋗{hong}⋗{tim}⋗ ')
clear()

try:
    if chon == '1':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/facebook.py').text
    elif chon == '2':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/fb.py').text
    elif chon == '3':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/ins.py').text
    elif chon == '4':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/tiktok.py').text
    elif chon == '5':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/tdspro5.py').text
    elif chon == '6':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/tiktok_speed.py').text
    elif chon == '7':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/main.py').text
except:
    if not network():
        print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
    else :
        print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
    exit()

exec(code, globals())