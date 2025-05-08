import json
# get data from json file
def get_books_data(): 
    with open('books_data.json') as file:
        content = file.read()
    return json.loads(content) # parse the json data to python object 

books = get_books_data()

# search for book 
def find_book(books, targeted_book): 
    return list(filter(lambda x: x.get("name") == targeted_book, books)) or "Book not found"
    
print("Welcome to The book haven library")

while True:
    book_name = input("Enter book name: ")
    
    print(find_book(books, book_name))
    break
