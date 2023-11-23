try:
    print(0/0)
    age = 10
    assert 1!=1, "Uno no es igual que uno"
    if age < 18:
        raise Exception("Nose permite menores de edad")
except ZeroDivisionError as error:
    print (error) 
except AssertionError as error:
    print (error)
except Exception as error:
    print (error)
    

print('Hola')