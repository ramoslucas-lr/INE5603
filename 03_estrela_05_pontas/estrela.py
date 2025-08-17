import turtle

t = turtle.Turtle()


pontas = 5
print("Só funciona para número ímpar de pontas. Para par precisa fazer outra coisa que não pensei :)")

for _ in range(pontas):
    t.forward(100)
    t.left((360/pontas)*((pontas-1)/2))

turtle.done()