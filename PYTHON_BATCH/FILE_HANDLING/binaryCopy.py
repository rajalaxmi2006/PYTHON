obj = open ("logo_lit.jpg" , 'rb')

data = obj.read()
obj.close()

obj = open ("lit-coverpage.png", 'wb')
obj.write(data)

obj.close()