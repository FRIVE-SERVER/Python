import os,sys,requests,threading
from time import sleep
from datetime import datetime
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
dem = 0
listcx = []
list_page_pro5 = []
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")
# ====================== [ FUNCTION ] ======================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print(hong+'────────────────────────────────────────────────────────────')
def frive_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XX......{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXX.....{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXX....{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXX...{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXX..{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXXX.{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[{do}FRIVE{trang}][{xanhbien}XXXXXXXX{trang}][{vang}{o}{trang}]','     ',end='\r');sleep(1/6)
def tangcxstr(x, dem, linkstr, dataurlstr):
    camxuc = listcx[0]
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_page_pro5[x].split('|')[0]
    name_page = list_page_pro5[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': linkstr,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'useStoriesSendReplyMutation',
        'x-fb-lsd': '4CR-snjduLBRfA-cdgjhg_',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        '__a': '1',
        '__dyn': '7AzHxqU5a5Q1ryUbFuC0BVU98nwgU29zEdEc8co2qwJxS1Nw9m3y4o1DU2_CxS320om782Cwwwqo465o-cw5MKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewGwkUtxGm2SUbElxm0zK5pUfE2FBx_wHwfCm2Sq2-azo2NwkQ0z8c84qifxe3u362-2B0oobo8o',
        '__csr': 'gP4nezNiOqiaH9H5qlPP_vilnFSncKIJESBc_riHQiGRB_iIgRl3maBgy8mlXp9oLD-XggV8zhaGbLBCUnCx-eDAKm78pCxim2yfUoJ12UGcUC3au6UgG9K225opwyxG9wFgfFE4S0MEkwyxOfxK1fwqouw9G1RwPx-0Q82jwoU5C1Twai0d3w2MUvw1Jy3e05ro03l7w1JG01MRw0iY8W0I81bU1G81zE0hZxC0D8',
        '__req': 'r',
        '__hs': '19325.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1006641324',
        '__s': 'vcrj03:a4aoft:01km45',
        '__hsi': '7171454504668598048',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '4CR-snjduLBRfA-cdgjhg_',
        '__aaid': '497084035286445',
        '__spin_r': '1006641324',
        '__spin_b': 'trunk',
        '__spin_t': '1669734368',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useStoriesSendReplyMutation',
        'variables': '{"input":{"attribution_id_v2":"StoriesCometSuspenseRoot.react,comet.stories.viewer,via_cold_start,1669734368520,55579,,","lightweight_reaction_actions":{"offsets":[0],"reaction":"'+str(camxuc)+'"},"message":"'+str(camxuc)+'","story_id":"'+str(dataurlstr)+'","story_reply_type":"LIGHT_WEIGHT","actor_id":"100088148974138","client_mutation_id":"2"}}',
        'server_timestamps': 'true',
        'doc_id': '4826141330837571',
    }

    runtanglikestr = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    if 'data' in runtanglikestr:
        print(f'{trang}['+vang+str(dem)+trang+'] | '+vang+str(time)+trang+f' | {xanhbien}SUCCESS {trang}| '+vang+str(uid_page)+trang+' | '+vang+str(name_page)+trang+' | '+vang+str(camxuc)+trang+' | '+vang+str(dataurlstr)+trang+' ')
    else:
        print(do+'TĂNG CẢM XÚC THẤT BẠI')
# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================
clear()
cookie = input(f'{luc}NHẬP COOKIE FACEBOOK{trang}: ')
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
}
    
try:
    print("Đang Check Live Cookie...", end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    exit("COOKIE DIE OR OUT")

headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_page_pro5.append(gomlist)
# NHẬP THÔNG SỐ ĐỂ CHẠY TOOL
clear()
print(f'{xnhac}ĐÃ TÌM THẤY '+vang+str(len(list_page_pro5))+xnhac+' PAGE PRO5')
thanh()
linkstr = input(f'{luc}NHẬP LINK STORY{trang}: ')
# TÁCH DATA TRONG URL STR
dataurlstr = linkstr.split('/')[5].split('/?')[0]
# GET THÀNH CÔNG
thanh()
print(f'{xanhbien}SUCCESS ID: '+vang+str(dataurlstr)+trang+'')
thanh()
print(xnhac+'[1 : LIKE — 2 : LOVE — 3 : CARE — 4 : HAHA]')
print(xnhac+'     [5 : WOW — 6 : SAD — 7 : ANGRY]')
thanh()
cx = int(input('Vui Lòng Nhập Lựa Chọn: '))
if cx == 1:
    listcx.append('👍')
if cx == 2:
    listcx.append('❤️')
if cx == 3:
    listcx.append('🤗')
if cx == 4:
    listcx.append('😆')
if cx == 5:
    listcx.append('😮')
if cx == 6:
    listcx.append('😢')
if cx == 7:
    listcx.append('😡')
thanh()
soluongcx = int(input(f'{luc}SỐ REACTION CẦN TĂNG{trang}: '))
thanh()
delay = int(input(f'{luc}NHẬP DELAY REACTION{trang}: '))
thanh()
while True:
    for x in range(int(len(list_page_pro5))):
        dem=dem+1
        threading.Thread(target=tangcxstr,args=(x, dem, linkstr, dataurlstr, )).start()
        frive_delay(delay)
        if dem == soluongcx:
            thanh()
            input(f'{xanhduong}DONE {soluongcx} REACTION </> ENTER ĐỂ EXIT')
            exit()