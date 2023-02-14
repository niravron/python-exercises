with open("sample.txt", "r") as file:
    content = file.read()

with open("sample-reverse.txt", "w") as file:
    file.write(content[::-1])