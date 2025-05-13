# all items
items: dict = {
    "burger": 90,
    "pizza": 80,
    "sandwich": 50,
    "chips": 15,
    "cake": 30,
    "chocolate": 20,
    "mojo":  25,
    "fresh water": 20
}

def buy_item(item):
    print(f"You selected {item} -> ৳{items[item]} taka") # show the selected item with price
    while True: # loop to take the valid value
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0: # if quantity is 0 or less than 0 raise an error for error check 
                raise ValueError
            break  
        except ValueError:
            print("Enter a valid quantity")
    return f"Your price is ৳{quantity * items[item]} taka"  # return items price

def print_item(): 
    for i, (item, price) in enumerate(items.items(), 1): # enumerate the the items key, value 
        print(f"{i}.{item}:     ৳{price}")
   
help_msg = """choice:
1.burger, 2.pizza 3.sandwich, 4.chips, 5.cake, 6.chocolate, 7.mojo, 8.fresh water q to quit the game, v to check the price of all item, h to print the message 
    """

print(help_msg) # first print the help message 

while True:
    choice = input("Choose what you want to buy: ").strip().lower() # get the choice and trim the white spaces 
    
    if choice == "q":
        print("Successfully quit the program!")
        break
    # match case statement to match the choice
    match choice:
        case "h":
            print(help_msg)
        case "v": 
            print_item()
        case "1": 
            print(buy_item("burger"))
        case "2": 
            print(buy_item("pizza"))
        case "3": 
            print(buy_item("sandwich"))
        case "4": 
            print(buy_item("chips"))
        case "5": 
            print(buy_item("cake"))
        case "6": 
            print(buy_item("chocolate"))
        case "8": 
            print(buy_item("mojo"))
        case "9": 
            print(buy_item("fresh water"))
        case _:
            print("Invalid item")
        
    