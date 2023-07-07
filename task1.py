class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        self.Accept()   # if you write here then no need to call Accept() in main()

    def Accept(self):
        self.Radius = float(input("Enter the Radius of a Circle: "))

    def CalculateArea(self):
        self.Area = self.__class__.PI*self.Radius*self.Radius
        
    def CalculateCircumference(self):
        self.Circumference = 2*Circle.PI*self.Radius

    def Display(self):
        print("Area of Circle = ",self.Area)
        print("Area of Circumference = ",self.Circumference)

def main():
    Obj = Circle()
    # Obj.Accept()
    Obj.CalculateArea()
    Obj.CalculateCircumference()
    Obj.Display()

if __name__=="__main__":
    main()