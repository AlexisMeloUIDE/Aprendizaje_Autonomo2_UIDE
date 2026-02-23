#Librería gráfica para crear el juego Pong

import turtle

#Especificar las dimensiones de la ventana del juego

s = turtle.Screen()
s.setup(800,600)
s.bgcolor("black")
s.tracer(0)

#Línea central continua

linea = turtle.Turtle()
linea.color("white")
linea.penup()
linea.goto(0,-300)
linea.setheading(90)
linea.pendown()
linea.forward(600)
linea.hideturtle()

#Diseñar el tamaño de las paletas y posicionarlas

def paleta(x):
    t=turtle.Turtle();t.shape("square");t.color("white")
    t.shapesize(5,1);t.penup();t.goto(x,0)
    return t

l,r=paleta(-350),paleta(350)

#Diseño de la pelota

b=turtle.Turtle();b.shape("square");b.color("white");b.penup()

#Velocidad de la pelota

b.dx=b.dy=0.09

#Variables del juego

score_l = 0
score_r = 0
paused = False

#Marcador

marcador=turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(0,260)

def actualizar_marcador():
    marcador.clear()
    marcador.write(f"{score_l}   |   {score_r}",
                   align="center",
                   font=("Courier",24,"normal"))

actualizar_marcador()

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

#Función de pausa

def toggle_pause():
    global paused
    paused = not paused

#Función reiniciar

def reiniciar():
    global score_l, score_r
    score_l = 0
    score_r = 0
    actualizar_marcador()
    b.goto(0,0)

#Controles del teclado

s.listen()
s.onkeypress(izquierda_arriba,"w")
s.onkeypress(izquierda_abajo,"s")
s.onkeypress(derecha_arriba,"Up")
s.onkeypress(derecha_abajo,"Down")
s.onkeypress(toggle_pause,"p")
s.onkeypress(reiniciar,"r")

#Bucle principal del juego

while True:
    s.update()
    if not paused:
        b.setx(b.xcor()+b.dx); b.sety(b.ycor()+b.dy)
        if abs(b.ycor())>290:
            b.dy*=-1
#Puntajes de jugadores
        if b.xcor()<-390:
            score_r+=1
            actualizar_marcador()
            b.goto(0,0); b.dx*=-1
        if b.xcor()>390:
            score_l+=1
            actualizar_marcador()
            b.goto(0,0); b.dx*=-1
        for paleta,x in ((l,-340),(r,340)):
            if abs(b.ycor()-paleta.ycor())<50 and x-10<b.xcor()<x+10:
                b.dx*=-1