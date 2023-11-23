items = [
    {'product': 'camisa',
    'price': 100,
    },
    {'product': 'pantalones',
    'price': 200,
    },
    {'product': 'pantalones 2',
    'price': 300,
    }
]

prices = list(map(lambda item: item['price'], items))

print(prices)

def add_taxes(item):
    item_copy = item.copy()
    item_copy['taxes'] = item_copy['price'] * 0.19
    return item_copy
new_items = list(map(add_taxes, items))

print('New items')
print(new_items)
print('Old items')
print(items)