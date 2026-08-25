#1. Sum of digits of a number using for loop? 
num = 54321 
sum_digits = 0 
for digit in str(num): 
    sum_digits += int(digit) 
    print("Sum:", sum_digits) 
#2. Find all prime numbers from 1 to 50 
for num in range(2, 51): 
    for i in range(2, num): 
        if num % i == 0: 
            break
        else: 
            print(num, end=' ') 
#3. Print only even-position characters in a string 
s = "PYTHONLOOP" 
for i in range(0, len(s), 2): 
    print(s[i], end='') 
#4. Print only non-repeating characters from a string 
s = "programming" 
for ch in s: 
    if s.count(ch) == 1: 
        print(ch, end=' ') 
#5. Check if a number is an Armstrong number (e.g. 153) 
num = 153 
sum = 0 
for digit in str(num): 
    sum += int(digit) ** len(str(num)) 
    print("Armstrong" if sum == num else "Not Armstrong") 
#6. Find the largest digit in a number 
num = 986532 
max_digit = 0 
for ch in str(num): 
    if int(ch) > max_digit: 
        max_digit = int(ch) 
        print("Max digit:", max_digit) 
#7. Print all palindromic numbers between 10 and 200 
for i in range(10, 201): 
    if str(i) == str(i)[::-1]: 
        print(i, end=' ') 
#8. Count frequency of each character in a string (without collections module) 
s = "loopinside" 
for ch in sorted(set(s)): 
    count = 0 
    for c in s: 
        if c == ch: 
            count += 1 
            print(f"{ch}: {count}") 
#9. Find factorial of each digit in a number and sum them 
num = 145 
sum = 0 
for ch in str(num): 
    fact = 1 
    for i in range(1, int(ch)+1): 
        fact *= i 
        sum += fact 
        print("Sum of factorial of digits:", sum) 
#10. Count frequency of words in a sentence 
sentence = "Python is fun and Python is easy" 
words = sentence.split() 
for word in set(words): 
    count = 0 
    for w in words: 
        if w == word: 
            count += 1 
            print(f"{word}: {count}") 
#11. Print all pairs of numbers from 1 to 5 
for i in range(1, 6): 
    for j in range(1, 6): 
        print(f"({i},{j})", end=' ') 
        print() 
#12. Reverse each word in a sentence 
sentence = "Python for loop practice" 
words = sentence.split() 
for word in words: 
    rev = '' 
    for i in range(len(word)-1, -1, -1): 
        rev += word[i] 
        print(rev, end=' ') 
#13. Find the longest word in a list 
words = ["python", "list", "comprehension", "loop"] 
longest = "" 
for word in words: 
    if len(word) > len(longest): 
        longest = word 
        print("Longest word:", longest) 
#14. Remove duplicate characters from a string 
s = "programming" 
result = "" 
for ch in s: 
    if ch not in result: 
        result += ch 
        print("Without duplicates:", result) 
#15. Find common elements in two lists 
list1 = [1, 2, 3, 4] 
list2 = [3, 4, 5, 6] 
common = [] 
for i in list1: 
    for j in list2: 
        if i == j and i not in common: 
            common.append(i) 
            print("Common elements:", common) 
#16. Print all unique words in a sentence 
sentence = "python is fun and python is powerful" 
words = sentence.split() 
for i in range(len(words)): 
    count = 0 
    for j in range(len(words)): 
        if words[i] == words[j]: 
            count += 1 
            if count == 1: 
                print(words[i], end=' ') 
#17. Find all pairs in a list that sum to a given number 
nums = [1, 3, 5, 2, 4, 6] 
target = 7 
for i in range(len(nums)): 
    for j in range(i+1, len(nums)): 
        if nums[i] + nums[j] == target: 
            print(f"{nums[i]} + {nums[j]} = {target}") 
#18. Remove duplicates from a list (without set) 
nums = [1, 2, 3, 2, 4, 3, 5] 
unique = [] 
for num in nums: 
    if num not in unique: 
        unique.append(num) 
        print("Without duplicates:", unique)
