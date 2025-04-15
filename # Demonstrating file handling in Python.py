# Demonstrating file handling in Python

with open("example.txt", "w") as file:
    file.write("Hello, file handling!")

with open("example.txt", "r") as file:
    print(file.read())