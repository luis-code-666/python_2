with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')

# las read (r) para leer  write (w) para escribir y el (r+) para ambos casos de escribir y leer pero si le colocamos el (w+) tambien tiene los permisos de escribir y leer la desventaja que es de lo  que sobrescribe osea si hay algo en el txt borra eso y coloca lo que estmos enviando por el codigo 
