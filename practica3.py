import turtle
import random

window = turtle.Screen()
window.title("Carrera de tortugas")
window.bgcolor("lightblue")
window.setup(width=900, height=500)


t1 =turtle.Turtle()
t1.shape("turtle")
t1.color("Black")
t1.penup() #Levanta el lapiz para no visualizar los "trazos" del movimiento
t1.goto(-300,100) #GoTo es para indicarle a donde tiene que ir el puntero 
t1.speed(1)

t2 =turtle.Turtle()
t2.shape("turtle")
t2.color("Orange")
t2.penup()
t2.goto(-300,-100) #Usa coordenadas en el plano
t2.speed(1)


metaLogo = turtle.Turtle()
#metaLogo.shape("point")
metaLogo.penup()
metaLogo.goto(300,200) #300 es el eje X

if metaLogo.xcor() == 300:
    metaLogo.pendown()
    metaLogo.goto(300,-200)
    """
    Se mantiene sobre el eje X, 
    pero el movimineto es de arriba hacia abajo...
    por lo tanto es en el eje Y
    """


meta = 300

while True:

    avance_T1 = random.randint(1,18)
    avance_T2 = random.randint(1,18)

    if avance_T1 % 2 ==0 or avance_T2 % 2 ==0:
        continue

    t1.forward(avance_T1) #Se utiliza FORWARD para el movimiento de objeto
    t2.forward(avance_T2)

    print (f"La tortuga 1 avanza: {avance_T1} ,para un total de:{t1.xcor()}") #XCOR nos la la coordenada del ejeX
    print (f"La tortuga 2 avanza: {avance_T2} ,para un total de:{t2.xcor()}") #XCOR nos la la coordenada del ejeX
    print("---------------------------------------------------------------")


    if t1.xcor() >=300 or t2.xcor() >= 300:
        break

if t1.xcor() > t2.xcor():
    print("El ganador es la tortuga 1")
elif t1.xcor() < t2.xcor() :
    print("El ganador es la tortuga 2")
else:
    print("Es un empate")




window.exitonclick()
