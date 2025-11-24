string = input("Enter a string: ")
reversed = ""

for item in range(len(string) -1, -1, -1):
    reversed += string[item]
print(reversed)


