obj1 = open ("biodata.txt" , 'r')
# data = obj1.read(4)

# obj1.close()

# obj2 = open("newFile.txt" , 'w')
# obj2.write(data)

# obj2.close()


obj1.readline()
print(obj1.tell())
obj1.seek(25)
data = obj1.read(4)
obj1.close()

obj3 = open ("newFile2.txt", 'w')
obj3 . write(data)

obj3.close()
