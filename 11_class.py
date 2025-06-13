#클래스의 기본 구조 -> 각 메서드는 첫번째 매개변수로 self를 가짐
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getCircumference(self):
        result = 2 * 3.14 * self.radius
        return result

    def getArea(self):
        result = 3.14 * self.radius ** 2
        return result

small = Circle(1)
big = Circle(10)

print(f'반지름 {small.radius}인 원의 ', end='')
print(f'둘레는 {small.getCircumference():.2f}이고, ', end ='')
print(f'넓이는 {small.getArea():.2f}이다.')

print(f'반지름 {big.radius}인 원의 ', end='')
print(f'둘레는 {big.getCircumference():.2f}이고, ', end ='')
print(f'넓이는 {big.getArea():.2f}이다.')

#비공개 속성을 갖는 클래스 -> 객체 외부에서 접근 불가
class Circle:
    __PI = 3.14159265
    
    def __init__(self, radius):
        self.__radius = radius

    @staticmethod
    def getPI():
        return Circle.__PI
        
    def getCircumference(self):
        result = 2 * self.__PI * self.__radius
        return result

    def getArea(self):
        result = self.__PI * self.__radius ** 2
        return result

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius


small = Circle(1)
big = Circle(10)
print(Circle.getPI())


