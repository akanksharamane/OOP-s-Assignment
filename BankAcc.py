class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Accept()

    def Accept(self):
        self.Name = input("Enter the name of account holder: ")
        self.Amount = int(input("Enter the current amount in the account: "))

    def CalculateInterest(self):
        Interest = (self.Amount*1*BankAccount.ROI)/100
        return Interest
    
    def Deposite(self,value):
        self.Amount = self.Amount + value
    def Withdraw(self,value):
        self.Amount = self.Amount - value

    def Display(self):
        print(f"Account holder name : {self.Name}")
        print(f"Amount at {self.Name}'s Account : {self.Amount}")
        print(f"ROI on {self.Amount} for 1 year : {self.CalculateInterest()}")


def main():
    user1 = BankAccount()
    user2 = BankAccount()
    print("Depositing 300 in user1".center(50,"-"))
    user1.Deposite(300)
    user1.Display()

    print("-------------Withdrawing 200 from user2--------------")
    user2.Withdraw(200)
    user2.Display()

if __name__=="__main__":
    main()