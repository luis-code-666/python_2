import random
countries=['col', 'mex', 'bol', 'pe']

population_v2={ country:random.randint(1, 100) for country in countries}
print(population_v2)


result = {country: population for (country, population) in population_v2.items() if population >50}
print(result)

text = 'Hola soy Luis'
unique = {c:c.upper() for c in text if c in 'aeiou'}
print(unique)

text = 'Hola soy Luis'
vocales = 'aeiou'
unique_vocales = {c.upper() for c in text if c in vocales}
count_vocales = len(unique_vocales)

print(f"Vocales únicas en mayúsculas: {unique_vocales}")
print(f"Total de vocales únicas: {count_vocales}")


print('////////////////////////////////')
text = 'Hola soy Luis'
vocales = 'aeiou'
vocal_counts = {}

for c in text:
    if c.lower() in vocales:
        if c.lower() in vocal_counts:
            vocal_counts[c.lower()] += 1
        else:
            vocal_counts[c.lower()] = 1

for vocal, count in vocal_counts.items():
    print(f"{vocal}: {count} veces")
    
    

