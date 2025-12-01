

class Element:
    def __init__(self , point1 , point2 , E_type):
        self.point1 = point1
        self.point2 = point2
        self.type = E_type


class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.elements = []


class Grid:
    def __init__(self):
        self.points = []
        self.elements = []

    def find_point(self , x , y):
        for i in self.points:
            for j in i:
                if (j.x == x and j.y == y):
                    return j


def add_element(grid , E_type , point1_x , point1_y , point2_x , point2_y):
    first_point = grid.find_point(point1_x , point1_y)
    second_point = grid.find_point(point2_x , point2_y)
    new_element = Element(first_point , second_point , E_type)
    grid.elements.append(new_element)
    first_point.elements.append(new_element)
    second_point.elements.append(new_element)


points = []
for i in range(10):
    point_row = []
    for j in range(20):
        new_point = Point(i+1 , j+1)
        point_row.append(new_point)
    points.append(point_row)

grid = Grid()
grid.points = points
