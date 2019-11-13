class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0;
        self.Area=0.0;
        self.Circumference=0.0;

    def Accept(self,radius):
        self.Radius=radius


    def CalculateArea(self):
        self.Area=self.PI*self.Radius*self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        return self.Circumference

    def Display(self):
        print("Area ",self.CalculateArea())
        print("Circumference ",self.CalculateCircumference())


def main():
    Obj1 = Circle()
    Obj1.Accept(5)
    Obj1.Display()


if __name__=="__main__":
    main();