from csv import * 
def Create() :
        # fname = input("Enter file name : ")
        obj = open('info.csv','x' , newline="\n")
        wobj = writer(obj)
        wobj.writerow(["Rollno","Name"])
        obj.close()

def Insert():
        obj = open('info.csv','a' , newline="\n")
        wobj = writer(obj)
        Rollno = int(input("Enter student roll no :"))
        Name = input("Enter Studnet name :")
        wobj.writerow([Rollno,Name])
        obj.close()

def Display():
        obj = open('info.csv','r')
        records = reader(obj)
        for record in records (obj) :
                print(record)
                
while True:
        ch = input("select \n I for insert records \n C for create file \n D for displau all records \n Q for quit from file")
        if(ch=='I'):
                Insert()
        elif ch == "C":
                Create()
        elif ch == "D":
                Display()
        elif ch == "Q":
                pass
        else :
                print("invalid choice\n")
                