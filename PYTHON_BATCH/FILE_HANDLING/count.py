obj = open("lata.txt", 'r')
data = obj.read()

print("Numbers Of Character : " ,len(data))
print("Numbers Of Word : " ,len(data.split()))
print("Numbers Of Lines : " ,len(data.splitlines()))


obj.close()

