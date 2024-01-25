#Implement a program that simulates a basic bank account using a BankAccount class.

class BankAccount:
    def __init__(self, account, sold):
        self.account = account
        self.sold = sold    
        
    def transfer(self, amount, people):
        if amount > 0 and amount <= self.sold:
            people.sold += amount
        else :
            print("Invalid transaction")
        
def main():
    user1 = BankAccount("0123456789", 100)
    user2 = BankAccount("9876543210", 0)
    print(user2.sold)
    user1.transfer(50, user2)
    print(user2.sold)

if __name__ == "__main__":
    main()