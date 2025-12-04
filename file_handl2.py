filename = "output.txt"
textt = "hello pynative"

try:
    with open(filename, "w") as file:
        file.write(textt)
    print(f"successfuly written {textt} to {filename}")
except Exception as e:
    print(f"An error occured: {e}")
