def izr(n):
    if n < 0:
        print("negative number")
    elif n == 0:
        return 1
    else:
        return n * izr(n - 1)


n = 6
res = izr(n)
print(f"Faktorijela broja {n} je {res}")

