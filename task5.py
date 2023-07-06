class Numbers:
    Value = 0

    def __init__(self):
        self.Value = 0

    def Accept(self):
        self.Value = int(input("Enter a number to do given operations: "))

    def ChkPrime(self):
        i = 0
        Flag = True
        for i in range(2,self.Value):
            if(self.Value%i==0):
                Flag = False
                break
        return Flag
    
    def Factors(self):
        print("Factors of given number is: ")
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                print(i)
            
    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                sum = sum + i
        return sum
            
    def Perfect(self):
        i = 1
        while (i*i<=self.Value):
            if (i*i==self.Value):
                return True
            i = i+ 1
        return False

def main():
    obj = Numbers()
    obj.Accept()
    prime = obj.ChkPrime()
    print("checking if number is prime or not: ",prime)
    obj.Factors()
    sumfactors = obj.SumFactors()
    print("Sum of factors of given number = ",sumfactors)
    is_perfect_sqr = obj.Perfect()
    print("Is perfect square or not: ",is_perfect_sqr)



if __name__=="__main__":
    main()