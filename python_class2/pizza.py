"""Silly turtle example"""
import turtle
from time import sleep


pizza = turtle.Turtle()
pizza.color('#E3C12A', '#EAB832')
pizza.begin_fill()
pizza.forward(200)
pizza.left(120)
pizza.forward(200)
pizza.left(120)
pizza.forward(200)
pizza.left(120)
pizza.end_fill()
pizza.pensize(30)
pizza.color('#97803B')
pizza.forward(200)
#added this
pizza.left(5)

def pepperoni():
    pizza.left(120)
    pizza.penup()
    pizza.forward(60)
    pizza.pendown()
    pizza.pensize(5)
    pizza.color('red')
    pizza.dot(15, 'red')
    pizza.right(90)


pepperoni()
pepperoni()
pepperoni()
#added these lines to hide turtle arrow
pizza.color('#EAB832')
pizza.penup()
pizza.right(120)
pizza.forward(30)
sleep(10)
