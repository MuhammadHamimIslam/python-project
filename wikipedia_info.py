import wikipediaapi

wiki = wikipediaapi.Wikipedia(language="en", extract_format = wikipediaapi.ExtractFormat.WIKI, user_agent="WikiTiwiki/1.0") # Set up the wikipedia 

page_name = input("Enter the page name you want to know about: ").strip()
page = wiki.page(page_name) # get the page name

def get_data_from_wikipedia(): 
    if page.exists(): # check if page exists 
        page_title = page.title # returns page title 
        page_summary = page.summary # returns the page summary 
        page_text = page.text # returns the text
        page_categories = page.categories # returns page categories as dict
        page_sections = page.sections # list page sections 
        page_links = page.links # page links as dict
    
        print(f"{page_title = }")
        print(f"page summary = {page_summary:150}")
        print(f"page text = {page_text:200}")
        print(f"{page_categories = }")
        print(f"{page_sections = }")
        print(f"{page_links = }")
    else:
        print("Page not found!")

try:
    get_data_from_wikipedia()
except Exception as e:
    print("Can't get data: ", e)