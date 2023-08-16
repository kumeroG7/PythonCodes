#Bank Account Operations...

#Exceptions handling
class InvalidAmountError(Exception):
    pass
class BalanceLimitError(Exception):
    pass
class WithdrawalAmountError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    #initialize bank details
    def __init__(self, name, number, balance):
        self.account_name = name
        self.account_number = number
        self.initial_balance = balance
        self.min_withdrwal = 500.00
        self.min_balance = 1000.00
        self.max_balance = 999999999999.00
        self.new_balance = 0

    #display initial account balance
    def display_initial_balance(self):
        print(f'Your account balance is: Ksh. {self.initial_balance}')

    #deposit funds
    def deposit(self,amount):
        if amount < 0: #Prevent entry of negative values
            self.new_balance = self.initial_balance
            raise InvalidAmountError('Amount cannot be less than Ksh. 0.00!')
        else:
            if amount + self.initial_balance > self.max_balance: #Prevent exceeding legal maximum account balance
                self.new_balance = self.initial_balance
                raise BalanceLimitError(f'You cannot exceed maximum account balance of Ksh. {self.max_balance}!')
            else:
                self.new_balance = amount + self.initial_balance
                print(f'Confirmed, You have successfully deposited Ksh. {amount} to your account!\nYour Current balance is Ksh. {self.new_balance}')

    #withdrawing funds
    def withdraw(self,amount):
        if amount <= 0: #Prevent entry of negative values
            self.new_balance = self.initial_balance
            raise InvalidAmountError('Amount cannot be less than Ksh. 0.00!')
        else:
            if amount < self.min_withdrwal: #Implement minimum amount one can withdraw
                self.new_balance = self.initial_balance
                raise WithdrawalAmountError(f'You cannot withdraw an amount less than Ksh. {self.min_withdrwal}!')
            else:
                if self.initial_balance - amount < self.min_balance: #Implement minimum account balance
                    self.new_balance = self.initial_balance
                    raise InsufficientFundsError(f'Sorry, You have insuficient funds to withdraw Ksh. {amount}')
                else:
                    self.new_balance = self.initial_balance - amount
                    print(f'Confirmed, you have succefully withdrawn Ksh. {amount} from your account.\nYour Current balance is Ksh. {self.new_balance}')

    #display new account balance after transactions
    def current_balance(self):
        print(f'Your current balance is: Ksh. {self.new_balance}')
    

#Sample Bank Accounts
Account1 = BankAccount('GeraldSavings', '738535774', 74574854.00)
Account2 = BankAccount('KumeroSalary', '5463782398', 276455.00)
Account3 = BankAccount('FarmersSacco', '293485766678', 543687445877.00)
Account4 = BankAccount('BobMachinery', '54678445', 3894547.00)
Account5 = BankAccount('MilkCoop', '8765678', 863555778000.00)
Account6 = BankAccount('SchoolFee', '23456876', 5346666599)

#list of accounts
accounts = [Account1, Account2, Account3, Account4, Account5, Account6]

#Example usage...with handling exceptions:

#check initial balance
for account in accounts:
    account.display_initial_balance()
#First account
try:
    Account1.deposit(-3456)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')

#Second account
try:
    Account2.withdraw(150)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')

#Third account
try:
    Account3.withdraw(547687657699)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')


#Fourth account
try:
    Account4.withdraw(57950)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')

#Fifth account
try:
    Account5.deposit(999756432000)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')
    
#Sixth account
try:
    Account6.deposit(989000)
except InvalidAmountError as e:
    print('You cannot input negative number:',e)
except BalanceLimitError as e:
    print(f'Your account balance cannot exceed the balance limit:',e)
except WithdrawalAmountError as e:
    print('The amount enterd is below the minimum amount you can withdraw:',e)
except InsufficientFundsError as e:
    print('Insufficient funds:',e)
else:
    print('Transaction was successful.')
finally:
    print('End of Transaction!')

#Display current balance for each account
for account in accounts:
    account.current_balance()


#CODE BY GERALD KUMERO