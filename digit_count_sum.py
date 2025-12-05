str1 = "PYnative29@#8496"
result = 0
count = 0

for char in str1:
    if char.isdigit():
        result = result + int(char)
        count = count + 1

average_res = round((result / count),2)
print(f"Zbroj je: {result} a average: {average_res}")
