# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
for _ in range(int(input())):
    line = input().split()
    item_name = ' '.join(line[:-1])
    net_price = int(line[-1:][0])
    if item_name in items:
        items[item_name] += net_price
    else:
        items[item_name] = net_price

for item in items:
    print(item, items[item])

############

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

items = OrderedDict()
for _ in range(int(input())):
    *name,net_price = input().split()
    item_name = ' '.join(name)
    items[item_name] = items.get(item_name, 0) + int(net_price)

for item, price in items.items():
    print(item, price)