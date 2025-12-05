def info(**kwargs):
    if kwargs:
        print("---info---")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("no info provided")

info(name="Vlado", age=25, city="Zagreb")
info()
