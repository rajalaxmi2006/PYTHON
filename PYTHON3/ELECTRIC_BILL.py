cu=int(input("Enter current month  consume unit value"))
pu=int(input("Enter previous month consume unit value"))
unit=cu-pu
if unit >= 0:
    if unit>0 and unit <=50:
        bill=(unit-0)*2.90
        print(f"for 1st {unit} *2.90 = Rs.{bill}")
    elif unit >50 and unit <= 200:
        print(f"for 1st 50 unit *2.90 = Rs.{50*2.90}")
        bill=(unit-50)*4.70+50*2.90
        print(f"for next {unit-50}*4.70= Rs.{(unit-50)*4.70}")
    elif unit > 200 and unit <= 400:
        print (f"for 50 unit*2.90=rs.{50*2.90}")
        print(f"for 150 unit * 4.70=Rs.{150*4.70}")
        bill=(unit-200)*5.70+50*2.90+150*4.70
        print(f"for next {unit-200}*5.70 = Rs.{(unit-200)*5.70}")
    else :
        print (f"for 50 unit*2.90=rs.{50*2.90}")
        print(f"for 150 unit * 4.70=Rs.{150*4.70}")
        print(f"for 200 unit * 5.70=Rs.{200*5.70}")
        bill=(unit-400)*6.10+50*2.90+150*4.70+200*5.70
        print(f"for next {unit-400}*6.10 = Rs.{(unit-400)*6.10}")  
else:
    print("Invalid unit")
    exit()
print(f"Total unit={unit}")
print(f"Total bill amount=Rs.{bill+30}")
