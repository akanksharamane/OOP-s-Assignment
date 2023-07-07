class Arithmatics:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        return self.num1 + self.num2
    def Sub(self):
        return self.num1 - self.num2 
    def Div(self):
        return int(self.num1 / self.num2) 
    def Multi(self):
        return self.num1 * self.num2 

def main():

    obj1 = Arithmatics(45,10)
    print("Addition = ",obj1.Add())
    
    obj2 = Arithmatics(34,10)
    print("Subtraction = ",obj2.Sub())

    obj3 = Arithmatics(50,5)
    print("Division = ",obj3.Div())

    obj4 = Arithmatics(4,5)
    print("Multiplication = ",obj4.Multi())

    

if __name__=="__main__":
    main()
