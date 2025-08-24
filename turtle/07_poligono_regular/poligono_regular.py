import turtle

tt = turtle.Turtle()
num_lados = 12
tam_lado = 50


for _ in range(num_lados):
    tt.forward(tam_lado)
    tt.left(360/num_lados)

turtle.done()