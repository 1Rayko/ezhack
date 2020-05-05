#!/usr/bin/python3

# Examples:
# md5: fc5e038d38a57032085441e7fe7010b0 = helloworld
# sha256: 3fc9b689459d738f8c88a3a48aa9e33542016b7a4052e001aaa536fca74813cb = something
# sha512: 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043 = hello

from sys import argv
from hashlib import sha256, sha512, md5

# chmod +x main.py
# ./main.py md5 hash.txt rockyou.txt

line = "----------------------------------"

try:
	hashAlgr,fileHash,fileDict = argv[1],argv[2],argv[3]
except IndexError:
	print("Error: Arguments!")
	raise SystemExit

with open(fileHash) as file:
	hashFunc = file.read()
	hashFunc = hashFunc.replace('\n','')

def generator(string):
	for word in string:
		passwd = word.replace('\n','')
		if encrypt(passwd) == hashFunc:
			yield line +"\n[True]: "+passwd
			return
		else:
			yield "[False]: "+passwd

def encrypt(string):
	passwd = string.encode()
	if hashAlgr == "md5":
		signature = md5(passwd).hexdigest()
	elif hashAlgr == "sha256":
		signature = sha256(passwd).hexdigest()
	elif hashAlgr == "sha512":
		signature = sha512(passwd).hexdigest()
	else: raise SystemExit
	return signature

print(line)
with open(fileDict, errors = "ignore") as dictionary:
	for password in generator(dictionary):
		print(password)
print(line)