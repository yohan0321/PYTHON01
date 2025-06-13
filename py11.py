#연습문제 11.1
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def set(self, x, y):
        self.x = x
        self.y = y
        
    def get(self):
        result = (self.x, self.y)
        return result

def test():
    p1 = Point()
    p2 = Point(2, 3)

    p1.show()

    p1.set(10, 20)
    p1.show()

    p2.show()

    x, y = p2.get()
    print(f'x={x}, y={y}')

if __name__ == '__main__':
   test() 
"""

#연습문제 11.2
"""
class Time:
    def __init__(self, h = 0, m = 0):
        self.h = h
        self.m = m

    def display(self):
        if (self.m == 0):
            print(f"{self.h}:{self.m}0")
        else:
            print(f"{self.h}:{self.m}")

    def add(self, other):
        new_h = self.h + other.h
        new_m = self.m + other.m
        if new_m >= 60:
            new_h = new_h + 1
            new_m = new_m - 60
        return Time(new_h, new_m)
    
    @staticmethod
    def is_valid(h, m):     #정적 메서드에서는 self 인수가 필요없음
        if(0 <= h <= 23 and 0<= m <= 59):
            return True
        else:
            return False


def main():
    t1 = Time(9)
    t2 = Time(9, 30)

    t1.display()
    t2.display()

    later = t1.add(Time(1, 15))
    later.display()

    if Time.is_valid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')

if __name__ == '__main__':
    main()
"""



#연습문제 11.3
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getArea(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return x*y

    def getPerimeter(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return (x+y)*2

    def show(self):
        print(f"좌측 상단 꼿지점이 ({self.x1}, {self.y1})이고 ", end='')
        print(f"우측 하단 꼭지점이 ({self.x2}, {self.y2})인 사각형입니다. ", end='')


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')





















                
