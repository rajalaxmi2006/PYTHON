# duplicate palindrom,duplicate remove from a array

array1 = [1, 2, 3,4,1 ,5,4]
array2= []

for i in array1:
    if i not in array2:
        array2.append[i]
return array2

num=125
temp = num
result=0
while num != 0:
    digit = num % 10
    result = result * 10 + digit
    num = num //10

if result == temp:
    print(f"The num {temp} is palindrom")
else :
    print(f"The num {temp} is not palindrom")

# sum of even digit from a number:
num = 12546
sum = 0
while num!= 0 :
    digit = num%10
    if digit % 2 == 0:
        sum = sum +digit

    num = num // 10
print(sum)

# armstrong

num =
lenght= len (str(num))
result = 0
temp = num
while num != 0 :
    digit = num %10
    result= result + (digit ** length)
    num = num // 10
