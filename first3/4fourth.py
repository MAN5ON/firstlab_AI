from collections import OrderedDict, Counter, defaultdict

n = int(input('How Many N?:'))
order = OrderedDict(input('key and value: ').split() for _ in range(n))
order1 = defaultdict(int)

for key, value in order.items():
    order1[key] += int(value)

c = Counter(order1)
for d in order1:
    c.update(d)
print(c)
