obj = open ("Biodata.txt" , 'w')

obj.write ("Welcome to python world!" + '\n')
obj.write ("Name->" + "Rajalaxmi Biswal " + '\n')
obj.write ( "Age->" + str(19) + '\n')
obj.writelines (["DOB->" , "DD-31" , '/' , "MM-12" , '/' "YYYY-2006"])

obj.close()
