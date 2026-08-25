num=int(input("Enter any number"))
product=1
square=num*num
temp=num
while temp>0:
    product*=10
    temp//=10
last_digit=square%product
if last_digit==num:
    print("automorphic")
else:
    print("not automorphic")
