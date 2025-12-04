# Solution:
def count_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
char_count = count_characters("sample.txt")
print(f"Total characters in 'sample.txt': {char_count}")