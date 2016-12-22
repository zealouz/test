from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

   CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normilize the zero vector.'
   def __init__(self, coordinates):
      try:
         if not coordinates:
            raise ValueError
         
         self.coordinates = tuple([Decimal(x) for x in coordinates]);
         self.dimentions  = len(coordinates);
      except ValueError:
         raise ValueError('The coordinates must be non-empty')
      except TypeError:
         raise ValueError('The coordinates must be iterable')
      
   def __str__(self):
      return 'Vector: {}'.format(self.coordinates);
      
   def __eq__(self, v):        
      return self.coordinates == v.coordinates;
      
      
   def plus(self, v):
      newCoordinates = [x+y for x,y in  zip(self.coordinates, v.coordinates)]
         
      return Vector(newCoordinates);
      
   def minus(self, v):
      newCoordinates = [x-y for x,y in  zip(self.coordinates, v.coordinates)]
      
      return Vector(newCoordinates);
   
   def times_scalar(self, scalar):
      newCoordinates = [x*Decimal(scalar) for x in self.coordinates]
         
      return Vector(newCoordinates);
      
   def magnitude(self):
      newCoordinates = [x**2 for x in self.coordinates]
   
      return Decimal(sqrt(sum(newCoordinates)));
      
   def normalized(self):
      try:
         mag = self.magnitude()
         return self.times_scalar(Decimal('1.0')/mag)
      except ZeroDivisionError:
         raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
         
   def dot(self, v):
      return sum([x*y for x, y in zip(self.coordinates, v.coordinates)]);
      
   def angle_with(self, v, in_degrees = False):
      try:
         u1 = self.normalized();
         u2 = v.normalized();
         angle_in_rad = acos(u1.dot(u2));
         
         if in_degrees:
            degrees_per_radian = Decimal('180.0') / pi
            return angle_in_rad * degrees_per_radian;
         else:
            return degrees_per_radian;
            
      except Exception as e:
         if (str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG):
            raise Exception('Cannot compute an angle with zero vector')
         else:
            raise e
            
   def is_parallel_to(self, v):
      return (self.is_zero() or
              v.is_zero() or
              self.angle_with(v) == 0 or
              self.angle_with(v) == pi )
        
   def is_orthogonal_to(self, v, tolerance=1e-10):
      return abs(self.dot(v)) < tolerance
      
   def is_zero(self, tolerance = 1e-10):
      return self.magnitude() < tolerance
            
#v1 = Vector([8.218, -9.341])
#v2 = Vector([-1.129, 2.111])

#print v1.plus(v2)

#v1 = Vector([7.119, 8.215])
#v2 = Vector([-8.223, 0.878])

#print v1.minus(v2)

#v1 = Vector([1.671, -1.012, -0.318])
#print v1.times_scalar(7.41)

#v1 = Vector([-0.221, 7.437])
#print v1.magnitude();

#v1 = Vector([8.813, -1.331,-6.247])
#print v1.magnitude();

#v1 = Vector([5.581, -2.136])
#print v1.normalized();

#v1 = Vector([1.996, 3.108, -4.554])
#print v1.normalized();

#v1 = Vector([7.887, 4.138])
#v2 = Vector([-8.802, 6.776])
#print v1.dot(v2)

#v1 = Vector([-5.955, -4.904, -1.874])
#v2 = Vector([-4.496, -8.755, 7.103])
#print v1.dot(v2)
	
#v1 = Vector([3.183, -7.627])
#v2 = Vector([-2.668, 5.319])
#print v1.angle_with(v2)

#v1 = Vector([7.35, 0.221, 5.188])
#v2 = Vector([2.751, 8.259, 3.985])
#print v1.angle_with(v2, True)

v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([-2.029, 9.97, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)

v1 = Vector([2.118, 4.827])
v2 = Vector([0,0])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)


