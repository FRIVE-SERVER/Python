import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
from sys import platform
from pystyle import Write,Colors
dem=0
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

def idelay(self, p):
        while(p>1):
            p=p-1
            print(f'{trang}[{do}WAITING{trang}][{xanhbien}X{trang}....][{vang}{p}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}WAITING{trang}][.{xanhbien}X{trang}...][{vang}{p}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}WAITING{trang}][..{xanhbien}X{trang}..][{vang}{p}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}WAITING{trang}][...{xanhbien}X{trang}.][{vang}{p}{trang}]','     ',end='\r');sleep(1/6)
            print(f'{trang}[{do}WAITING{trang}][....{xanhbien}X{trang}][{vang}{p}{trang}]','     ',end='\r');sleep(1/6)
def frive(so):
	a= f"{hong}────"*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.003)
	print()
class Facebook:
	def __init__(self,cookie):
		self.cookie = cookie
		self.headers = {
			'authority': 'mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
			'cache-control': 'max-age=0',
			'cookie': cookie,
			'origin': 'https://www.facebook.com',
			'referer': 'https://www.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			}
	def get_thongtin(self):
		try:
			home = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = cookie.split('c_user=')[1].split(';')[0]
			print(f'{luc}NAME: {vang}{ten} {do}| {luc}UID: {vang}{self.user_id} ', end='')
			sys.stdout.flush()
			return self.user_id
		except:
			print(f'{do}GET THÔNG TIN THẤT BẠI')
			return 0
	def get_pro5(self):
		headers={
           	     'authority': 'www.facebook.com',
            	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          	      'accept-language': 'vi',
       	         'cookie': self.cookie,
           	     'sec-ch-prefers-color-scheme': 'light',
            	    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            	    'sec-ch-ua-mobile': '?0',
          	      'sec-ch-ua-platform': '"Windows"',
          	      'sec-fetch-dest': 'document',
           	     'sec-fetch-mode': 'navigate',
           	     'sec-fetch-site': 'none',
           	     'sec-fetch-user': '?1',
             	   'upgrade-insecure-requests': '1',
           	     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            	    'viewport-width': '1366',
          	 	 }
		data ={
					'av':self.user_id,
					'fb_dtsg':self.fb_dtsg,
					'jazoest':self.jazoest,
					'fb_api_caller_class':'RelayModern',
					'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
					'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
					'server_timestamps':'true',
					'doc_id':'8179507702122101',
				}
		try:
			a=requests.post('https://www.facebook.com/api/graphql/', headers=headers,data=data).json()
			get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
			tong = get['count']
			data_pro5 = get['nodes']
			print(f'\n{luc}BẠN CÓ {vang}{tong} {luc}PAGE PROFILE')
			return data_pro5
		except:
			print(f'\n{do}KHÔNG GET ĐƯỢC PAGE ')
			return 0
	def chap_nhan(self, id_moi, id_page, name):
		headers = {
	    "Host": "www.facebook.com",
	    "content-length": "1368",
	    "sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"",
	    "sec-ch-ua-mobile": "?0",
	    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
	    "viewport-width": "980",
	    "content-type": "application/x-www-form-urlencoded",
	    "x-fb-lsd": "DlCuUH2d6LEfs4R3HXWyCL",
	    "x-fb-friendly-name": "ProfilePlusCometAcceptOrDeclineAdminInviteMutation",
	    "sec-ch-prefers-color-scheme": "dark",
	    "sec-ch-ua-platform": "\"Linux\"",
	    "accept": "*/*",
	    "origin": "https://www.facebook.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://www.facebook.com/profile.php?id\u003d100087892570045\u0026notif_id\u003d1670335596145290\u0026notif_t\u003dprofile_plus_admin_invite\u0026ref\u003dnotif",
	    "accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5",
	    "cookie": self.cookie
	  }
		data={
		'av': self.user_id, 
		'__user': self.user_id,
		'__a':'1',
		'__dyn':'7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e0ykdwSxucyUco5S3O2Saxa1NwJwpUe8hwaG0Z82_CxS320om78bbwto886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUy2a0SEuBwJCwLyESE2KwwwOg2cwMwhF8-4UdUcobUak1xwJwxw',
		'__csr':'gjYmwDPV5kCL4_fcx5FjFbcwBRb4jIHiO_8zEAzFuCWSGtiSSCmyeLiSqqF6RiWAFKh5l4XQ9J29oFGVrKcKEnApUC9qCWUS-8ADhEO6ojxah3miez8XyEVa6p9FWDUPzECbCxC7rCwMwyy48CzobVofkueCwNBAx-8g6CEpguxC322e2qUbFEvypoW5Edozxm3O0y88EkxK9yE25Gmdwo88EaUrwJzU9U2mx66oSfxe6oJw0QRw0-ew0aou0vd04zw4Xw1h-0yE1XQ02ruu07jE0SwE06320l-1fg0wK0c_wpE2Gw7Kw',
		'__req':'n',
		'__hs':'19332.HYP:comet_pkg.2.1.0.2.1',
		'dpr':'2',
		'__ccg':'GOOD',
		'__rev':'1006690336',
		'__s':'pg8xvj:d1f9pk:2fmmqb',
		'__hsi':'7174038987510665339',
		'__comet_req':'15',
		'fb_dtsg':self.fb_dtsg,
		'jazoest':self.jazoest,
		'lsd':'DlCuUH2d6LEfs4R3HXWyCL',
		'__aaid':'775223720487728',
		'__spin_r':'1006690336',
		'__spin_b':'trunk',
		'__spin_t':'1670336115',
		'fb_api_caller_class':'RelayModern',
		'fb_api_req_friendly_name':'ProfilePlusCometAcceptOrDeclineAdminInviteMutation',
		'variables':'{"input":{"client_mutation_id":"1","actor_id":"'+self.user_id+'","is_accept":true,"profile_admin_invite_id":"'+str(id_moi)+'","user_id":"'+id_page+'"},"scale":2}',
		'server_timestamps':'true',
		'doc_id':'6535667269801310',
	}
		try:
			chapnhan = requests.post('https://www.facebook.com/api/graphql/', headers = headers, data =data).json()
			check=chapnhan['data']['accept_or_decline_profile_plus_admin_invite']['comet_profile_banner']['notice']['title']['text']
			print(f'{trang}[{vang}{dem}{trang}] {do}| {luc}CHẤP NHẬN QUYỀN QUẢN TRỊ THÀNH CÔNG')
		except:
			print(f'{trang}[{vang}{dem}{trang}] {do}| {luc}CHẤP NHẬN QUYỀN QUẢN TRỊ THẤT BẠI ')
	def set_admin(self, id, mk, id_page, name):
		cookie = self.cookie
		ck_pro5 = cookie + '; i_user=' + id_page + ';'
		headers_1 = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/settings/?tab=profile_access',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1074',
            'x-fb-friendly-name': 'ProfilePlusMarkReauthedMutation',
            'x-fb-lsd': 'ywHjyvroP8nBIwLKTYWKxO',
            'cookie': ck_pro5,
        }
		data_1 = {
            'av': id_page, 
            '__user': id_page,
            '__a': '1',
            '__dyn': '7AzHxqU5a5Q1ryUqxenFw9uu2i5U4e0ykdwSwAyUco2qwJxS1NwJwpUe8hw6vwb-q7oc81xoswaq221FwgolzUO0n2US2G5Usw9m1YwBgK7o884y0Mo5W3S1lwlE-UqwsUkxe2GewGwsoqBwJK2W5olwUwlu5o4q0GpovUaU3VBwJCwLyES0Io5d08O321bwzwTwNwLwFg667EW26',
            '__csr': 'nf1ld2JWTf4SHVBJ7m8V9fl7LV8WUGbjAHnAmFpKmGiCKrUB7yF8y4Hh4bBK8BDWUohbLBzkdxivUG2aQaBzEgF28hyp8zxi5E9EGcGp162a3eA2udwMzXzokyo7e2a1Rx62-3C4ocEhU6e5oC8yUK8Bws9E5S4Gwb21dwp8sw6gwvUbU2ew920LU1zo5m1fw0Fjw1n-2K00PtE0kIw1pha7A27g0udg04CR00wixW0oy15w7Sg0lPzEkG1zw1b102bE',
            '__req': 'm',
            '__hs': '19328.HYP:comet_plat_default_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'GOOD',
            '__rev': '1006673379',
            '__s': 'obqdxp:ldjxfi:qlyl0z',
            '__hsi': '7172443321293327429',
            '__comet_req': '1',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': 'ywHjyvroP8nBIwLKTYWKxO',
            '__spin_r': '1006673379',
            '__spin_b': 'trunk',
            '__spin_t': '1669964595',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfilePlusMarkReauthedMutation',
            'variables': '{"input":{"password":{"sensitive_string_value":"'+str(mk)+'"},"actor_id":"'+str(id_page)+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5048033918567225',
        }
		try:
			nhap_mk = requests.post('https://www.facebook.com/api/graphql/', headers = headers_1, data =data_1).json()
			check = nhap_mk['data']['admin_management_mark_reauthed']['reauth_is_successful']
			if str(check) == 'True' or str(check) == 'true':
				pass
			else:
				print(f'{do}MẬT KHẨU SAI')
				return 0
		except:
			print(f'{do}XÁC MINH MẬT KHẨU THẤT BẠI, CÓ THỂ ACC BẠN ĐÃ BỊ BLOCK !!')
			return 0
		headers={
			'Host':'www.facebook.com',
			'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile':'?0',
			'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			'viewport-width':'980',
			'content-type':'application/x-www-form-urlencoded',
			'x-fb-lsd':'bTS-BmlWblhR0XQU4HNRbo',
			'x-fb-friendly-name':'ProfilePlusCoreAppAdminInviteMutation',
			'sec-ch-ua-platform':'"Linux"',
			'sec-ch-prefers-color-scheme':'dark',
			'accept':'*/*',
			'origin':'https://www.facebook.com',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
			'referer':'https://www.facebook.com/settings/?tab=profile_access',
			'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
			'cookie':ck_pro5
		}
		data ={
			'av':id_page,
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoest,
			'fb_api_caller_class':'RelayModern',
			'fb_api_req_friendly_name':'ProfilePlusCoreAppAdminInviteMutation',
			'variables':'{"input":{"additional_profile_id":"'+id_page+'","admin_id":"'+id+'","admin_visibility":"Unspecified","grant_full_control":true,"actor_id":"'+id_page+'","client_mutation_id":"2"}}',
			'server_timestamps':'true',
			'doc_id':'5632879080105060',
			'fb_api_analytics_tags':'["qpl_active_flow_ids=30605361"]'
	}
		try:
			set=requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
			if id in set.text:
				data_id_moi = set.json()['data']['profile_plus_core_admin_invite']['profile_with_biz_tools']['outgoing_core_app_admin_invites']
				for x in data_id_moi:
					id_admin = x['admin_profile']['id']
					name_admin = x['admin_profile']['name']
					if id_admin == id:
						id_moi= x['profile_admin_invite_id']
						break
				print(f'{trang}[{vang}{dem}{trang}] {do}| {luc}NAME{trang}: {xanhbien}{name} {do}| {luc}UID{trang}: {vang}{id_page}{trang} {do}| {luc}NAME ADMIN{trang}: {vang}{name_admin} {do}| {vang}{id}] {do}| {luc}SUCCESS')
				return id_moi
			else:
				print(f'{trang}[{vang}{dem}{trang}] {do}| {luc}NAME{trang}: {xanhbien}{name} {do}| {luc}UID{trang}: {vang}{id_page}{trang} {do}| {luc}ADMIN{trang}: {vang}{id} {do}| {luc}ERROR')
		except:
			print(f'{trang}[{vang}{dem}{trang}] {do}| {luc}NAME{trang}: {xanhbien}{name} {do}| {luc}UID{trang}: {vang}{id_page}{trang} {do}| {luc}ADMIN{trang}: {vang}{id} {do}| {luc}ERROR')
		return 'None'
