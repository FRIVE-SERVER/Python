import re, requests, json, random, base64, time, os, datetime, sys, socket
from urllib.parse import quote
from bs4 import BeautifulSoup
from sys import platform
from time import sleep,strftime
from pystyle import Write,Colors
from datetime import datetime
from pystyle import Colors, Colorate
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau=red+"["+vang+"⟨⟩"+red+"]"+trang +"➩"+luc
ip = requests.post('https://api.proxyscrape.com/ip.php').text
def clear ():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
	    os.system("cls")
def checkkey(key):
    try:
        key_phi = requests.get(f'https://keysieuvip.link/api/key?key={key}').json()
        if key_phi["status"] == "success":
            return key_phi["name"], key_phi["start"], key_phi["end"]
        else:
            return [key_phi["messenger"]]
    except:
        return False 
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
try:
		b = '\033[1;32mVui Lòng Chờ...\033[0m\n'
		for i in range(len(b)):
			sys.stdout.write(b[i])
			sys.stdout.flush()
			sleep(0.02)
		get = requests.get(f'https://keysieuvip.link/api/api.php').json()
		link = get['link']
		ma_key = get['key']
except:
	ma_key = 'frive'
	link = f'{red}SERVER KEY FREE LỖI HÃY DÙNG KEY: {vang}{ma_key}'
clear()        
banner()
while True:
	check_file_key=os.path.exists("Key_Tool.txt")
	if check_file_key == False:
		print(f'{thanh_xau} {luc}IP HIỆN TẠI CỦA BẠN LÀ: {vang}{ip}')
		print(f'{thanh_xau} {luc}LINK LẤY KEY: {vang}{link}')
		key = input(f'{thanh_xau} {luc}NHẬP KEY ĐÃ MUA HOẶC KEY FREE: {vang}');print(red,end='')
		key_phi = checkkey(key)
		if key == ma_key:
			print(f'{lam}KEY CHÍNH XÁC')
			check = ''
			
			file_key = open(f"Key_Tool.txt", "a+")
			file_key.write(key)
			file_key.close()
			break
		elif checkkey == False:print(red+'SERVER KEY PHÍ GẶP LỖI HÃY DÙNG KEY FREE'); continue 
		elif checkkey != False:
			try:
				name = key_phi[0];batdau = key_phi[1];hethan = key_phi[2];check = True;keycode = key
				print(f'{lam}KEY CHÍNH XÁC ')
				file_key = open(f"Key_Tool.txt", "a+")
				file_key.write(key)
				file_key.close()
				break
			except:
				print(f"{red}{key_phi[0]}")
				exit(0)
		else:
			print(f"KEY KHÔNG CHÍNH XÁC, BẠN CHẮC CHẮN ĐÃ NHẬP ĐÚNG KEY?")
			exit(0)
	else:
		file_key = open(f"Key_Tool.txt", "r")
		key_cu = file_key.read()
		file_key.close()
		key_phi = checkkey(key_cu)
		if key_cu == ma_key:
			print(f'{lam}KEY CHÍNH XÁC ',end= '\r')
			check = ''
			
			break
		elif key_phi == False:print(red+'SERVER KEY PHÍ GẶP LỖI HÃY DÙNG KEY FREE');os.remove('Key_Tool.txt'); continue 
		elif key_phi != False:
			try:
				name = key_phi[0];batdau = key_phi[1];hethan = key_phi[2];check = True;keycode = key_cu
				print(f'{lam}KEY CHÍNH XÁC')
				
				break
			except:
				if key_phi[0] == 'KEY KHÔNG TỒN TẠI! BẠN CHẮC CHẮN ĐÃ NHẬP ĐÚNG KEY?':
					print(f'KEY{key_cu}ĐÃ ĐƯỢC THAY THẾ HÃY LẤY KEY MỚI')
				else:
					print(key_phi[0])
				os.remove('Key_Tool.txt')
				continue 
		else:
			print(f"KEY KHÔNG CHÍNH XÁC, BẠN CHẮC CHẮN ĐÃ NHẬP ĐÚNG KEY?")
			exit(0)

