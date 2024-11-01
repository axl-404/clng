#--[ DECODE BY - ERRORxLMNx9 ]
#--[ JOIN - t.me/DARK_TEAM_LMNx9 ]

import requests
import random
import os
import sys
import time
from random import randint
from user_agent import generate_user_agent
from getuseragent import UserAgent
import pyfiglet
import webbrowser
os.system('xdg-open https://t.me/DARK_TEAM_LMNx9')
os.system('pip install pyfiglet')
os.system('pip install requests')
os.system('pip install webbrowser')
os.system('pip install user_agent')
os.system('pip install getuseragent')
os.system('clear')

print(pyfiglet.figlet_format('ig likes'))

def to(s):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0625)

to('\n\x1b[31;m TOOL >> \x1b[1;36mFREE IG LIKES FOR EVERYONE\n\x1b[1;31m DEVELOPER >>\x1b[1;33m @crazy_hacker404 \n\x1b[31;m JOIN >> \x1b[1;36m @xSPY_TEAM  \n')

ua = UserAgent('ios')
Random = random.randint(100000, 999999)

user = input('[+] InstaGram UserName : ')
link = input('[+] Post Link : ')

print('')

res = requests.post('https://api.likesjet.com/freeboost/7', json={
    'instagram_username': user,
    'link': link,
    'email': f'{Random}@gmail.com'
}, headers={
    'Host': 'api.likesjet.com',
    'content-length': '137',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'user-agent': ua.generate_user_agent(),
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://likesjet.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://likesjet.com/',
    'accept-language': 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5'
})

print(res.json()['message'])
print('\x1b[32;m DEVELOPER IS ONLY @CRAZY_HACKER404.')


#---[ FUCKED BY - ERRORxLMNx9 ]

