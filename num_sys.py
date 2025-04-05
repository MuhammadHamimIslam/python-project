# convert decimal to binary 
def decimalToBin (num):
    return f"{bin(num)}"[2:]
    
# convert binary to decimal
def binToDecimal(num): 
    return int(num, 2)

# convert decimal to octal

# convert octal to decimal 
def octToDecimal(num): 
    return int(num, 8)
    
# convert hexadecimal to decimal 
def hexaToDecimal(num): 
    return int(num, 16)

print(hexaToDecimal(input(">>")))