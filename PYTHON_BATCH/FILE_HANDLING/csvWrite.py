from csv import *       

obj = open("data.csv", 'w' , newline="\n")
wobj = writer(obj)
wobj.writerow(['Rollno' , 'Name' , 'DeptName', 'Gender', 'Address'])
wobj.writerow(['1' , 'Raj' , 'CS', 'Female', 'Puri'])
wobj.writerow(['2' , 'Laxmi' , 'CS', 'Female', 'BBSR'])

obj.close()