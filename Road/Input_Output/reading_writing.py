#   open(filename, mode)
#   modes:  'r' - read only
#           'w' - for only writing (an existing file with the sam name will be erased)
#           'a' - open the file for appending ( any data is automatically added to the end)
#           'r+'- opens the file for both reading and writing 

#           It is good practice to use the with keyword when dealing with file objects. 
#           The advantage is that the file is properly closed after its suite finishes, 
#           even if an exception is raised at some point.

with open('adress.txt') as f:
    data_ = f.read()
    f.readline()
    list(f)
    f.readlines()

    for line in data_:
        print(line, end='')
    
f.closed

#   f.readline() returns an empty string, the end of the file has been reached
#   If you’re not using the with keyword, then you should call f.close()

new = open('workfile', 'rb+')
new.write(b'Hello world')