def bitInput():
    userInput = 0
    while(True):
        userInput = input("\nIngrese un numero binario de 8 bits:\n")
        if(len(userInput) == 8 and userInput.isnumeric()):
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
    c2 = "b"
    return c2



print("Bienvenido al sistema de conversion!")
while(True):
    bits = bitInput()
    print("Complemento en M&S:\t" + toMS(bits))
    print("Complemento a 2:\t" + toC2(bits))
