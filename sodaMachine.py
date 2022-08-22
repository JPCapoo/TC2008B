ActionObject = {
            'moneda':'pedir-codigo',
            'moneda,a1':'servir-bebida1',
            'moneda,a2':'servir-bebida2',
            'moneda,a3':'servir-bebida3'
        }
            
class Agent:
    def __init__(self, actions):
        self.actions = actions
        self.input = ''
    
    def checkPayment(input):
        if(input):
            return True
        print('Ingrese una moneda');
        return False
        
    def actuar(self, input, functions=''):
        if not input:
            return functions
        if input in self.actions.keys():
            print('Preparando...')
            return self.actions[input]
        return functions

sodaMachine = Agent(ActionObject)

while(True):
    coin = input(str('Please Insert a Coin: '))

    if(not Agent.checkPayment(input)):
        break;

    service = input(str('Please Select Your Service: '))

    sodaMachine.actuar(coin, service);



