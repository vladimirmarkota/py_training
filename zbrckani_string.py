prvi = "abc"
drugi = "xyz"

prvi_len = len(prvi)
drugi_len = len(drugi)

lenght = prvi_len if prvi_len > drugi_len else drugi_len
result = ""

drugi = drugi[::-1]

for char in range(lenght):
    if char < prvi_len:
        result = result + prvi[char]
    if char < drugi_len:
        result = result + drugi[char]

print(result)
