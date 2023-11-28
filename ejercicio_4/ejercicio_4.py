import csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        sum = { key: value for key, value in reader}
        total = 0
        for valor in sum.values(): 
             total += int(valor)
        return int(total)


response = read_csv('./data.csv')
print(response)