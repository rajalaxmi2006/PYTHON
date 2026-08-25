#1. Write a program to find the largest digit in a number using a while loop. 
num = int(input("Enter a number: ")) 
max_digit = 0 
while num > 0: 
    digit = num % 10 
    if digit > max_digit: 
        max_digit = digit
        num //= 10 
        print("Largest digit is:", max_digit ) 
#2. Write a program to print the Fibonacci series up to n terms using a while loop. 
n = int(input("Enter number of terms: ")) 
a, b = 0, 1 
count = 0 
while count < n: 
    print(a, end=" ") 
    a, b = b, a + b 
    count += 1 
#3. Write a program to check whether a number is an Armstrong number using a while loop. 
#� Armstrong number: A number is Armstrong if the sum of cubes of its digits equals the 
#number itself (e.g., 153 → 1³ + 5³ + 3³ = 153) 
num = int(input("Enter a number: ")) 
original = num 
sum = 0 
while num > 0: 
    digit = num % 10 
    sum += digit ** 3 
    num //= 10 
    if sum == original: 
        print("Armstrong number") 
        else:
            print("Not an Armstrong number") 
#4. Keep summing the digits of a number until a single-digit number is obtained (e.g., 9875 → 
#9+8+7+5=29 → 2+9=11 → 1+1=2) 
num = int(input("Enter a number: ")) 
while num >= 10: 
    temp = num 
    sum_digits = 0 
    while temp > 0: 
        sum_digits += temp % 10 
        temp //= 10 
        num = sum_digits 
        print("Single digit sum:", num) 
#5. Check whether a number is a perfect number (e.g., 28 → 1 + 2 + 4 + 7 + 14 = 28) 
num = int(input("Enter a number: ")) 
i = 1 
sum_divisors = 0 
while i < num: 
    if num % i == 0: 
        sum_divisors += i 
        i += 1 
        if sum_divisors == num: 
            print("Perfect number") 
            else: 
                print("Not a perfect number") 
#6. Find the GCD (Greatest Common Divisor) of two numbers 
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
while b != 0: 
    a, b = b, a % b 
    print("GCD is:", a) 
#7. Program to reverse order of words. 
s=input("Enter Some String:")  
l=s.split()  
l1=[]  
i=len(l)-1  
while i>=0:
    l1.append(l[i])
    i=i-1
    output=' '.join(l1)
    print(output) 
#8. Program to reverse internal content of each word. 
s=input("Enter Some String:")  
l=s.split()  
l1=[]  
i=0  
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
    output=' '.join(l1)
    print(output) 
#9. Write a program to remove duplicate characters from the given input string? 
s=input("Enter Some String:")  
l=[]  
for x in s:
    if x not in l:
        l.append(x)
        output=''.join(l)
        print(output) 
#10. Write a program to find the number of occurrences of each character present in the given String? 
s=input("Enter the Some String:")  
d={}  
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
        else:
            d[x]=1
            for k,v in d.items():
                print("{} = {} Times".format(k,v))    
