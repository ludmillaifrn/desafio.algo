from turtle import Turtle,onscreenclick, onkey, listen, Screen
turtle = Turtle ()
tela = Screen()

turtle.forward(200)
turtle.backward(200)
turtle.right(90)
turtle.forward(200)
turtle.left(180)
turtle.forward(200)
turtle.forward(200)
turtle.backward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(180)
turtle.forward(200)

def goto_and_mark(x, y):
    turtle.goto(x, y)
    turtle.write(turtle.position())

turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)


listen()
tela.mainloop()