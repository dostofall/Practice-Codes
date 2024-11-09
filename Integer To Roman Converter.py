#Program to convert integers into roman numerals

integer = int(input("Enter the number to conver it to roman numeral here: "))
romancharacters = ["M","D","C","L","X","V","I"]
romanvalues = [1000,500,100,50,10,5,1]

romannumeral = []

multiplier = 1
parts_of_integer = []

while integer != 0:
    parts_of_integer.append(multiplier*(integer%10))
    integer = integer // 10
    multiplier *= 10
parts_of_integer.reverse()

for i in parts_of_integer:
    currentint = i
    tempromannumeral = ""
    if i not in romanvalues:
        while currentint != 0:
            for k in romanvalues:
                if k < currentint and (currentint%k != 0 and (k*4 > currentint)):
                    currentint -= k
                    tempromannumeral += romancharacters[romanvalues.index(k)]

                else:
                    if currentint % k == 0 and currentint//k <= 3:
                        tempromannumeral += romancharacters[romanvalues.index(k)] * (currentint//k)
                        currentint = 0
                        break
                    elif  ((len(romanvalues)-1)-romanvalues.index(k)) >= 1:
                        if ((len(romanvalues)-1)-romanvalues.index(k)) >= 1:
                            if k - (romanvalues[romanvalues.index(k)+1]) == i:
                                currentint = 0
                                tempromannumeral = romancharacters[romanvalues.index(k)+1] + romancharacters[romanvalues.index(k)]
                                break
                            elif ((len(romanvalues)-1)-romanvalues.index(k)) > 1:
                                if k - (romanvalues[romanvalues.index(k)+2]) == i:
                                    currentint = 0
                                    tempromannumeral = romancharacters[romanvalues.index(k)+2] + romancharacters[romanvalues.index(k)]
                                    break
    else:
        tempromannumeral = romancharacters[romanvalues.index(i)]
        currentint = 0
                        
    romannumeral.append(tempromannumeral)
            

roman = ""
for i in romannumeral:
    roman += i

print(roman)