#Program to convert integers into roman numerals

integer = int(input("Enter the number to conver it to roman numeral here: "))
basicromanvaluecount = {"M":0,"D":0,"C":0,"L":0,"X":0,"V":0,"I":0}
repeatableromanvalues = ["M","C","X","I"]
romancharacters = ["M","D","C","L","X","V","I"]
basicromanvalueskeys = list(basicromanvaluecount.keys())
romanvalues = [1000,500,100,50,10,5,1]

basicromanvaluesvalues = list(basicromanvaluecount.values())

romannumeral = ""

while integer != 0:
    for i in romanvalues:
        if i == integer:
            integer = 0
            break
        if i < integer:
            integer -= i
            basicromanvaluecount[(romancharacters[romanvalues.index(i)])] += 1
        
for i in basicromanvaluecount:
    if basicromanvaluecount[i] > 3:
        

        
        

print(romannumeral)