from tkinter import *
import random
import time
class Pelota:
    def __init__(self,canv,color,raqueta):
        self.canv=canv
        self.raqueta=raqueta
        self.id=canv.create_oval(10,10,25,25,fill=color)
        self.canv.move(self.id,245,100)
        empezar=[-3,-2,-1,1,2,3]
        random.shuffle(empezar)#varia  empezar
        self.x=empezar[0]
        self.y=-3#velocidad hacia arriba
        self.canheight=self.canv.winfo_height()#devuelve altura
        self.canwidth=self.canv.winfo_width()
        self.golpeaf=False
        self.puntos=0

    def golpea(self,pos):
        raqpos=self.canv.coords(self.raqueta.id)
        if pos[2]>=raqpos[0] and pos[0]<=raqpos[2]:
            if pos[3]>=raqpos[1] and pos[3]<=raqpos[3]:
                self.x+=self.raqueta.x
                return True
        return False
            
        
        
    def dibujar(self):
        self.canv.move(self.id,self.x,self.y)
        pos=self.canv.coords(self.id)#regresa 4 numeros como coordenadas x y x1 y1
        if pos[1]<=0:#si  choca arriba
            self.y=2
        if pos[3]>=self.canheight:#si choca abajo
            self.golpeaf=True
        if self.golpea(pos)==True:##golpea raqueta
            self.y=-2
            self.puntos+=1
        if pos[0]<=0:#si  choca de lado
            self.x=2
        if pos[2]>=self.canwidth:#si choca abajo
            self.x=-2


#---------------------------------------------------------------------------------------------------------------------------------------------------------     
class Raqueta:
    def __init__(self,canv,color):
        self.canv=canv
        self.id=canv.create_rectangle(0,0,100,10,fill=color)
        self.canv.move(self.id,200,350)
        self.x=0
        self.canwidth=self.canv.winfo_width()
        self.empezado=False
        self.canv.bind_all("<Button-1>",self.izq)
        self.canv.bind_all("<Button-3>",self.der)
        self.canv.bind_all("<Button-2>",self.comenzar)
        

    def dibujar(self):
        self.canv.move(self.id,self.x,0)
        pos=self.canv.coords(self.id)
        if pos[0]==0:#si  choca de lado
            self.x=0
        elif pos[0]<0:#si  choca de lado
            self.x=1
        if pos[2]==self.canwidth:#si choca abajo
            self.x=0
        if pos[2]>self.canwidth:#si choca abajo
            self.x=-1

    def izq(self,evt):
        self.x=-2

    def der(self,evt):
        self.x=2

    def comenzar(self,evt):
        self.empezado=True
     
        

tk=Tk()
tk.title("pingpong")
tk.resizable(0,0)#inescalable
tk.wm_attributes("-topmost",1)#encima de otras ventanas
canv=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)#bd y el otro no tiene bordes
canv.pack()#visualizar canvas
tk.update()
raqueta=Raqueta(canv,"green")#instancia raqueta
pelota=Pelota(canv,"red",raqueta)#instancia pelota
tper=canv.create_text(250,200,text="PERDISTE",font=("Barbieri-Book",34),state="hidden",fill="purple")
puntos=0
tex=canv.create_text(20,20,text=pelota.puntos,font=("Barbieri-Book",34),fill="red")

while 1:
    if pelota.golpeaf==False and raqueta.empezado==True:
        pelota.dibujar()
        raqueta.dibujar()
        canv.delete(tex)
        tex=canv.create_text(20,20,text=pelota.puntos,font=("Barbieri-Book",34),fill="red")
    if pelota.golpeaf==True:
         time.sleep(0.3)
        
         canv.itemconfig(tper,state="normal")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

