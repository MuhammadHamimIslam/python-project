
# program design 
while True:
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    operator = input("Enter the operator: ")
    if not operator: 
        break
    if operator == "+":
        print("sum is:  %f", number1 + number2)
    elif operator == "-":
        print("Result is: %f", number1 - number2)
    elif operator in ("*", "×") :
        print("Result is: %f", number1 * number2)
    elif operator in ("/", "÷"):
        try:
            print("Result is: %f", number1 / number2)
        except ZeroDivisionError:
            print("Can't divide by 0!")
    else:
        print("Invalid operator!")