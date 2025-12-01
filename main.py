

class Elements:
    def __init__(self , point1 , point2 , E_type):
        self.point1 = point1
        self.point2 = point2
        self.type = E_type


class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.elements = None

class Grid:
    def __init__(self):
        self.points = None


points = []
for i in range(10):
    point_row = []
    for j in range(20):
        new_point = Point(i+1 , j+1)
        point_row.append(new_point)
    points.append(point_row)

grid = Grid()
grid.points = points

