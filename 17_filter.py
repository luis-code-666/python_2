numbers=[1, 2, 3, 4, 5]
new_numbers=list(filter(lambda item: item%2==0, numbers))
print(new_numbers)