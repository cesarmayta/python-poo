class Automovil:
    
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    def encender(self):
        print('encender ' + self.marca)
        
#creamos objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
print("año : " + str(vw.año))
print("color:" + vw.color)
vw.encender()