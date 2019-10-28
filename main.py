import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;              \TuanTayoV1/             ;
		;---------------------------------------------;
		; Author : TuanTayo                   ;
		; Contact Us  :                             ;
        ; cyber.tuantayo@gmail.com  ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		
- Pilih Salah Satu -
1. Analog Freeze
2. Auto LAG
3. AFK
""")
		pilih=int(input('/TuanTayo: '))
		if pilih == 1:
			import src.analog
		elif pilih == 2:
			import src.ping
		elif pilih == 3:
			import src.afk
		
	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
