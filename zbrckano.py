def brojac(str11):
    brojevi = 0
    simboli = 0
    slova = 0
    for char in str11:
        if char.isalpha():
            slova += 1
        elif char.isdigit():
            brojevi += 1
        else:
            simboli += 1
    print(f"Brojevi: {brojevi}, simboli: {simboli}, slova: {slova}")

str11 = "P@#yn26at^&i5ve"
print("total count of brojeva, simbola i slova \n")
brojac(str11)
