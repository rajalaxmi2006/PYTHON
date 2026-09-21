obj1 = open ("even.txt" , 'w')
obj2 = open ("odd.txt" , 'w')

res1, res2 = 0, 1

for no in range (1,500+1):
    if no % 2 == 0 :
        obj1.write(str(no) + " ")
        res1= res1+ no

    else :
        obj2.write (str(no) + " ")
        res2 = res2 + no

obj1.write("\n Sum of all even numbers  = " + str(res1))
obj2.write("\n Sum of all odd numbers  = " + str(res2))

obj1.close()
obj2.close()