
# -------------------------------------------------------------------
class Comppressed_Point:
    def __init__(self):
        self.elements = []
        self.points = []

    def update_elements(self , point):
        for i in point.elements:
            if (i not in self.elements) and (i.type != 1):
                self.elements.append(i)
# --------------------------------------------------------------------
class Circuit:
    def __init__(self , elements):
        self.elements = elements
        self.compressed_points = []

    def is_appended(self , point):
        for compressed in self.compressed_points:
            if point in compressed.points:
                return True
        return False

    def find_compressed(self , point):
        for i in self.compressed_points:
            if point in i.points:
                return i

    def init_circuit(self , grid):
        for row in grid.points:
            for point in row:
                point.compressed = False

        for row in grid.points:
            for point in row:
                if not point.compressed:
                    new_compressed = Comppressed_Point()
                    new_compressed.update_elements(point)
                    new_compressed.points.append(point)
                    self.compressed_points.append(new_compressed)

                    neighbors = []
                    grid.find_neighbors(point , neighbors)

                    for neighbor in neighbors:
                        new_compressed.points.append(neighbor)
                        new_compressed.update_elements(neighbor)

# --------------------------------------------------------------------- 
# ---------------------------------------------------------------------
class Element:
    def __init__(self , point1 , point2 , E_type , amount):
        self.point1 = point1
        self.point2 = point2
        self.type = E_type
        self.amount = amount

    def find_another_point(self , point):
        if self.point1 == point:
            return self.point2
        if self.point2 == point:
            return self.point1

# ---------------------------------------------------------------------
class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.elements = []
        self.compressed = False

    def has_sim(self):
        for i in self.elements:
            if i.type == 1:
                return True
        return False
# ----------------------------------------------------------------------
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

    def add_element(self , E_type , point1_x , point1_y , point2_x , point2_y , amount):
        first_point = self.find_point(point1_x , point1_y)
        second_point = self.find_point(point2_x , point2_y)
        if self.is_empty(first_point , second_point):
            new_element = Element(first_point , second_point , E_type , amount)
            self.elements.append(new_element)
            first_point.elements.append(new_element)
            second_point.elements.append(new_element)

    def find_active_points(self , active_points):
        for i in self.points:
            for j in i:
                if len(j.elements) != 0:
                    active_points.append(j)

    def find_neighbors(self , point , neighbors):
        if not point.compressed:
            neighbors.append(point)
            point.compressed = True

        for element in point.elements:
            if element.type == 1:
                another_point = element.find_another_point(point)

                if not another_point.compressed:
                    self.find_neighbors(another_point , neighbors)
# ---------------------------------------------------------------------------------------------

grid = Grid()
grid.init_points()
grid.add_element(1 , 1 , 1 , 2 , 1 , 5)
grid.add_element(2 , 1 , 1 , 1 , 2 , 5)
grid.add_element(1 , 1 , 1 , 2 , 2 , 5)

active_points = []
grid.find_active_points(active_points)

for i in active_points:
    print(i.x , i.y)

