#power of two check(using bitwise operator)
num =16
result ="power of 2" if (num & (num -1)) ==0 and num !=0 else "not power of 2"
print(f"{num} is {result}")
