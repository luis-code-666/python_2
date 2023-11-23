import functools

numbers = [1, 2, 3, 4]
result = functools.reduce(lambda conter, item: conter + item, numbers)
print(result)
print('//////////////////')


def acum (conter, item):
    
    print('conter == ',  conter)
    print('conter == ',  item)
    return conter + item

result = functools.reduce(acum, numbers)
print(result)