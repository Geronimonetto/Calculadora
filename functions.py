from strings import msg

class calculadora:

    def __init__(self):
        msg()

    
    def menu(self):
        self.number1 = int(input("Number1: "))
        self.number2 = int(input("Number2: "))
        self.operator = input("Operator [+ - * / ]: ")
    
    def numbers(self):
        if self.operator =="+":
                print(f'A soma dos números {self.number1} + {self.number2} = {self.number1 + self.number2}')
        elif self.operator =="-":
                print(f'A subtração dos números {self.number1} + {self.number2} = {self.number1 - self.number2}')
        elif self.operator =="*":
                print(f'A multiplicação dos números {self.number1} + {self.number2} = {self.number1 * self.number2}')
        elif self.operator =="/":
                print(f'A divisão dos números {self.number1} + {self.number2} = {self.number1 / self.number2}')
        self.menu()

    def msg():
        print('**'*20)
        print("Bem vindo a CALCULADORA")
        print('**'*20)
        
        