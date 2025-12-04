def print_info(**kwargs):
    if kwargs:
        print("---info---")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("No info provided")

print_info(Name = "Alice", Age = 30, City = "New York")
print_info(job="engineer", salary = 75000)
print_info()

