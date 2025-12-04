prev = 0
cur = 0

for i in range(11):
    sum = prev + cur
    print(f"Current num {cur} + Previous num {prev} su {sum}")
    cur = i
    prev = cur - 1

