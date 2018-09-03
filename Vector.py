#From Udacity Linear Algebra Refresher with Python

from math import sqrt, pi, acos
from decimal import Decimal


class Vector(object):
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

            def plus(self, v):
                new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(new_coordinates)

            def minus(self, v):
                new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(new_coordinates)
                
            def times_scalar(self, c):
                new_coordinates = [c*y for x in self.coordinates, v.coordinates]
            return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def dot(self, v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] * v.coordinates[i])
        return new_coordinates

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute with zero angle')
            else:
                raise e
                
    def plus(self, v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] - v.coordinates[i])
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] * c)
        return Vector(new_coordinates)

    def magnitude(self):
        squares = []
        n = len(self.coordinates)
        for i in range(n):
            squares.append(self.coordinates[i]**2)
        return sqrt(sum(squares))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0/magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
