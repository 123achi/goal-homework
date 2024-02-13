from turtle import *


#we want to pait a house

#step 1:  draw a square
speed(2)
width(7)
color("sky blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of squar

#drawing  a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(202)
end_fill()

color("black")
begin_fill()
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
penup()
goto(200,200)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()




