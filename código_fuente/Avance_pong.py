
#Librería gráfica para crear el juego Pong

import turtle

#Especificar las dimensiones de la ventana del juego

s = turtle.Screen()
s.setup(800,600)
s.bgcolor("black")
s.tracer(0)

#Diseñar el tamaño de las paletas y posicionarlas a cada lado de la ventana del juego

def paleta(x):
    t=turtle.Turtle();t.shape("square");t.color("white")
    t.shapesize(5,1);t.penup();t.goto(x,0)
    return t

l,r=paleta(-350),paleta(350)

#Diseño de la pelota

b=turtle.Turtle();b.shape("square");b.color("white");b.penup()

#Velocidad de la pelota

b.dx=b.dy=0.09

#Funciones del movimiento de las paletas

def mover_paleta(t, d):
    nueva_y = t.ycor() + d
    t.sety(nueva_y)

def izquierda_arriba():
    mover_paleta(l, 20)

def izquierda_abajo():
    mover_paleta(l, -20)

def derecha_arriba():
    mover_paleta(r, 20)

def derecha_abajo():
    mover_paleta(r, -20)

#Controles de las paletas con el teclado

s.listen()
s.onkeypress(izquierda_arriba, "w")
s.onkeypress(izquierda_abajo, "s")
s.onkeypress(derecha_arriba, "Up")
s.onkeypress(derecha_abajo, "Down")

#Bucle principal del juego

while True:
    s.update()
    b.setx(b.xcor()+b.dx); b.sety(b.ycor()+b.dy)
    if abs(b.ycor())>290: b.dy*=-1
    if abs(b.xcor())>390: b.goto(0,0); b.dx*=-1
    for paleta,x in ((l,-340),(r,340)):
        if abs(b.ycor()-paleta.ycor())<50 and x-10<b.xcor()<x+10:
            b.dx*=-1
