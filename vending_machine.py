items: dict = {
    "burger": 90,
    "pizza": 80,
    "sandwich": 50,
    "chips": 15,
    "cake": 30,
    "chocolate": 20
}

def buy_item(item):
    print(f"You selected {item} -> ৳{items[item]} taka")
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0: 
                raise ValueError
            break  
        except ValueError:
            print("Enter a valid quantity")
    return f"Your price is ৳{quantity * items[item]} taka"    

def print_item(): 
    for i, (item, price) in enumerate(items.items(), 1): 
        print(f"{i}.{item}:     ৳{price}")
   
help_msg = """choice:
1.burger, 2.pizza 3.sandwich, 4.chips, 5.cake, 6.chocolate, q to quit the game, v to check the price of all item, h to print the message 
    """

print(help_msg)

while True:
    choice = input("Choose what you want to buy: ").strip()
    
    if choice.lower() == "q":
        print("Successfully quit the program!")
        break
    match choice.lower():
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
        case _:
            print("Invalid item")
        
    