score = int(input("unesi score: "))

if score >= 90:
    print("odlican 5")
else:
    if score >= 80:
        print("vrlo dobar 4")
    else:
        if score >= 70:
            print("dobar 3")
        else:
            if score >= 60:
                print("dovoljan 2")
            else:
                print("nedovoljan 1")

# elif

bodovi = int(input("bodovi: "))
if bodovi >= 90:
    print("odlican 5")
elif bodovi >= 80:
    print("vrlo dobar 4")
elif bodovi >= 70:
    print("dobar 3")
elif bodovi >= 60:
    print("dovoljan 2")
else: print("nedovoljan 1")

