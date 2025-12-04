import io

filename = "output.txt"
apstr = "This is an appended line."

try:
    with open(filename, "a") as file:
        novi = file.write("\n" + apstr)
        print(f"Successfuly written {apstr} to {filename}")
except Exception as e:
    print(f"An error occured: {e}")

