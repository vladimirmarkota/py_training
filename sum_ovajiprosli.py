previous = 0

for current in range(1, 11):
    total = previous + current
    print(f"current: {current}, previous: {previous}, sum: {total}")
    previous = current

