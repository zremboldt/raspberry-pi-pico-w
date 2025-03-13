import math

def degreesToRadians(degrees):
  return degrees/360 * 2 * math.pi

# We have a triangle. The hypotenuse is 2. The angle is 60 degrees.
hypotenuse = 180
angle = 30

# What is the length of the adjacent side?
print(hypotenuse * math.cos(degreesToRadians(angle))) # 155.88

# What is the length of the opposite side?
print(hypotenuse * math.sin(degreesToRadians(angle))) # 90.0

# The three corners in a triangle must add up to 180 degrees
# If we know that one is a right angle (90 degrees) and we know that one is 30 degrees, then we know that the third angle must be 60 degrees.