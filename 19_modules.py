import sys
print(sys.path)


import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi nuemero de la suerte es 3'
result = re.findall('[0-9]+',  text)
print(result)


import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
resul = time.asctime(local)
print(resul) 


import collections
number = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(number)
print(counter)