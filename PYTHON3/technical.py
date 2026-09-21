#wap to display numbers from 1 to n.
#find sum of 1 to n
#display all the even numbers from 1 to n
#display all the prime number from 1 to n
#find the sum of first 1 to n armstrong number

'''
#1.Ans :
n=int(input("enter any number"))
for i in range (1,n+1):
    print(i,end=" ")
'''
'''
#2.Ans:
n=int(input("Enter any number"))
sum=0
for i in range (1,n+1):
    sum+=i
print("sum of numbers=",sum)
'''
'''
#2.
n=int(input())
lst=[x for x in range(1,n+1)]
print(lst)
'''
'''
print(' '.join([str(x) for x in range(1,int(input())+1)]))
'''
'''
#3.Ans:
n=int(input("Enter any number"))
l=[]
for i in range (1,n+1):
    if i%2==0:
        l.append(i)
print("even numbers are",l)
'''
'''
#4.Ans:
n=int(input("Enter any number"))
for i in range (2,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)
'''
#5.Ans:
n = int(input("Enter a number: "))

for num in range(1, n + 1):
    order = len(str(num))      # number of digits
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num:
        print(num)













