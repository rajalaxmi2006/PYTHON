obj = open("Number.txt",'w')

sum=0
for i in range (1,100+1):
    obj.write(str(i)+ " ")
    sum= sum+1 

obj.write( "\n Sum of the numbers : " + str(sum) + " ")
obj.close()

