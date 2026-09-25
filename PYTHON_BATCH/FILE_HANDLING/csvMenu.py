from csv import * 
def Create() :
        # fname = input("Enter file name : ")
        obj = open('demo.csv','x' , newline="\n")
        wobj = writer(obj)
        wobj.writerow(["Rollno","Name"])
        obj.close()

def Insert():
        obj = open('demo.csv','a' , newline="\n")
        wobj = writer(obj)
        Rollno = int(input("Enter student roll no :"))
        Name = input("Enter Studnet name :")
        wobj.writerow([Rollno,Name])
        obj.close()

def Display():
        obj = open('demo.csv','r')
        records = reader(obj)
        for record in records:
                print(record)
        obj.close()

def Remove():
        drollno = input("Enter any roll no which you want to delete : ")
        students , found = [] , False
        obj = open ("demo.csv",'r')
        records = reader(obj)
        for row in records :
                if row[0] == drollno :
                        found = True
                else :
                        students.append(row)

        obj.close()
        obj = open ("demo.csv", 'w',  newline='\n')
        wobj = writer(obj)
        wobj.writerows(students)
        if found :
                print("Successfully deleted!")
        else :
                print("Record not found!")
                
while True:
        ch = input("select \n I for insert records \n C for create file \n D for display all records \n Q for quit from file \n R for Remove existing file")
        if(ch=='I'):
                Insert()
        elif ch == "C":
                Create()
        elif ch == "D":
                Display()
        elif ch == "R":
                Remove()
        elif ch == "Q":
                pass
        else :
                print("invalid choice\n")
                