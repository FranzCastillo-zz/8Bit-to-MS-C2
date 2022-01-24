def bitInput():
    userInput = 0
    nonBinary = ["2", "3", "4", "5", "6", "7", "8", "9"]
    isBinary = False
    while(True):
        userInput = input("\nIngrese un numero binario de 8 bits:\n")
        #Validacion solo 0 y 1
        if any(n in userInput for n in nonBinary):
            isBinary = False 
        else:
            isBinary = True
        if(len(userInput) == 8 and userInput.isnumeric() and isBinary == True):
            return userInput
        else:
            print("Ha ingresado un numero binario invalido. Pruebe de nuevo.")

def toMS(bits):
    temp = list(bits)
    if(temp[0] == '0'):
        temp[0] = '1'
    else:
        temp[0] = '0'
    return "".join(temp)

def toC2(bits):
    temp = list(bits)
    c1 = ''
    for i in range(0, len(temp)):
        if(temp[i]== '0'):
            c1 += '1'
        else:
            c1 += '0'
    c2 = "".join(c1)
    return c2



print("Bienvenido al sistema de conversion!")
while(True):
    bits = bitInput()
    print("Complemento en M&S:\t" + toMS(bits))
    print("Complemento a 2:\t" + toC2(bits))
