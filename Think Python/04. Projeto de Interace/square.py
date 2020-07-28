import turtle

t = turtle.Turtle()

def square(t, length):
    #reset
    t.pu()
    t.bk(100)
    t.pd()

    for i in range(4):
        t.fd(length)
        t.lt(90)


    turtle.mainloop()

        

square(t,200)

    

