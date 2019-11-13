class Arithmatic:
    PI=3.14

    def __init__(self):
        self.Value1=0;
        self.Value2=0;

    def Accept(self,value1,value2):
        self.Value1 = value1;
        self.Value2 = value2;

    def Addition(self):
        addition=self.Value1+self.Value2
        print("Addition is",addition)
        return addition

    def Substraction(self):
        substraction = self.Value1 - self.Value2
        print("Substraction is", substraction)
        return substraction

    def Multiplication(self):
        multiplication = self.Value1 * self.Value2
        print("Multiplication is", multiplication)
        return multiplication

    def Division(self):
        division = self.Value1/self.Value2
        print("Division is", division)
        return division


def main():
    Obj1 = Arithmatic()
    Obj1.Accept(10,5)
    Obj1.Addition();
    Obj1.Substraction()
    Obj1.Multiplication()
    Obj1.Division()


if __name__=="__main__":
    main();