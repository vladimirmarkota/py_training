#user inputs int, while loop sums the ints from users input till 0

broj = int(input("upisi broj: "))
counter = 0

init = broj

while broj > 0:
    counter += broj
    broj -= 1

print("unesen: ", init)
print("zbroj: ", counter)
