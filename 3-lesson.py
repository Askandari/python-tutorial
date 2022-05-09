print('hello world')
print(2 ** 8)
lumberjack='okay'
print(lumberjack)
print('Spam!' * 8)
import os
print (os.getcwd())
import this
for x in 'spam':
	print(x)
	print('done')

import script1
import script1
from importlib import reload
reload(script1)
import mylife #выполнить файл и загрузить модуль целиком
print (mylife.title) #Использовать .атрибут
print ('ogo') #Просто попробовал вывести случайное слово
import imp #Перед imp.reload(...) нужно писать команду "import imp", хотя терминал и будет выдавать текст о устаревании команды "imp" и замене её на "impotlib"
imp.reload(script1) #импортируем сценарий script1
from script1 import y #в файле script1 у нас переменная "у" с значением (2**8) - тут извлекаем это значение с помощью from ..
from importlib import reload
reload(mylife)
print (mylife.title)
import imp
imp.reload(script1)
print(script1.x)
import mylife          #Первое - иморт модуля: КАКОЙ
print (mylife.title)   #Второе - иморт .атрибута: ЧТО ИМЕННО
import imp
imp.reload(mylife)
print(mylife.title)
import threenames
print (threenames.b, threenames.c)
from threenames import a, b, c # ОТКУДА, ЧТО
print(c) # ЧТО из этого вывести
import imp
imp.reload(threenames)
dir(threenames)
exec(open('script1.py').read())
