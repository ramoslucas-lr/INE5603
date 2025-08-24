import turtle


construtor = turtle.Turtle()
construtor.speed(20)

initial_size = 50
size_increase = 20
num_turns = 50

for size in range(initial_size, initial_size + size_increase*(num_turns+1), size_increase):

    construtor.forward(size)
    construtor.right(90)

turtle.done()