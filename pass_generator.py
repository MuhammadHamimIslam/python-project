import string 
import random

def take_inp(prompt):
    """
    DESCRIPTION: taking valid input 
    
    args: 
    prompt -> prompt while taking the input
    
    how it works:
    run an infinite while loop then put a try, except block if user input is invalid it goes to except block. If user input is correct return the value by trimming whitespaces and break the loop
    """
    while True:
        try:
            data = int(input(prompt).strip())
            if not data: 
                raise ValueError
            return data
        except ValueError:
            print("Enter a valid input")

def generate_pass(length): 
	"""
	take the length as an argument.
	list all of the characters. then shuffle the list to make it random. then create an empty list to store the password. Then choose a random item from the characters and append it to the password. finally join the list and return it 
	"""
	characters = list(string.ascii_letters +  string.digits + "+$#@*':;!?.%=/-") # all password characters 
	random.shuffle(characters) # shuffle the order
	password = [] # password holder
	for i in range(length):
		# shuffle it again to make it more random 
		random.shuffle(characters)
		password.append(random.choice(characters)) # append a random item to password 
	return "".join(password)

if __name__ == '__main__':
	password_length = take_inp("Enter the password length: ")
	print(generate_pass(password_length))