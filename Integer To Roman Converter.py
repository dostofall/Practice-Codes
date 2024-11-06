#Program to convert integers into roman numerals

integer = int(input("Enter the number to conver it to roman numeral here: "))
basicromanvalues = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
repeatableromanvalues = {"M":1000,"C":100,"X":10,"I":1}
romancharacters = ["M","D","C","L","X","V","I"]
basicromanvalueskeys = list(basicromanvalues.keys())
romanvalues = [1000,500,100,50,10,5,1]

basicromanvaluesvalues = list(basicromanvalues.values())

romannumeral = ""

while integer != 0:
    for i in basicromanvalues:
        if basicromanvalues[i] < integer:
            integer -= basicromanvalues[i]
            romannumeral += i
        elif basicromanvalues[i] - integer in romanvalues:
            romannumeral = romannumeral + romancharacters[romanvalues.index(basicromanvalues[i] - integer)]
            romannumeral += i
            integer -= integer
            break
print(romannumeral)