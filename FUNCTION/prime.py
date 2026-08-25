#using  map check each elements is prime or not
def Prime(no):
    l=[]
    for i in range (1,no+1):
        if no%i==0:
            l.append(i)
        print("factors=" ,l)
        print("prime" if  len(l)==2 else "not prime")
l=[10,6,2,8,4,121,11,18,19,21,23,78,89]
obj=map(Prime,l)
print(list(obj))

