try:
    a = float(input("unesi prvi: "))
    b = float(input("unesi drugi: "))

    if b == 0:
        print("nazivnik ne moze biti 0")
    else:
        x = (a / b) * 100
        print(f"The percentage is: {x:.2f}%")

except ValueError:
    print("Invalid input")