a = ["Alice", "Bob", "Charlie"]
b = [85, 92, 78]

print(f"{"name"} {"score"}")
print("-" * 15)
for name, score in zip(a, b):
    print(f"{name:10} -> {score:5}")
