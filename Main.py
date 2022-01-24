def bitInput():
    userInput = 0
    while(True):
        userInput = input("\nIngrese un numero binario de 8 bits:\n")
        if(len(userInput) == 8 and userInput.isnumeric()):
            return userInput
        else:
            print("Ha ingresado un numero binario invalido. Pruebe de nuevo.")

def toMS(bits):
    return bits

def toC2(bits):
    c2 = "b"
    return c2



print("Bienvenido al sistema de conversion!")
while(True):
    bits = bitInput()
    print("Bits en M&S:\t" + toMS(bits))
    print("Bits en C2:\t" + toC2(bits))
