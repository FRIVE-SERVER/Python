from pystyle import Write,Colors
import json
import requests, os, sys, re, json
from time import sleep
from pystyle import Colors, Colorate
from datetime import datetime
import random
import time
import os
dem = 0
list=''

list_cookie = []
def coin(ckvp):
	h_xu = {'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36','cookie':ckvp}
	x = requests.post('https://vipig.net/home.php', headers=h_xu).text
	xu = x.split('"soduchinh">')[1].split('<')[0]
	return xu

def cookie(token):
	ck = requests.post('https://vipig.net/logintoken.php',headers={'Content-type':'application/x-www-form-urlencoded',},data={'access_token':token})
	cookie = 'PHPSESSID='+(ck.cookies)['PHPSESSID']
	return cookie
def get_nv(type, ckvp):
	headers={'content-type':'text/html; charset=UTF-8','accept':'application/json, text/javascript, */*; q=0.01','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','referer':'https://vipig.net/kiemtien/','x-requested-with':'XMLHttpRequest','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','cookie':ckvp}
	a = requests.post(f'https://vipig.net/kiemtien{type}/getpost.php', headers=headers).json()
	return a
def nhan_tien(list, ckvp, type):
	data_xu='id='+str(list)
	data_nhan=str(len(data_xu))
	headers={'content-length':data_nhan,'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','content-type':'application/x-www-form-urlencoded; charset=UTF-8','accept':'*/*','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','sec-ch-ua-mobile':'?1','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','origin':'https://vipig.net','sec-ch-ua-platform':'"Android"','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://vipig.net/kiemtien'+type+'/','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ckvp}
	a = requests.post(f'https://vipig.net/kiemtien{type}/nhantien.php',headers=headers,data=data_xu).text
	return a
def nhan_sub(list, ckvp):
	data_xu='id='+str(list[0:len(list)-1])
	data_nhan=str(len(data_xu))
	headers={'content-length':data_nhan,'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','content-type':'application/x-www-form-urlencoded; charset=UTF-8','accept':'*/*','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','sec-ch-ua-mobile':'?1','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','origin':'https://vipig.net','sec-ch-ua-platform':'"Android"','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://vipig.net/kiemtien/subcheo','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ckvp}
	a = requests.post('https://vipig.net/kiemtien/subcheo/nhantien2.php',headers=headers,data=data_xu).json()
	return a

def delay(dl):
  try:
    for i in range(dl, -1, -1):
       Write.Print('[FRIVE]['+str(i)+']                                                                ',Colors.blue_to_cyan,interval=0.0001,end='\r')
       sleep(1)
  except:
     sleep(dl)
     print(dl,end='\r')
     
	
def name(cookie):
	headers={'Host':'www.instagram.com','cache-control':'max-age=0','viewport-width':'980','sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
	a=requests.get('https://www.instagram.com/', headers=headers).text
	try:
		user = a.split('username')[1].split('\\"')[2]
		id = cookie.split('ds_user_id=')[1].split(';')[0]
		return user, id
	except:
		return 'die','die'
os.system("cls" if os.name == "nt" else "clear")
def bongoc(so):
	a = print("────"*so)
	Write.Print(f'',Colors.blue_to_cyan,interval=0.0001)
    
	
def like(id, cookie):
	headers = {"x-ig-app-id": "1217981644879628","x-asbd-id": "198387","x-instagram-ajax": "c161aac700f","accept": "*/*","content-length": "0","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19","x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],"x-requested-with": "XMLHttpRequest","cookie": cookie}
	like = requests.post(f'https://www.instagram.com/web/likes/{id}/like/',headers=headers).text
	if 'ok' not in like:
		return '1'
	else:
		return '2'
def get_id(link):
	headers = {"x-ig-app-id": "1217981644879628","x-asbd-id": "198387","x-instagram-ajax": "c161aac700f","accept": "*/*","content-length": "0","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19","x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],"x-requested-with": "XMLHttpRequest","cookie": cookie}
	try:
		a = requests.get(link, headers=headers).text
		id = a.split('media?id=')[1].split('"')[0]
		return id
	except:
		return False

def follow(id, cookie):
	headers = {"x-ig-app-id": "1217981644879628","x-asbd-id": "198387","x-instagram-ajax": "c161aac700f","accept": "*/*","content-length": "0","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19","x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],"x-requested-with": "XMLHttpRequest","cookie": cookie}
	fl = requests.post("https://i.instagram.com/web/friendships/"+id+"/follow/", headers=headers).text
	if 'ok' not in fl:
		return '1'
	else:
		return fl
def cmt(msg, id , cookie):
	headers = {"x-ig-app-id": "1217981644879628","x-asbd-id": "198387","x-instagram-ajax": "c161aac700f","accept": "*/*","content-length": "0","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19","x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],"x-requested-with": "XMLHttpRequest","cookie": cookie}
	cmt = requests.post(f'https://i.instagram.com/api/v1/web/comments/{id}/add/', headers=headers, data={'comment_text':msg}).json()
	try:
		cmt['status'] == 'ok'
		return 'ok'
	except:
		return cmt
		
	
def cau_hinh(id_ig, ckvp):
	headers={'content-length':'23','sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','accept':'*/*','content-type':'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with':'XMLHttpRequest','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://vipig.net/cauhinh/datnick.php','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':ckvp}
	a=requests.post('https://vipig.net/cauhinh/datnick.php', headers=headers, data={'iddat[]':id_ig}).text
	return a

while True:
	token = str(Write.Input('Nhập Access_Token Vipig: ',Colors.blue_to_cyan,interval=0.0001))
	#token = input('Nhập Access_Token Vipig: ')
	log = requests.post('https://vipig.net/logintoken.php', headers={'Content-type':'application/x-www-form-urlencoded'}, data={'access_token':token}).json()
	if log['status'] == 'success':
		user = log['data']['user']
		xu = log['data']['sodu']
		ckvp = cookie(token)
		Write.Print('Đăng Nhập Thành Công\n',Colors.blue_to_cyan,interval=0.0001)
		break
	elif log['status'] == 'fail':
		print(log['mess'])
bongoc(14)
x = 0
Write.Print('[LƯU Ý] Muốn Dừng Thì Nhấn Enter\n',Colors.blue_to_cyan,interval=0.0001)
while True:
	x = x +1
	cookie = str(Write.Input(f'Nhập Cookie Instagram Thứ {x}: ',Colors.blue_to_cyan,interval=0.0001))
	if cookie == '' and x > 1:
		break
	ten = name(cookie)
	if ten[0] != 'die':
		Write.Print(f'User Instagram: {ten[0]}\n',Colors.blue_to_cyan,interval=0.0001)
		list_cookie.append(cookie)
		bongoc(14)
	else:
		Write.Print('Cookie Instagram Sai ! Vui Lòng Nhập Lại !!! \n',Colors.blue_to_cyan,interval=0.0001)
		x = x-1
		bongoc(14)


Write.Print(f"""Tên Tài Khoản: {user}
Xu Hiện Tại: {xu}
Số Cookie: {len(list_cookie)}\n""",Colors.blue_to_cyan,interval=0.0001)
bongoc(14)
Write.Print("""[1 : LIKE — 2 : FOLLOW — 3 : COMMENT]
Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)\n""",Colors.blue_to_cyan,interval=0.0001)
chon = str(Write.Input('Nhập Số Để Chạy Nhiệm Vụ: ',Colors.blue_to_cyan,interval=0.0001))
bongoc(14)
dl = int(Write.Input('Nhập Delay: ',Colors.blue_to_cyan,interval=0.0001))
Write.Print('Sau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.',Colors.blue_to_cyan,interval=0.0001,end='\r')
chong_block = int(Write.Input('Sau ',Colors.blue_to_cyan,interval=0.0001))
Write.Print(f'Sau {chong_block} Nhiệm Vụ Nghỉ Ngơi ____ Giây       ',Colors.blue_to_cyan,interval=0.0001,end='\r')
delay_block = int(Write.Input(f'Sau {chong_block} Nhiệm Vụ Nghỉ Ngơi ',Colors.blue_to_cyan,interval=0.0001))
doi_acc = int(Write.Input('Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: ',Colors.blue_to_cyan,interval=0.0001))


while True:
	x = 0
	ngoctool=0
	if len(list_cookie) == 0:
		Write.Print('Toàn Bộ Cookie Đã Out Vui Lòng Nhập Lại !!\n',Colors.blue_to_cyan,interval=0.0001)
		while True:
			x = x + 1
			cookie = str(Write.Input(f'Nhập Cookie Instagram Thứ {x}: ',Colors.blue_to_cyan,interval=0.0001))
			if cookie == '' and x > 1:
				break
			ten = name(cookie)
			if ten[0] != 'die':
				Write.Print(f'User Instagram: {ten[0]} \n')
				list_cookie.append(cookie)
				bongoc(14)
			else:
				Write.Print('Cookie Instagram Sai ! Vui Lòng Nhập Lại !!! \n',Colors.blue_to_cyan,interval=0.0001)
				x = x - 1
				bongoc(14)
	for i in range(len(list_cookie)):
		if ngoctool == 2:
			break
		loi_like = 0
		loi_cmt = 0
		cookie = list_cookie[i]
		user = name(cookie)
		id_ig=user[1]
		if user[0] == 'die':
			Write.Print('Cookie Instagram Die !!!! \n',Colors.blue_to_cyan,interval=0.0001)
			list_cookie.remove(cookie)
			continue
		ngoc = cau_hinh(id_ig, ckvp)
		if ngoc == '1':
			bongoc(14)
			Write.Print(f'Đang Cấu Hình ID: {id_ig} | User: {user[0]}\n',Colors.blue_to_cyan,interval=0.0001)
			bongoc(14)
		else:
			Write.Print(f'Cấu Hình Thất Bại ID: {id_ig} | User: {user[0]} \n',Colors.blue_to_cyan,interval=0.0001)
			delay(3)
			list_cookie.remove(cookie)
			continue
		ngoctool=0
		while True:
			if ngoctool == 1 or ngoctool == 2:
				break
			if '1' in chon:
				get_like = get_nv('', ckvp)
				if len(get_like) == 0:
					Write.Print('Tạm Thời Hết Nhiệm Vụ Like     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				if len(get_like) != 0:
					Write.Print(f'Tìm Thấy {len(get_like)} Nhiệm Vụ Like     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				for x in get_like:
					link = x['link']
					uid = x['idpost']
					id = get_id(link)
					if id == False:
						continue
					lam = like(id, cookie)
					if lam ==  '1':
						user = name(cookie)
						if user[0] == 'die':
							Write.Print('Cookie Instagram Die !!!! \n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
							ngoctool=2
							break
						else:
							Write.Print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác {lam}\n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
							ngoctool=2
							break
					elif loi_like >= 4:
						Write.Print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác\n',Colors.blue_to_cyan,interval=0.0001)
						list_cookie.remove(cookie)
						ngoctool=2
						break
					elif lam == '2':
						nhan = nhan_tien(uid, ckvp, '')
						if 'mess' in nhan:
							xu=coin(ckvp)
							dem = dem + 1
							tg=datetime.now().strftime('%H:%M')
							Write.Print(f'[{dem}] | {tg} | LIKE | {id} | +300 | {xu}\n',Colors.blue_to_cyan,interval=0.0001)
							loi_like = 0
							if dem % chong_block == 0:
								delay(delay_block)
							else:
								delay(dl)
							if dem % doi_acc == 0:
									ngoctool=1
									break
						else:
							tg=datetime.now().strftime('%H:%M')
							Write.Print(f'[X] | {tg} | LIKE | {id} | ERROR \n',Colors.blue_to_cyan,interval=0.0001)
							loi_like += 1
							delay(dl)
						
			if ngoctool == 1 or ngoctool == 2:
				break
			if '2' in chon:
				get_sub = get_nv('/subcheo', ckvp)
				if len(get_sub) == 0:
					Write.Print('Tạm Thời Hết Nhiệm Vụ Follow     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				if len(get_sub) != 0:
					Write.Print(f'Tìm Thấy {len(get_sub)} Nhiệm Vụ Follow     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				for x in get_sub:
					id=x['soID']
					lam = follow(id, cookie)
					if lam == '1':
						if user[0] == 'die':
							Write.Print(f'Cookie Instagram Die !!!!  \n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
						else:
							Write.Print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác \n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
						ngoctool=2
						break
					data_id = open(f"{id_ig}.txt", "a+")
					data_id.write(str(id) + ',')
					dem = dem + 1
					tg=datetime.now().strftime('%H:%M')
					Write.Print(f'[{dem}] | {tg} | FOLLOW | {id} | SUCCESS\n',Colors.blue_to_cyan,interval=0.0001)
					data_id = open(f"{id_ig}.txt", "r")
					list = data_id.read()
					dem_sub = len(list.split(','))-1
					if dem % chong_block == 0:
						delay(delay_block)
					else:
						delay(dl)
					if dem_sub >= 6:
						nhan = nhan_sub(list, ckvp)
						try:
							xu_them = nhan['sodu']
							job = xu_them // 600
							xu=coin(ckvp)
							Write.Print(f'Nhận Thành Công {job} Nhiệm Vụ Follow | +{xu_them} | {xu}\n',Colors.blue_to_cyan,interval=0.0001)
						except:
							print(nhan)
						os.remove(f"{id_ig}.txt")
						dem_sub = 0
					if dem % doi_acc == 0:
								ngoctool=1
								break
			if ngoctool == 1 or ngoctool == 2:
				break
			if '3' in chon:
				get_cmt = get_nv('/cmtcheo', ckvp)
				
				if len(get_cmt) == 0:
					Write.Print('Tạm Thời Hết Nhiệm Vụ Comment     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				if len(get_cmt) != 0:
					Write.Print(f'Tìm Thấy {len(get_cmt)} Nhiệm Vụ Comment     ',Colors.blue_to_cyan,interval=0.0001,end ='\r')
				for x in get_cmt:
					link = x['link']
					uid = x['idpost']
					msg = random.choice(json.loads(x['nd']))
					id = get_id(link)
					if id == False:
						continue
					lam = cmt(msg, id, cookie)
					if lam ==  '1':
						user = name(cookie)
						if user[0] == 'die':
							Write.Print('Cookie Instagram Die !!!! \n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
							ngoctool=2
							break
						else:
							Write.Print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác \n',Colors.blue_to_cyan,interval=0.0001)
							list_cookie.remove(cookie)
							ngoctool=2
							break
					elif loi_cmt >= 4:
						Write.Print(f'Tài Khoản {user[0]} Đã Bị Chặn Tương Tác\n',Colors.blue_to_cyan,interval=0.0001)
						list_cookie.remove(cookie)
						ngoctool=2
						break
					elif lam == 'ok':
						nhan = nhan_tien(uid, ckvp, '/cmtcheo')
						if 'mess' in nhan:
							xu=coin(ckvp)
							dem = dem + 1
							tg=datetime.now().strftime('%H:%M')
							Write.Print(f'[{dem}] | {tg} | COMMENT | {id} | {msg} | +600 | {xu}\n',Colors.blue_to_cyan,interval=0.0001)
							loi_cmt = 0
							if dem % chong_block == 0:
								delay(delay_block)
							else:
								delay(dl)
							if dem % doi_acc == 0:
									ngoctool=1
									break
						else:
							tg=datetime.now().strftime('%H:%M')
							Write.Print(f'[X] | {tg} | COMMENT | {id} | ERROR\n',Colors.blue_to_cyan,interval=0.0001)
							loi_cmt += 1
							delay(dl)