'''
#wap to display numbers from 1 to 100.
for i in range (10+1):
        print(i)
#wap to display all the even number b/w 1 to 100 and find sum of all even number and count number of even.
l=[]
for i in range(1,100+1):
    if i%2==0:
        l.append(i)
print("All evem number=", l, "\n sum of all even=", sum(l), "\n count even=", len(l))
#multiplication table.
i=2
no=int(input("Enter any number"))
for i in range (10+1):
    print(no,"x",i,"=",no*i)
#multiplication table (n).
i=2
no=int(input("Enter any number"))
for i in range (no+1):
    print("======", i , "======")
    j=1
    for j in range (10+1):
        print(i,"x",j,"=",i*j)
        j+=1
    i+=1
'''
#wap to find factors of any number
#12->1,2,3,4,6,12
#12->2,3,4,6,12
#12->1,2,3,4,6
#12->2,3,4,6
'''
no=int(input("Enter any number"))
for i in range (1,no+1):
    if no % i==0:
        print(i)
    i+=1

no=int(input("Enter any number"))
for i in range (2,no+1):
    if no % i==0:
        print(i)
    i+=1

no=int(input("Enter any number"))
for i in range (1,no):
    if no % i==0:
        print(i)
    i+=1

no=int(input("Enter any number"))
for i in range (2,no):
    if no % i==0:
        print(i)
    i+=1

#prime factor.
no=int(input("Enter any number"))
factor=[]
for i in range (1,no+1):
    if no % i==0:
        factor.append(i)
    i+=1
'''
'''
#wap to find the count all even factor of any number and find sum of all even factors.
no=int(input("Enter any number"))
count,res=0,0
for i in range (1,no+1):
    if no % i==0 and i % 2 ==0:
        print(i)
        count+=1
        res+=1
    i+=1
print("sum of all numbers=", res, "\n numbers of factor=", count)
'''
'''
#wap to display all words from a given string in desc order & count how many words are present in that string.
str=input("Enter any string")
str=str.split()
str.sort(reverse=True)
print(str,len(str))
'''
'''
#wap to display all palindrom word present in a given string & count numbers of palindrom word present in that string.
word=input("enter any string")
word=word.split()
print(word,len(word))
l=[]
for i in word:
    if i == i [ : : -1] and len(i)>1:
        l.append(i)
print(l,len(l))
'''
#wap to display all unique word present in a given string.
word=input("enter any string")
word=word.split()
s=set(word)
print(len(s),s)

#wap to display & count all vowel word present in a given string.
str=input("Enter any string")
words=str.split()
count=0
print(words)
for word in words:
    if word[0] in "AEIOUaeiou":
        print(word)
        count+=1
print("no of vowel words=", count)

#wap to display all number which is divided by both 5 & 3 but not with 4 with in any range & count how many numbers are present & find sum of all there.
res , count = 0 ,0
l=[]
for i in range (1,100+1):
    if (i%5==0 and i% 3==0) and i%4 != 0:
        l.append(i)
        print(i)
        count+=1
        res+=i
print("Total count=" , count , " \n sum of all num =", sum(l))