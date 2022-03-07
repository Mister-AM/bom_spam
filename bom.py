import requests
import time,os,sys,time,requests
from time import sleep

#subrek oiiii ngambil doang

#Script yang gua buat kagak pernah gua endcrypt atau marsal
#jadi open sourse
a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

#logo
os.system('clear')
print ('\033[36mSubscribe yt ku ngab \033[37mMisterAM \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCXk4vbvDl7i6dxWBtNdpx6w')
sleep(4)
os.system('clear')
print ('\033[36mJoin Grub \033[37mDark Cyber')
os.system('termux-open-url https://cararegistrasi.com/bvC8MF')
sleep(3)
os.system('clear')
banner= """
\033[33m ____                         \033[36m ____   ___  __  __
\033[33m/ ___| _ __   __ _ _ __ ___   \033[36m| __ ) / _ \|  \/  |
\033[33m\___ \| '_ \ / _` | '_ ` _ \  \033[36m|  _ \| | | | |\/| |
\033[33m ___) | |_) | (_| | | | | | | \033[36m| |_) | |_| | |  | |
\033[33m|____/| .__/ \__,_|_| |_| |_| \033[36m|____/ \___/|_|  |_|
\033[33m      |_|
\033[32m[•]───────────────────────────────────────────[•]
\033[32m | \033[94m[+]  \033[32mAuthor  : \033[35mMisterAM                    \033[32m |
\033[32m | \033[33m[+]  \033[32mTEAM    : \033[33mDARK CYBER HUNTER           \033[32m |
\033[32m | \033[35m[+]  \033[32mChanel  : \033[35mMister A.M                  \033[32m |
\033[32m[•]───────────────────────────────────────────[•]"""
os.system('clear')
print (banner)

print ('\033[33m')
print ('\033[31mNomor awali dari : \033[94m 8xxxx')


#Run nomor

nomor = input(' \033[33mNomor target lu :\033[90m ')
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
     print (' \033[32m[√] \033[94mspam berhasil ngab :) ')
else:
     print (' \033[31m[¡] \033[94mspam gagal ngab :( ')
