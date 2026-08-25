sub1=float(input("Enter Odia secure mark"))
sub2=float(input("Enter Eng secure mark"))
sub3=float(input("Enter Math secure mark"))
sub4=float(input("Enter Phy secure mark"))
sub5=float(input("Enter Chem secure mark"))
sub6=float(input("Enter Bio secure mark"))
total=sub1+sub2+sub3+sub4+sub5+sub6
per=total*100/600
grade=None
if sub1>=30 and sub2>=30 and sub3>=30 and sub4>=30 and sub5>=30 and sub6>=30:
        if per >=60:
                grade="1st division"
        elif per >= 50 and per < 60:
                grade="2nd division"
        elif per >= 35 and per <50:
                grade="3rd division"
        else :
                grade="Fail"
else :
                grade="Fail"
print("Total mark secure=",total)
print("%Secure mark=",per)
print("Grade=",grade)
