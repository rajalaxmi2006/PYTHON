# 1.wap to find all factors of given list by using  general function & map function
'''
def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors
numbers = [10, 15, 21,54]
result = list(map(find_factors, numbers))
print(f"factors of {numbers}: {factors}")
'''
'''
#wap to find all vowel words from a string by using function.
    
def find_vowel_words(s):
    vowels = "aeiouAEIOU"
    words = s.split()
    vowel_words = []

    for word in words:
        if word[0] in vowels:
            vowel_words.append(word)

    return vowel_words

s=input("Enter any string")
result=find_vowel_words(s)
print(result)
'''
'''
#wap to find lcm of given list by using predefine function
from functools import reduce
def LCM(n1,n2):
    t1,t2=n1,n2
    while(n1 != n2):
        if n1>n2:
            n2=n1-n2
        else:
            n2=n2-n1
    return(t1*t2)//n1
l=[1,2,3,4,5,6,7,8,9,10]
obj=reduce(LCM,l)
print(list(obj))
'''
'''
from math import lcm
print(lcm(1,2,3,4,5,6,7,8,9,10))
'''
#wap to make reverse numbers of all elements present in a given list
def reverse(no):
    res=0
    while no !=0:
        res=res*10+no%10
        no //= 10
    return res
l=[21,23,45,56,66,79]
obj=map(reverse,l)
print(list(obj))





















