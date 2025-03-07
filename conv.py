import math

print("""1. Volume of sphere 
2. Area of circle 
3. Area of triangle 
4. Volume of cylinder 
5. Perimeter of circle 
6. Info about triangle 
7. Surface of sphere 
""")

def sphereVol(radius):
  "Get the radius of sphere and apply the formula (4/3)πr³"
  return (4 / 3) * math.pi * (radius ** 3)
def circleArea(radius): 
  "get the radius of the circle and apply πr²"
  return math.pi * (radius ** 2)
def triangleArea(a, b, c):
  """
  get 3 sides.
  find s = (a + b + c)
  then apply formula s*(s-a)*(s-b)*(s-c)
  """
  s = (a + b + c)
  return s * (s - a) * (s - b) * (s - c)
def cylinderVol(height, radius): 
  """
  get the radius and height of the cylinder 
  then apply the formula πr²h
  """
  return math.pi * (radius ** 2) * height
def permCircle(radius): 
  """
  get the radius 
  then apply the formula 2πr
  """
  return 2 * math.pi * radius
def infoTriangle(a, b, c):
  """
  Determine the type of triangle based on its sides a, b, and c.
  Returns:
    str: Description of the triangle type or an error message if not valid.
  """
    # checks if triangle is possible 
  if (a <= 0) or (b <= 0) or (c<= 0): 
    return "Triangle isn't possible! All sides must be positive or greater than 0"
    
  if ((a + b) <= c) or ((b + c ) <= a) or((a + c) <= b):
    return "Triangle isn't possible"
    
  else:
    # checks if it's a right triangle 
    if (a**2 + b**2 == c**2) or  (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2) :
      return "It's a right triangle!"
    # checks if it's a equilateral triangle 
    elif a == b == c:
      return "It's a equilateral triangle!"
    # checks if it's a isosceles triangle 
    elif (a == b) or (b == c) or (a == c):
      return "It's a isosceles triangle"
    else: return "It's a scalene triangle"
def sphereSurf(radius): 
  """
  get the radius and apply the formula 4πr²
  """
  return 4 * math.pi * (radius ** 2)
while True:
  choice = input("Choose one or type /exit to exit the program: ")
  match choice: 
    case "1":
      r = int(input("Enter the radius of sphere: "))
      print("The volume of the sphere is: ", sphereVol(r))
    case "2":
      r = int(input("Enter the radius of circle: "))
      print("The area of the circle is: ", circleArea(r))
    case "3":
      a = int(input("Enter a of the triangle: "))
      b = int(input("Enter b of the triangle: "))
      c = int(input("Enter c of the triangle: "))
      print("The area of the triangle is: ", triangleArea(a, b, c))
    case "4": 
      h = int(input("Enter the height of the cylinder: "))
      r = int(input("Enter the radius of the cylinder: "))
      print("The volume of the cylinder is: ", cylinderVol(h, r))
    case "5": 
      r = int(input("Enter the radius of circle: "))
      print("The perimeter of the circle is: ", permCircle(r))
    case "6": 
      a = int(input("Enter a of the triangle: "))
      b = int(input("Enter b of the triangle: "))
      c = int(input("Enter c of the triangle: "))
      print(infoTriangle(a, b, c))
    case "7": 
      r = int(input("Enter the radius of sphere: "))
      print(sphereSurf(r))
    case "/exit": break
    case _: 
      print("command not found")
  
