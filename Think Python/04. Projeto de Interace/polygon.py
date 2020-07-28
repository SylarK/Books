import turtle

t = turtle.Turtle()

def polygon(t, n):
    #reset
    t.pu()
    t.bk(100)
    t.pd()

    #
    angulo = 360/n

    for i in range(n):
        t.fd(50)
        t.lt(int(angulo))


    turtle.mainloop()

        

polygon(t, 9)

    

