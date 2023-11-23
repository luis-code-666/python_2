import mod

data = [
    {
        'country': 'Colombia',
        'population': 500  
    },
    {
        'country': 'Bolivia',
        'population': 300  
    }
]

def run():
    keys,values = mod.get_opulation()
    print (keys,values)


    contry = input('Type Contry => ')

    result =  mod.population_by_country(data, contry)
    print (result)

if __name__ == '__main__':
    run()