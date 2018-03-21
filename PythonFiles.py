#Next reading files from input streams##
from pathlib import Path ##is_file, is_dir and so on so forth
file_="TBD.txt"

##file open operation: open() method

    ##Modes of opening files:
        #r-read
        #w-write (any existing files with the same name will be erased when this mode is activated) 
        #a-append
        #r+-Both read and write


write_handle=open("C:\\Users\\Sai\\Documents\\py\\TBD_1.txt","w")
write_handle.write("Hello This is my first line of python in a file\n")
###Close is mandatory for the write to complete, i.e for the buffered writes will be flushed to disk
write_handle.close()

append_handle=open("C:\\Users\\Sai\\Documents\\py\\TBD_1.txt","a")
print("File handle opened for the file: ",file_," and its value is: ",append_handle)
append_handle.write("And I am going to gift her something! for sure!\n")
append_handle.close()

##read handle##
##open(file, mode, buffering, encoding, errors, newline, closefd, opener)##
read_handle=open("C:\\Users\\Sai\\Documents\\py\\TBD_1.txt","r")
##print first two characters: readline method can be used for this, specifying the number of bytes to be read 
#[ Since 1 char ~ 1 bytes, number specified can be equivalent to number of characters] 
print(read_handle.readline(2))
##Not specifying any valid non-negative integer takes the entire line from the current curser position
print(read_handle.readline())
print(read_handle.readline())
read_handle.close()


if Path(file_).is_file():
    print("The file: ",file_," is already present")


########Tip --- Add + for the mode to open even if the file doesn't exist, applicable for a+ and w+

##The other inbuilt python library for file I/O operations

##Binary I/O -- mode rb

#####https://docs.python.org/3/library/io.html#binary-i-o