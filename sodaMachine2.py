REGLAS ={'sin-moneda':'pedir-moneda',
         'con-moneda':'pedir-codigo',
         'a1-selec':'preparando',
         'a2-selec':'preparando',
         'a3-selec':'preparando'}

MODELO ={('sin-moneda','pedir-moneda','moneda'):'con-moneda',
         ('con-moneda','pedir-codigo','a1'):'a1-selec',
         ('con-moneda','pedir-codigo','a2'):'a2-selec',
         ('con-moneda','pedir-codigo','a3'):'a3-selec',
         ('a1-selec','preparando','servida'):'sin-moneda',
         ('a2-selec','preparando','servida'):'sin-moneda',
         ('a3-selec','preparando','servida'):'sin-moneda'}

class AgenteReactivoBasadoenModelos:
    def __init__(self, modelo, reglas, estado_inicial='', accion_inicial=''):
        self.modelo = modelo
        self.reglas = reglas
        self.estado_inicial = estado_inicial
        self.accion_inicial = accion_inicial
        self.accion = None
        self.estado = self.estado_inicial
        self.ult_accion = self.accion_inicial
        self.bebidas = {'a1','a2','a3'}
        
    def actuar(self):
        percepcion = self.obten_percepcion()
        
        if not percepcion:
            return self.accion_inicial

        clave = (self.estado,self.ult_accion,percepcion)

        if clave not in self.modelo.keys():
            self.accion = None
            self.estado = self.estado_inicial
            self.ult_accion = self.accion_inicial
            return self.accion_inicial

        self.estado = self.modelo[clave]

        if self.estado not in self.reglas.keys():
            self.accion = None
            self.estado = self.estado_inicial
            self.ult_accion = self.accion_inicial
            return self.accion_inicial

        accion = self.reglas[self.estado]
        self.ult_accion = accion

        return accion
       
    def sinMoneda(self):
        moneda = int(input("Ingresa una Moneda: "))
        if (moneda < 100):
            return "moneda"
        return " "

    def conMoneda(self):
        bebida = input("Ingresa una Bebida: ")
        if bebida in self.bebidas:
            return bebida
        return ""

    def a1Selec(self):
        print("Servida")
        return "servida"

    def a2Selec(self):
        print("Servida")
        return "servida"

    def a3Selec(self):
        print("Servida")
        return "servida"
    
    def obten_percepcion(self):
        percepcion = ""
        
        if(self.estado == "sin-moneda"):
            percepcion = self.sinMoneda()

        elif (self.estado == "con-moneda"):
            percepcion = self.conMoneda()

        elif(self.estado == "a1-selec"):
            percepcion = self.a1Selec()

        elif(self.estado == "a2-selec"):
            percepcion = self.a2Selec()

        elif(self.estado == "a3-selec"):
            percepcion = self.a3Selec()
            
        return percepcion

expendedora = AgenteReactivoBasadoenModelos(MODELO,REGLAS,'sin-moneda','pedir-moneda')

print("Bienvenido")
while True:
    accion = expendedora.actuar()