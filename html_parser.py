import re

code = input("Enter html code to get the info: ") 

matches = re.search(r"^(<.+>)(.+)(</.+>)$", code) # search for a string starts with <tagName> then text and ends with </tagName>

print(matches.group(2))