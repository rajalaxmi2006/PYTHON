'''
#1. Write a program in python to replace all the 'a' by '@' in a file data.txt
f= open ('data.txt','r')
d= f.read ()
d= d.replace ('a','@')
f.close ()
f= open ("data.txt","w")
f.write(d)
f.close ()
'''

#2.  write a program in python to display only unique words from file "data.txt"
f= open ("data.txt",'r')
d= f. read ()
d= d.split ()
str = " "
m = []
for i in d :
        if i not in str:
                str = str+i
                print (i, end = "  ")
f.close ()

'''
#3.  write a program in python to count those lines from the file which are starting from T or M
f= open ("data.txt",'r')
d= f. readlines ()
c= 0
for i in d :
        if i [0] =='M' or i[0] == 'T':
                c=c +1
print ("total lines", c )
'''
'''
#4. write a program in python to read the entire content from file and copy only those words to another file which start from vowels.
f = open ("data.txt", 'r')
f1 = open ('lata.txt','w')
d= f. read ()
d= d. lower ()
word = d.split()
for i in word :
        if i [0] in ['a','e','i','o','u']:
                f1. write ()
f.close ()
f1. close ()
'''
'''
#5.Write a Python program to read a text file named sample.txt, count the number of words in the file, and display the result.
try:
    with open("data.txt", "r") as file:
        content = file.read()  # Read the entire content of the file
        words = content.split()  # Split the content into words
        word_count = len(words)  # Count the number of words
        print("Number of words in the file:", word_count)
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")
except Exception as e:
    print("An error occurred:", e)
'''
'''
#6.Write a Python program to remove all blank lines from a file named messy.txt.
try:
    with open("data.txt", "r") as infile:
        lines = infile.readlines()
    with open("raj.txt", "w") as outfile:
        for line in lines:
            if line.strip() != "":
                outfile.write(line)
    print("Blank lines removed. Saved to 'raj.txt'.")
except FileNotFoundError:
    print("File not found.")
'''




















