#wap to check a given number is even or odd.
num=int(input("Enter a number"))
if num% 2 == 0:
    print("Even")
else :
    print("Odd")

#wap to check a year is leap year or not.
year=int(input("Enter any year"))
if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
    print("Leap year")
else:
    print("Not a leap year")

#wap to check a given string is general,questionmark or exclamatory sentence.
sentence=input("Enter a sentence")
if sentence.endswith("."):
    print("General sentence")
elif sentence.endswith("?"):
    print("Question mark sentence")
elif sentence.endswith("!"):
    print("Exclamatory sentence")
else :
    print("Non of the above")

#wap to check a word is upper case or lower case.
word=input("Enter any word")
if word.upper:
    print("upper")
elif word.lower:
    print("lower")
else:
    print("You don't have common sense.")




















