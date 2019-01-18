import math

class Point:
  def get_x(self):
    return self._x
  
  def get_y(self):
    return self._y

  def set_x(self, x : float):
    self._x = x

  def set_y(self, y : float):
    self._y = y

  x = property(get_x, set_x)
  y = property(get_y, set_y)

  def __init__(self, x : float = 0.0, y : float = 0.0):
    self._x = x
    self._y = y

def Len(A : Point, B : Point):
  return math.sqrt((A.x + B.x)*(A.x + B.x) + (A.y + B.y)*(A.y + B.y))

class Triangle:
  def __init__(self, A : Point, B : Point, C : Point):
    self._A = A
    self._B = B
    self._C = C

  def is_exist(self):
    AB = Len(self._A, self._B)
    BC = Len(self._B, self._C)
    AC = Len(self._A, self._C)

    if AB + BC <= AC:
      return False
    elif BC + AC <= AB:
      return False
    elif AC + AB <= BC:
      return False
    else:
      return True

  def per(self):
    return Len(self._A, self._B) + Len(self._B, self._C) + Len(self._A, self._C)

  def square(self):
    p = self.per() / 2
    AB = Len(self._A, self._B)
    BC = Len(self._B, self._C)
    AC = Len(self._A, self._C)

    return math.sqrt(p * (p - AB) * (p - BC) * (p - AC))


print ("Point A: ")
Ax = float(input())
Ay = float(input())
print ("Point B: ")
Bx = float(input())
By = float(input())
print ("Point C: ")
Cx = float(input())
Cy = float(input())
Tr = Triangle(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy))
print("Triangle: ")
if Tr.is_exist():
  print("Exist")
  print("Per: " + str(Tr.per()))
  print("Square: " + str(Tr.square()))
else:
  print("Not exist")

