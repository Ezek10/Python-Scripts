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

class Simulador ():

    def __init__(self):
        self.i = 0
        self.ventana = tk.Tk()
        self.ventana.geometry("300x300")

        self.texto = tk.StringVar()
        self.texto.set("Colisiones: 0")

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.pack(fill = BOTH, expand = YES)

        self.CreateObjetos()
        self.Update()

        self.ventana.after(30,self.Update)
        self.ventana.mainloop()

    def CreateObjetos (self):
        
        posY = 0.5
        posX1 = 0.2
        posX2 = 0.8
        tamañoCuadrados = 20
        n = 2
        self.texto = tk.StringVar()
        self.texto.set("Colisiones: 0")
        
        self.Label = tk.Label(self.ventana, textvariable = self.texto)
        self.Label.pack()
        
        self.cuadrado1 = self.canvas.create_rectangle(posX1 * 300, posY * 300, posX1 * 300 + tamañoCuadrados ,posY * 300 + tamañoCuadrados, fill = "#fb0")
        self.cuadrado2 = self.canvas.create_rectangle(posX2 * 300, posY * 300, posX2 * 300 + tamañoCuadrados ,posY * 300 + tamañoCuadrados, fill = "#fb0")

        self.objeto1 = Objetos(vel = 0, masa = 1)
        self.objeto2 = Objetos(vel = -1, masa = 100**n)

    def Update(self):
        self.i+=1
        self.texto.set("{0}".format(self.i))
        self.canvas.move(self.cuadrado1,1,0)
        self.ventana.after(30,self.Update)

def main():
    Simulador()

if __name__ == "__main__":
    main()
