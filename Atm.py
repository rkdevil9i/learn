'''ATM PROGRAMING'''


def atm():
  while True:
    print('****ATM****')
    print(' for start enter:- run \n for stop enter:- exit')
    d = input(' :-')
    if d == 'run':

      class Atm():

        def __init__(self):
          self.pin = ""
          self.balance = 0
          print(id(self))

          self.menu()

        def menu(self):
          user_input = input("""
            enter 1 for set pin
            enter 2 for cash deposite
            enter 3 fr withdrawl
            enter 4 for check balance
            enter 5 for pin change
            enter 6 for check pin
            enter 7 for back
            Enter:- """)
          if user_input == '1':
            self.set_pin()

          elif user_input == '2':
            self.deposit()

          elif user_input == '3':
            self.withdrawl()

          elif user_input == '4':
            self.check_balance()

          elif user_input == '5':
            self.change_pin()

          elif user_input == '6':
            self.check_pin()

        #pin set by user
        def set_pin(self):
          self.pin = input("enter your pin:-")
          print('pin set succesful')
          self.menu()

        #user deposit his money

        def deposit(self):
          pin = input('enter you pin:-')

          if pin == self.pin:
            balance = int(input('enter your amount'))
            self.balance = self.balance + balance
            print('deposit succesfull')
            print("current balance:-", self.balance)

          else:
            print('invalid pin')

          self.menu()

        #user withdrawl his money

        def withdrawl(self):
          pin = input('enter you pin:-')
          if pin == self.pin:
            balance = int(input('enter your amount'))
            if balance > self.balance:
              print('insufficiant balance')

            else:
              self.balance = self.balance - balance
              print('withdrawl succesfull')
              print("current balance:-", self.balance)

          else:
            print('invalid pin')
          self.menu()

        def check_balance(self):
          pin = input('enter you pin:-')
          if pin == self.pin:
            balance = self.balance
            print(f'your balance is:-  {balance}')

          else:
            print('invalid pin')
          self.menu()

        def change_pin(self):
          pin = input('enter your old pin:-')
          if pin == self.pin:
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pim changed')

          else:
            print('invalid pin')
          self.menu()

        def check_pin(self):
          print("yor pin is ", self.pin)

      user = input('enter name:-')
      user = Atm()
      print(user)
    else:
      break


atm()
