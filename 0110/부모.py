class personal_client :
    def __init__(self,a,b) :
        self.name = a
        self.balance = b

    def get_balance(self):
        return self.balance
    
    def insert(self,KRW):
        self.balance +=KRW

class Bubin_client(personal_client):
    def widthraw(self,KRW):
        return self.balance-KRW
    
Client1 = personal_client(1234,50000)
print(Client1.get_balance())
Client1.insert(20000)
print(Client1.get_balance())

Bubinclient1 =Bubin_client(2222,90000)
print(Bubinclient1.get_balance())
print(Bubinclient1.widthraw(10000))
