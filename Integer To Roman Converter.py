#Program to convert integers into roman numerals

integer = int(input("Enter the number to conver it to roman numeral here: "))
basicromanvalues = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
repeatableromanvalues = {"M":1000,"C":100,"X":10,"I":1}

basicromanvalueskeys = list(basicromanvalues.keys())

romancharactercounts = {"M":0,"D":0,"C":0,"L":0,"X":0,"V":0,"I":0}

maxcountexceeded = True

romannumeral = ""

currentexceedingvalues = []

while integer != 0 or maxcountexceeded == True:
    if integer == 0 and maxcountexceeded == True:
        for i in romancharactercounts:
            if romancharactercounts[i] > 3:
                currentexceedingvalues.append(i)
        for value in currentexceedingvalues:
            