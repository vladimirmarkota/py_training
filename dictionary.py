dic = {"Queen": "Bohemian Rhapsody",
       "Bee Gees": "Stayin' Alive",
       "U2": "One",
       "Michael Jackson": "Billie Jean",
       "The Beatles": "Hey Jude",
       "Bob Dylan": "Like A Rolling Stone"}

print(len(dic))

for key in dic.keys():
    print(key)


for value in dic.values():
    print(value)


for key, value in dic.items():
    print(key + " - " + value)


if dic.get("Promise of the Real"):
    print(dic.get("Promise of the Real"))
else: print("not found")
#ILI
print(dic.get("Promise of the Real", "That is not found"))
