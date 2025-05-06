file = open("C:/Users/Stewie/Desktop/stuff/Python OOP/BASICS AND DSA/dsaPython/File Handling/notes.txt", "r")
# command to read the file is file.read()
cont = file.read()

print(cont)
file.close

print("__________________________")

# reading  a file in binary mode
file = open("C:/Users/Stewie/Desktop/stuff/Python OOP/BASICS AND DSA/dsaPython/File Handling/notes.txt", "rb")
# command to read the file is file.read()
cont = file.read()

print(cont)
file.close