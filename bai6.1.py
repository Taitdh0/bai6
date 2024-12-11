print ("Tran Tuan Tai")
print("235752021610014")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Ví dụ sử dụng class Circle
radius = float(input("Nhập bán kính của hình tròn: "))
circle = Circle(radius)
print(f"Diện tích của hình tròn là: {circle.area()}")
