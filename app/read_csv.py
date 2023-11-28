# import csv
# def read_csv(path):
#     with open(path, 'r') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             print('***'*5)
#             print(row)
# if __name__ == '__main__':
#     read_csv('./app/data.csv')
    
    
import csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
            
if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])