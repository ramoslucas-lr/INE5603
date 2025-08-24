import turtle
import math

t = turtle.Turtle()
t.color("orange")

raio_inicial = 50
num_laranjas = 6
aumento_raio = 10

for raio in range(raio_inicial, aumento_raio*num_laranjas+raio_inicial, aumento_raio):
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

    entre_circulo = math.sqrt(math.pow((2*raio+aumento_raio), 2) - math.pow(aumento_raio, 2))
    t.up()
    t.forward(entre_circulo)
    t.down()


turtle.done()


