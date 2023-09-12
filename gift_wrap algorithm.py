class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
            # May want to throw an exception if area == 0
    return area > 0 

def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def classify_points(line_start, line_end, points):
    """Takes an infinite line, with a start and end, and a list of points
    Returns a two tuple of integers."""
    right = 0
    left = 0
    left_dist = 0
    right_dist = 0
    if signed_area(line_start, line_end, points) > 0:
        left += 1
        left_dist += signed_area(line_start, line_end, points)
    elif signed_area(line_start, line_end, points) < 0:
        right_dist += signed_area(line_start, line_end, points)
        right += 1
    if left > 0:
        return ('Left', left_dist)
    else:
        return ('Right', right_dist)

def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False

    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None: # ** FIXME **
                candidate = p
            elif  classify_points(hull[-1], candidate, p) > 0:
                candidate = p
                
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

def is_strictly_convex(vertices):
    """Returns true if all interior angles of lines are less than 180 degrees"""
    #Checks if the points are to the left of the line made by i and i + 1
    for i in range(len(vertices)):
        if i + 2 < len(vertices):
            if classify_points(vertices[i], vertices[i + 1], vertices[i + 2]) == 0:
                return False
    
    #Checks the lines that were at the start and end of the lists, to loop it around
    if len(vertices) > 2:
        #Create a closed loop
        vertex_list = vertices[-2:] + vertices[:2]
        for i in range(len(vertex_list)):
            if i + 2 < len(vertices):
                if classify_points(vertex_list[i], vertex_list[i + 1], vertex_list[i + 2]) == 0:
                    return False            
                           
    return True

from functools import cmp_to_key # Converts a cmp function to a key function
def cmp(p1, p2):
    """Compares two points with respect to a globally defined anchor point.
    Returns a negative, zero or positive value according to whether p1 is
    to the right of p2 ("p1 < p2"), collinear with it ("p1 == p2") or to
    the left ("p1 > p2").
    """
    v1 = p1 - anchor
    v2 = p2 - anchor
    if v1.lensq() == 0: # Is p1 the anchor point (or a copy of it)?
        return -1 # Yes. Make sure anchor point < everything else
    elif v2.lensq() == 0: # Is p2 the anchor point (or a copy of it)?
        return +1 # Yes, Make sure all other points > anchor
    else: # In all other cases, return the negative of the usual area
        return v2.x * v1.y - v1.x * v2.y # This is negative if p1 < p2


def simple_polygon(points):
    """Creates a simple polygon, ordered by angles"""
    order = []
    y = float('inf')
    for item in points:
        if item.y < y:
            y = item.y
            best = item
    
    

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = simple_polygon(points)
for v in verts:
    print(v)
print('\n')
    
points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = simple_polygon(points)
for v in verts:
    print(v)