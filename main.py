import colorgram
colors = colorgram.extract("image.jpg", 10)
import random
import turtle as turt_mod
turt_mod.colormode(255)

rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    col = (r, g, b)
    rgb_colors.append(col)
timothy = turt_mod.Turtle()
timothy.pu()

pallete = [(28, 37, 55), (226, 232, 242), (236, 154, 96), (229, 215, 86), (132, 165, 204), (202, 135, 144),
           (155, 29, 27)]

timothy.setpos(-300, -250)
dots = 70

for dot in range(1, 85):
    timothy.dot(20, random.choice(pallete))
    timothy.fd(100)

    if dot % 7 == 0:
        timothy.setheading(90)
        timothy.fd(50)
        timothy.setheading(180)
        timothy.fd(700)
        timothy.setheading(0)


screen = turt_mod.Screen()
screen.exitonclick()



