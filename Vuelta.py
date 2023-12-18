import tkinter as tk
import random
import math
import json

objetos=[]
numerosats=10

#Clase objeto "Objetos"
class Objetos:
    def __init__(self):
        self.centrox = 512
        self.centroy = 512
        self.radioS = 30
        self.radioM = 300
        self.direccion = random.randint(0,360)
        self.color1 = "blue"
        self.color2 = "green"
        self.color3="grey"
        self.grosorborde=10
        self.entidad=""
        self.velocidad = random.randint(1,10)
        self.a=random.randint(2,8)
        self.b=random.randint(1,4)
        
#Método visualizar propiedades tierra
    def visualizarT(self):
        lienzo.create_oval(
            self.centrox-self.radioM/2,
            self.centroy-self.radioM/2,
            self.centrox+self.radioM/2,
            self.centroy+self.radioM/2,
            fill=self.color1,
            outline=self.color2,
            width=self.grosorborde)
        
#Método visualizar propiedades satélites
    def visualizarS(self):
        self.entidad=lienzo.create_oval(
            self.centrox-self.radioS/2,
            self.centroy-self.radioS/2,
            self.centrox+self.radioS/2,
            self.centroy+self.radioS/2,
            fill=self.color3)
        
#Movimientos elípticos de los satélites
    def mueve(self):
        self.direccion += math.radians(self.velocidad)
        x = self.centrox + self.a * math.cos(self.direccion)
        y = self.centroy + self.b * math.sin(self.direccion)
        lienzo.move(self.entidad, x - self.centrox, y - self.centroy)

#Método guardar posición de cada objeto (satélites)
def guardarPosicion():
    print("Guardar posicion")
    cadena=json.dumps([vars(objeto) for i in objetos])
    archivo=open("C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\ACCESO A DATOS\\Practicas\\Practica6AD\\satelite.json","w")
    archivo.write(cadena)
    archivo.close()
                 
raiz=tk.Tk()

#Lienzo
lienzo=tk.Canvas(width=1024,height=1024)
lienzo.pack()

#Declaración de objeto
objeto=Objetos()
objeto.visualizarT()

#Introducción de objetos en la lista
for i in range(0,numerosats):
    objetos.append(Objetos())

#Para cada uno de los objetos credos dar un atributo específico
for elemento in objetos:
    elemento.visualizarS()

#Velocidad de movimiento en el tiempo 
def velocidad():    
    for objeto in objetos:
        objeto.mueve()
    raiz.after(10,velocidad)

velocidad()

#Boton para guardar
boton = tk.Button(raiz,text="Guardar", command=guardarPosicion)
boton.pack()
raiz.mainloop()
