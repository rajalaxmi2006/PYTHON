obj = open("Factors.txt" , 'w')
n = int(input("Enter any number : "))
obj.write(f"{n} factors = ")
c = 0

for i in range (1, n+1):
    if n % i == 0 :
        obj.write(str(i) + ' ')
        c += 1
obj.write("\n" + str (n) + " : ")
obj.write(" \n prime number" if c == 2 else "Not Prime")
