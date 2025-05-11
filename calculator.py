# user input taking function 
def take_input(prompt):
    while True:
      try:
          input_number = float(input(prompt))
          return input_number
          break
      except ValueError:
          print("Enter a valid value!")
        
# function to perform calculation 
def calculate(num1, num2, operator):
    if operator == "+": return num1 + num2
    elif operator == "-": return num1 - num2
    elif operator in ("*", "×"): return num1 * num2
    elif operator in ("/", "÷"): return num1 / num2
    elif operator in ("**", "^"): return num1 ** num2
    else: return "Invalid operator!"
    

# main program design 
def main(): 
    while True:
        operator = input("Enter the operator: (+, -, (*, ×), (/, ÷), (**, ^) or q to quit: ").strip() # get the input and trim the whitespaces 
        # if user enter q -> quit the program
        if operator.lower() == "q": 
            break 
        # take user input 
        num1 = take_input("Enter number 1: ")
        num2 = take_input("Enter number 2: ")
        # a try block of performing calculation 
        try:
            print(calculate(num1, num2, operator))
        except Exception as e:
            print(e)
        




if __name__ == '__main__':
    main()