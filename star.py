# Write a program that uses the turtle module and a for loop to draw something.
# It doesn’t have to be complicated, but draw something different than we have done in the past. 
# (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over.
# Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

import turtle

star = turtle.Turtle() 
  
for i in range(50): 
    star.forward(50) 
    star.right(144) 
      
turtle.done() 

