#1. Check if a number is positive, negative, or zero 
num = int(input(“Enter any number”)) 
if num > 0: 
    print("Positive") 
elif num == 0: 
    print("Zero") 
else: 
    print("Negative") 
#2. Find the largest of three numbers. 
a , b, c= 5, 8, 3 
if a >= b and a >= c: 
    print("Largest:", a) 
elif b >= a and b >= c: 
    print("Largest:", b) 
else: 
    print("Largest:", c) 
#3. Check if a year is a leap year 
year = 2024 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print("Leap Year") 
else: 
    print("Not a Leap Year") 
#4. Check triangle type using sides 
a, b, c = 5, 5, 5 
if a == b == c: 
    print("Equilateral Triangle") 
elif a == b or b == c or a == c: 
    print("Isosceles Triangle") 
else: 
    print("Scalene Triangle") 
#5. 24-hour to 12-hour format converter 
hour = 14 
if hour == 0: 
    print("12 AM") 
elif hour < 12: 
    print(f"{hour} AM") 
elif hour == 12: 
    print("12 PM") 
else: 
    print(f"{hour - 12} PM") 
#6. Days in a month (not considering leap year) 
month = 2 
if month in [1, 3, 5, 7, 8, 10, 12]: 
    print("31 days") 
elif month in [4, 6, 9, 11]: 
    print("30 days") 
elif month == 2: 
    print("28 days") 
else: 
    print("Invalid month") 
#7. Password strength checker 
password = "abc123" 
if len(password) < 6: 
    print("Weak password") 
elif password.isalpha() or password.isdigit(): 
    print("Moderate password") 
else: 
    print("Strong password")
