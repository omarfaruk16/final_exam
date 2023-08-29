class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.total_ballance = 0
        self.total_lone = 0
        self.lone_process_enable = True
        self.users = []
        self.admins = []

    def create_user_account(self, name,email):
        user = User(name,email)
        self.users.append(user)
        return f"User '{name}' account created."
    
    def create_admin_account(self, name,email):
        admin = Admin(name,email)
        self.admins.append(admin)
        return f"Admin '{name}' account created."

    def change_loan_process(self):
        self.lone_process_enable = not self.lone_process_enable
        status = "enabled" if self.lone_process_enable else "disabled"
        return f"Loan process has been {status}."
    
    def see_users(self):
        for i in self.users:
            print(i," ")

    

from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email

    @abstractmethod
    def see_profile(self):
        print(f'Name = {self.name} \nEmail = {self.email}')
    

class User(Employee):
    def __init__(self, name,email) -> None:
        self.total_ammount = 0
        self.total_deposit = 0
        self.total_withdraw = 0
        self.total_received = 0
        self.total_transfar = 0
        super().__init__(name, email)

    def deposit(self, ammount, bank):
        self.total_ammount+=ammount
        bank.total_ballance +=ammount
        self.total_deposit+=ammount
    
    def withdraw(self,ammount, bank):
        if ammount > 0 and ammount < self.total_ammount and bank.total_ballance >= ammount:
            self.total_withdraw+=ammount
            bank.total_ballance -=ammount
            self.total_ammount-=ammount
        elif self.total_ammount < ammount:
            print(f"You can withdraw less than {self.total_ammount}. ")

        elif bank.total_ballance < ammount:
            print("the bank is bankrupt.")

    def take_lone(self, ammount, bank):
        if bank.lone_process_enable and bank.total_ballance >= ammount*2: 
            self.total_ammount += ammount
            bank.total_ballance -= ammount
            bank.total_lone += ammount
            print(f"{self.name} is taking lone {ammount} taka. Please return this money as early as possible")


    def check_transaction_history(self):
        print(f'''
              Hello {self.name}\n
              Your total deposit = {self.total_deposit}
              Your total withdraw = {self.total_withdraw}
              Your transfar money = {self.total_transfar}
              Your total received money = {self.total_received}
              Your current money = {self.total_ammount}
              ''')

    def available_ammount(self):
        print(self.total_ammount)

    def see_profile(self):
        return super().see_profile()
    
    def transfer(self,other,ammount):
        if(self.total_ammount > ammount):
            print(f"Transfaring {ammount} taka from {self.name} to {other.name}")
            self.total_ammount -=ammount
            self.total_transfar +=ammount
            other.total_ammount +=ammount
            other.total_received +=ammount

        else:
            print(f'{self.name}, You have not enough money.')

      

class Admin(Employee):
    def __init__(self, name, email) -> None:
        super().__init__(name, email)

    def see_profile(self):
        return super().see_profile()

    def check_total_ballance(self, bank):
        return f'Current bank balance = {bank.total_ballance}'
    
    def check_total_lone(self, bank):
        return f'Current lone = {bank.total_lone}'
    
    def change_lone_taken_option(self,bank):
        return bank.change_loan_process()



sonar_bank = Bank('Sonar Bank')
sonar_bank.create_user_account('omar','omar@gamil.com')
sonar_bank.create_user_account('faruk','faruk@gamil.com')
sonar_bank.create_user_account('khan','khan@gmail.com')
sonar_bank.create_admin_account('arnob','arnob@gmail,com')

omar = sonar_bank.users[0]
omar.deposit(50,sonar_bank)
print(omar.total_ammount)

# sonar_bank = Bank('Sonar_Bank')
# omar = User('Omar','ukomarkhan16800@gmail.com',50)
# omar.see_profile()
# omar.deposit(50)
# omar.withdraw(60)
# omar.deposit(30)
# omar.withdraw(60)
# print(omar.total_ammount)
# faruk = User('Faruk','faruk@gmail.com',40)
# omar.transfer(faruk,9)
# print(omar.total_ammount)
# print(faruk.total_ammount)
# omar.check_transaction_history()
# faruk.check_transaction_history()
# sonar_bank.see_users()