with open("test.txt", "w") as file:
    file.write("I am learning file handling!")

with open("test.txt", "r") as file:
    content = file.read()

print(content)