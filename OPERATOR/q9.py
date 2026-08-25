#largest of three numbers (using conditional operator)
a,b,c=25,40,15
largest = a if (a>b and a>c) else (b if b>c else c)
print("largest number is:",largest)
