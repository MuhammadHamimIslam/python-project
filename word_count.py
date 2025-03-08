x = input("String: ")

def countWord(s): 
  obj = {}
  for i in sorted(s): 
    if i not in obj:
      obj[i] = 1
    else:
      obj[i] += 1
  return obj

print(countWord(x))