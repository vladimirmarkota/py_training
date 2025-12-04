filename = "output.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(e)
