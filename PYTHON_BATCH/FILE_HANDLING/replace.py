obj = open ("lata.txt" , 'r')
data = obj.read()

data.replace("Goodddddddddd", "Badddddddddd")

obj.close()

obj = open ("lata.txt", "w")
obj.write(data)
obj.close()


