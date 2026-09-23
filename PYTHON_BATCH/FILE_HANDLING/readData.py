obj = open ("biodata.txt" , 'r')
print("before read file pointer position : " , obj.tell())

print(obj.readline())
print("after read one line file pointer position : " , obj.tell())

print(obj.read(4))
print(obj.read())
obj.seek(25)

print(obj.readlines())

obj.close()