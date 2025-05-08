import json

# get data from json file
def get_books_data(): 
    with open('data/books_data.json') as file: # open the file 
        content = file.read() # get the content
    return json.loads(content) # parse the json data to python object 

books = get_books_data()

# search for book 
def find_book(books, targeted_book): 
    # return The desired book that's name is the searched book
    return list(filter(lambda x: x.get("name") == targeted_book, books)) or "Book not found"
    
print("Welcome to The book Haven library")

while True:
    book_name = input("Enter book name: ")
    
    print(find_book(books, book_name))
    break

