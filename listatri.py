l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l4 = []
l3 = []
l5 = []

for i in l1:
    if l1.index(i) % 2 == 1:
        l3.append(i)

for i in l2:
    if l2.index(i) % 2 == 0:
        l4.append(i)

l5 = l3 + l4
print(l5)


