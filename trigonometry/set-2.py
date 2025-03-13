import math

def degreesToRadians(degrees):
  return degrees/360 * 2 * math.pi

# We have a triangle. The hypotenuse is 2. The angle is 60 degrees.
hypotenuse = 2
angle = 60

# What is the length of the opposite side?
print(hypotenuse * math.cos(degreesToRadians(angle))) # 1.0

# What is the length of the adjacent side?
print(hypotenuse * math.sin(degreesToRadians(angle))) # 1.73

# The three corners in a triangle must add up to 180 degrees
# If we know that one is a right angle (90 degrees) and we know that one is 30 degrees, then we know that the third angle must be 60 degrees.