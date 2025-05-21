# writing to a file is done using file.write() method

file = open("C:/Users/Stewie/Desktop/stuff/Python OOP/BASICS AND DSA/dsaPython/File Handling/notes.txt", "w") # open the file in write mode

cont = file.write("This is a test file") # write to the file
# print(cont) 
file.close() 