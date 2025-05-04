# can be achieved by file.read() whuch read the entire file

# example of reading a file in python

file = open("notes.txt", "r") # open the file in read mode
data = file.read() # read the entire file
print(data) # print the data    
file.close() # close the file

# if the 