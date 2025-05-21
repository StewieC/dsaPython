# its important to handle exceptions to ensure that files are closed properly

try:
    file = open("C:/Users/Stewie/Desktop/stuff/Python OOP/BASICS AND DSA/dsaPython/File Handling/notes.txt", "r")
    # command to read the file is file.read()
    cont = file.read()
    print(cont)

finally:
    file.close()