while True:
	while True:
		cookie=input (f'{xanhbien}NHẬP COOKIE NICK CẦM PAGE PROFILE{trang}: ')
		mk = input (f'{xanhbien}NHẬP MẬT KHẨU NICK CẦM PAGE PROFILE{trang}: ')
		fb = Facebook(cookie)
		frive(14)
		a=fb.get_thongtin()
		if a == 0:
			continue
		data_pro5 = fb.get_pro5()
		frive(14)
		if data_pro5 == 0:
			continue
		else:
			break
	chon = input(f'{xanhbien}BẠN CÓ MUÔN AUTO CHẤP NHẬN QUYỀN QUẢN TRỊ KHÔNG {trang}[{xnhac}Y/N{trang}]{trang}: ')
	if chon == 'y':
		while True:
			cookie=input (f'{xanhbien}NHẬP COOKIE CẦN SET ADMIN{trang}: ')
			fb2 = Facebook(cookie)
			frive(14)
			id=fb2.get_thongtin()
			if id == 0:
				continue
			else:
				print()
				break
	else:
		id = input (f'{xanhbien}NHẬP ID NICK CẦN SET ADMIN{trang}: ')
	dl = int(input(f'{xanhbien}NHẬP DELAY{trang}: '))
	for x in data_pro5:
		id_page=x['profile']['id']
		name=x['profile']['name']
		dem+=1
		id_moi=fb.set_admin(id, mk, id_page, name)
		if id_moi == 0:
			break
		if chon == 'y' and id_moi != 'None':
			fb2.chap_nhan(id_moi, id_page, name)
		
		idelay(dl)