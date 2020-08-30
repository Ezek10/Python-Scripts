"""Mi consigna (leela bien esta vez) (consejo, copiala en el main de tu proyecto, como resumen....)
Tu trabajo es crear una interfaz grafica (pantalla), en la cual existan 2 objetos (no se ahora si en python se pueden definir clases, pero si se puede, esa es la idea)
-Los objetos no tienen por que tener forma definida, podes hacer un punto o un rectangulo (puntos extra si tienen un pixelart)
-Objeto_1 debe comenzar estático.
-Objeto_2 debe comenzar con una velocidad (hacia Objeto_1).
-Objeto_2 debe tener una Masa2 = Masa1*(100^n)
-los objetos colisionan entre si con choques ELÁSTICOS (física, no se pierde energía en el impacto.)
-No hay fricción.
-Si Objeto_1 colisiona con el borde de la ventana (no puede "spawnear" pegado a esta), rebota elasticamente como si impactara un objeto de masa INFINITA (basicamente cambia de dirección con su misma velocidad).

Esas son las reglas del programa. Ya que ya sabes hacer cosas graficas, te permito revisar tus cosas (o las de la facu digamos) pero trata de no buscar en internet, ya que es un problema conocido.

Lo mas importante es las clases de los objetos (que tengan variables de posicion, velocidad, y todas esas cosas, para mas adelante).
y el tema de colisiones.
si queres, podes agregar el tema del proyecto anterior (mandar wpp) para enviarme la cuenta de colisiones.
podes buscar la formula del choque elastico si queres xD (no me la acuerdo de memoria)"""

import tkinter as tk
from tkinter.constants import *

class Objetos ():

    def __init__(self,vel=0,masa=1):
        """Constructor"""
        self.__masa__ = masa
        self.__velocidad__ = vel
    
    def GetMasa(self):
        return self.__masa__

    def GetVelocidad(self):
        return self.__velocidad__

    def SetVelocidad(self,vel):
        self.__velocidad__ = vel

def Choque(objeto1 = Objetos(), objeto2=Objetos(), pared=True):
    if not hasattr(Choque,"contador"):
        Choque.contador = 1
    else:
        Choque.contador += 1
    
    if pared:
        objeto1.SetVelocidad (-objeto1.GetVelocidad())
    else:
        nuevaVelocidadObjeto1 = (objeto1.GetVelocidad()*(objeto1.GetMasa() - objeto2.GetMasa()) + 2*objeto2.GetMasa()*objeto2.GetVelocidad())/(objeto1.GetMasa() + objeto2.GetMasa())
        nuevaVelocidadObjeto2 = (objeto2.GetVelocidad()*(objeto2.GetMasa() - objeto1.GetMasa()) + 2*objeto1.GetMasa()*objeto1.GetVelocidad())/(objeto2.GetMasa() + objeto1.GetMasa())
        objeto1.SetVelocidad(nuevaVelocidadObjeto1)
        objeto2.SetVelocidad(nuevaVelocidadObjeto2)
    
    return Choque.contador

class Simulador():

    def __init__(self):
        self.width = 300
        self.height = 300
        self.Contador = 0
        self.ventana = tk.Tk()
        self.ventana.geometry("300x300")
        self.ventana.title("Simulador")
        self.canvas = tk.Canvas(self.ventana)
        self.canvas.pack(fill = BOTH, expand = YES)
        self.CreateObjetos()
        self.Update()
        self.ventana.mainloop()

    def CreateObjetos (self):
        
        posY = 0.5
        posX1 = 0.2
        posX2 = 0.8
        tamañoCuadrados = 20
        n = 3
        self.texto = tk.StringVar()
        self.texto.set("Colisiones: 0")
        
        self.Label = tk.Label(self.ventana, textvariable = self.texto)
        self.Label.pack(side = TOP, fill = X)
        self.objeto1 = Objetos(vel = 0, masa = 1)
        self.objeto2 = Objetos(vel = -1, masa = 100**n)
        self.cuadrado1 = self.canvas.create_rectangle(posX1 * self.width, posY * self.height, posX1 * self.width + tamañoCuadrados ,posY * self.height + tamañoCuadrados, fill = "#fb0")
        self.cuadrado2 = self.canvas.create_rectangle(posX2 * self.width, posY * self.height, posX2 *self. width + tamañoCuadrados ,posY * self.height + tamañoCuadrados, fill = "#fb0")
    
    def Update (self):

        self.canvas.move(self.cuadrado1,self.objeto1.GetVelocidad(),0)
        self.canvas.move(self.cuadrado2,self.objeto2.GetVelocidad(),0)
        
        if (self.canvas.coords(self.cuadrado1)[2] >= self.canvas.coords(self.cuadrado2)[0]):
            self.Contador = Choque(self.objeto1,self.objeto2,pared = False)

        if (self.canvas.coords(self.cuadrado1)[0] <= 0.1):
            self.Contador = Choque(self.objeto1)
        
        self.texto.set("Colisiones: {0}".format(self.Contador))

        self.ventana.after(10,self.Update)

    def Destructor(self):
        pass

def main():
    Simulador()

if __name__ == "__main__":
    main()