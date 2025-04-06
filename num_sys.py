# convert decimal to binary 
def decimalToBin (num):
    return f"{bin(num)}"[2:]
    
# convert binary to decimal
def binToDecimal(num): 
    return int(num, 2)

# convert decimal to octal
def decimalToOct(num): 
    return f"{oct(int(num))}"[2:]

# convert octal to decimal 
def octToDecimal(num): 
    return int(num, 8)

# convert decimal to hexadecimal 
def decimalToHexa(num):
    return f"{hex(int(num))}"[2:]

# convert hexadecimal to decimal 
def hexaToDecimal(num): 
    return int(num, 16)

helpMsg = """Choose one-
1. convert binary to decimal
2. convert decimal to binary
3. convert octal to decimal
4. convert decimal to octal
5. convert hexadecimal to decimal
6. convert decimal to hexadecimal
7. To print this message 
8. To exit the program 
"""
print(helpMsg)

while True: 
    # option choosing
    while True:
        try: # try block to get the input and then break 
            chosenOption = int(input("Choose one:"))
            break 
        except ValueError: # if value error don't break the loop and show errorsg
            print("Invalid input!")
    # error handling for chosen option 
    if 0 > chosenOption > 9: 
        print("choose the correct option!")
        continue
    # match case to apply the function 
    match chosenOption: 
        case 1:
            inpNum = input("Enter the number to convert it's base: ")
            print(binToDecimal(inpNum))
        case 2:
            inpNum = input("Enter the number to convert it's base: ")
            print(decimalToBin(inpNum))
        case 3:
            inpNum = input("Enter the number to convert it's base: ")
            print(octToDecimal(inpNum))
        case 4:
            inpNum = input("Enter the number to convert it's base: ")
            print(decimalToOct(inpNum))
        case 5:
            inpNum = input("Enter the number to convert it's base: ")
            print(hexaToDecimal(inpNum))
        case 6:
            inpNum = input("Enter the number to convert it's base: ")
            print(decimalToHexa(inpNum))
        case 7: print(helpMsg)
        case 8: break 
        case _: print("Invalid input!")
        