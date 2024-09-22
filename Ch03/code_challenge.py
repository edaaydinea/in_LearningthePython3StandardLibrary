# Python code​​​​​​‌​‌‌‌‌​​‌​‌‌‌‌​​‌​‌‌‌​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_words(file_path):
    with open(file_path, 'r') as file:
        return len(file.read().split())

def create_file(file_path, contents):
    with open(file_path, 'w') as file:
        file.write(contents)