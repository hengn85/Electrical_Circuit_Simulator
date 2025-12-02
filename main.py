

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

class Edge:
    def __init__(self , node1 , node2):
        self.node1 = node1
        self.node2 = node2
        self.elements = []

class Node:
    def __init__(self):
        self.points = []
        self.edges = []

class Grid:
    def __init__(self):
        self.points = []
        self.elements = []

    def init_points(self):
        points = []
        for i in range(10):
            point_row = []
            for j in range(20):
                new_point = Point(i+1 , j+1)
                point_row.append(new_point)
            points.append(point_row)
        self.points = points

    def is_empty(self , first_point , second_point):
        for i in first_point.elements:
            if i in second_point.elements:
                return False
        return True

    def find_point(self , x , y):
        for i in self.points:
            for j in i:
                if (j.x == x and j.y == y):
                    return j

    def add_element(self , E_type , point1_x , point1_y , point2_x , point2_y):
        
        first_point = self.find_point(point1_x , point1_y)
        second_point = self.find_point(point2_x , point2_y)
        new_element = Element(first_point , second_point , E_type)
        self.elements.append(new_element)
        first_point.elements.append(new_element)
        second_point.elements.append(new_element)

    # def find_nodes(self):



# def print_elements(grid):
#     for i in grid.elements:
#         print(f'{i.type} : ({i.point1.x} , {i.point1.y}) ({i.point2.x} , {i.point2.y})')
    


grid = Grid()

grid.init_points()





