from collections import OrderedDict

n = int(input('How Many N?:'))
order = OrderedDict()

for i in range(n):
    name, price = input('Product name and volume separate by a space:').rsplit(' ', 1)
    price = int(price)

    if name in order:
        order[name] += price
    else:
        order[name] = price

print('\n'.join(f"{key} {value}" for key, value in order.items()))
