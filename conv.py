import math

print("""1. Volume of sphere 
2. Area of circle 
3. Area of triangle 
4. Volume of cylinder 
""")

def sphereVol(radius):
  "Get the radius of sphere and apply the formula (4/3)πr³"
  return (4 / 3) * math.pi * (radius ** 3)
def circleArea(radius): 
  "get the radius of the circle and apply πr²"
  return math.pi * (radius ** 2)
def triangleArea(a, b, c):
  """
  get 3 arms.
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
  
  
choice = int(input("Enter the number: "))

match choice: 
  case 1:
    r = int(input("Enter the radius of sphere: "))
    print("The volume of the sphere is: ", sphereVol(r))
  case 2:
    r = int(input("Enter the radius of circle: "))
    print("The area of the circle is: ", circleArea(r))
  case 3:
    a = int(input("Enter a of the triangle: "))
    b = int(input("Enter b of the triangle: "))
    c = int(input("Enter c of the triangle: "))
    print("The area of the triangle is: ", triangleArea(a, b, c))
  case 4: 
    h = int(input("Enter the height of the cylinder: "))
    r = int(input("Enter the radius of the cylinder: "))
    print("The volume of the cylinder is: ", cylinderVol(h, r))
  
  
