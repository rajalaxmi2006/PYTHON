## File Writing Operation 

-  before write we must  open that file
-  in a file all data must be string type
- for write operation python provides:

        -write () : write one one parameters into a file
        -writelines ([]) : write data in a list format

## File Read Operation

- before read file must be present otherwise raise an error (FileNotFoundError)
- for read operation we use :

        -read() : read one one character from file upto EOF
        -read(n) : read one one character from file upto n ( numbers of charcters)
        -readline() : read only one line data 
        -readlines() : read all data from file within a list

# How to set and get file pointer position

TELL() : is used to find current pointer position
SEEK(position) : is used to set file current pointer position