clear()
banner()
if check == True:
	if len(keycode) == 3 or len(keycode) == 2 or len(keycode) == 1: keycode = '*'*len(keycode)
	elif len(keycode) == 4: keycode = keycode.replace(keycode[0:3], '***')
	elif len(keycode) == 5: keycode = keycode.replace(keycode[0:4], '****')
	elif len(keycode) == 6: keycode = keycode.replace(keycode[0:5], '*****')
	elif len(keycode) == 7: keycode = keycode.replace(keycode[0:5], '*****')
	else: keycode=keycode.replace(keycode[0:len(keycode)-3], '*'*len(keycode[0:len(keycode)-3]))
	print('\033[1;33m[\033[1;31mWARNING\033[1;33m] \033[1;32mBẠN ĐANG DÙNG KEY PHÍ')
	print(f'{thanh_xau} {luc}NGƯỜI MUA: {vang}{name}\n{thanh_xau} {luc}KEY CODE: {vang}{keycode}\n{thanh_xau} {luc}NGÀY MUA KEY: {vang}{batdau}\n{thanh_xau} {luc}NGÀY HẾT HẠN: {vang}{hethan}\n')


print(f'{red}╔═══════════╦═══════════════════════════════════════╦══════════════════╦═══════════════════╗')
print(f'{red}║  {vang} ORDER  {red} ║   {vang}             MENU TOOL        {red}      ║  {vang}    STATUS  {red}    ║  {vang}    VERSION    {red}  ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  1  {red}   ║   {lamd}        TOOL TRAO ĐỔI SUB  {red}         ║  {luc}    ONLINE    {red}  ║     {lamd}  [1.0]     {red}  ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  2    {red} ║     {lamd}     TOOL TƯƠNG TÁC CHÉO       {red}   ║   {luc}   ONLINE    {red}  ║    {lamd}   [1.0]   {red}    ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  3    {red} ║        {lamd}   TOOL PAGE PROFILE        {red}   ║   {luc}   ONLINE    {red}  ║    {lamd}   [1.0]   {red}    ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  4    {red} ║          {lamd}   TOOL TIỆN ÍCH           {red}  ║   {luc}   ONLINE    {red}  ║  {lamd}     [1.0]    {red}   ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  5    {red} ║          {lamd}   ZEFOY SELENIUM           {red} ║   {luc}   ONLINE    {red}  ║  {lamd}     [1.0]    {red}   ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╬═══════════════════╣')
print(f'{red}║   {vang}  6    {red} ║          {lamd}GET TOKEN FULL LOẠI [PHÍ]   {red} ║   {luc}   ONLINE    {red}  ║  {lamd}     [1.0]    {red}   ║')
print(f'{red}╠═══════════╬═══════════════════════════════════════╬══════════════════╩═══════════════════╣')
print(f'{red}║   {vang}  7   {red}  ║          {lamd}     THOÁT TOOL            {red}  ║        {luc}  ADMIN:{vang} FRIVE{red} - {vang}TOOL       {red}  ║')
print(f'{red}╠═══════════╩═══════════════════════════════════════╩══════════════════════════════════════╣')
print(f'{red}║                     {red}     [{vang}LƯU Ý{red}] {lamd}LỰA CHỌN THÌ NHẬP SỐ NHA {red}[{lamd}1{red}-{vang}>{lamd}7{red}]                         ║')
print(f'{red}╚══════════════════════════════════════════════════════════════════════════════════════════╝')
print(f'')
print(f'{red}╔════[{tim}FRIVE{vang}-{lamd}TOOL{red}]')
print(f'{red}║')
chon = input(f'{red}╚════════⋗{hong}⋗{tim}⋗ ')
clear()

try:
    if chon == '1':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/main_tds.py').text
    elif chon == '2':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/main_ttc.py').text
    elif chon == '3':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/main_page.py').text
    elif chon == '4':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/main_tienich.py').text
    elif chon == '5':
        code = requests.get('https://damhuuphuoc.io.vn/zefoy.php').text
    elif chon == '6':
        code = requests.get('https://damhuuphuoc.io.vn/getoken.php').text
    elif chon == '7':
        code = requests.get('https://raw.githubusercontent.com/FRIVE-SERVER/Python/main/server/thoat.py').text
except:
    if not network():
        print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
    else :
        print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
    exit()

exec(code, globals())