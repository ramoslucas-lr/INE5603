import turtle


construtor = turtle.Turtle()
construtor.speed(0)

initial_size = 50
size_increase = 2
num_turns = 200

for size in range(initial_size, initial_size + size_increase*(num_turns+1), size_increase):

    construtor.forward(size)
    construtor.right(91)

turtle.done()