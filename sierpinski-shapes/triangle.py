import turtle


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def drawSquare(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[3][0], points[3][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)


def sierpinskiSquare(x, y, ix, iy, myTurtle):
    quad1 = [[x, y], [(x+ix)/2, y], [(x+ix)/2, (y+iy)/2], [x, (y+iy)/2]]
    drawSquare(quad1, 'white', myTurtle)


def tempFun(x, y, ix, iy, myTurtle):
    # 1: copy 1
    sierpinskiSquare((x+ix)/2, y, ix, (y+iy)/2, myTurtle)
    # 1: copy 2
    sierpinskiSquare((x+ix)/2, (y+iy)/2, ix, iy, myTurtle)
    # 1: copy 3
    sierpinskiSquare(x, (y+iy)/2, (x+ix)/2, iy, myTurtle)


def anotherFun(x, y, ix, iy, myTurtle):
    # Focuses only on quadrant 2
    n = 1
    while(n < 5):
        tempFun((x+ix)/2, y, ix, (y+iy)/2, myTurtle)
        tempFun((x+ix)/2, (y+iy)/2, ix, iy, myTurtle)
        tempFun(x, (y+iy)/2, (x+ix)/2, iy, myTurtle)
        x = (x+ix)/2
        y = y
        ix = ix
        iy = (y+iy)/2
        n = n+1

    n = 1
    while(n < 5):
        tempFun((x+ix)/2, y, ix, (y+iy)/2, myTurtle)
        tempFun((x+ix)/2, (y+iy)/2, ix, iy, myTurtle)
        tempFun(x, (y+iy)/2, (x+ix)/2, iy, myTurtle)

        x = (x+ix)/2
        y = (y+iy)/2
        ix = ix
        iy = iy
        n = n+1

    n = 1
    while(n < 5):
        tempFun((x+ix)/2, y, ix, (y+iy)/2, myTurtle)
        tempFun((x+ix)/2, (y+iy)/2, ix, iy, myTurtle)
        tempFun(x, (y+iy)/2, (x+ix)/2, iy, myTurtle)

        x = x
        y = (y+iy)/2
        ix = (x+ix)/2
        iy = iy
        n = n+1


def main():
    myTurtle = turtle.Turtle()
    myScreen = turtle.Screen()
    x = 100
    ix = -100
    y = 100
    iy = -100
    myPoints = [[x, y], [ix, y], [ix, iy], [x, iy]]
    drawSquare(myPoints, 'red', myTurtle)
    quad1 = [[x, y], [(x+ix)/2, y], [(x+ix)/2, (y+iy)/2], [x, (y+iy)/2]]
    drawSquare(quad1, 'white', myTurtle)
    tempFun(x, y, ix, iy, myTurtle)

    # Focuses only on quadrant 2
    anotherFun(x, y, ix, iy, myTurtle)
    anotherFun((x+ix)/2, (y+iy)/2, ix, iy, myTurtle)
    anotherFun(x, (y+iy)/2, (x+ix)/2, iy, myTurtle)
    myScreen.exitonclick()


main()


# def main():
#     myTurtle = turtle.Turtle()
#     myWin = turtle.Screen()
#     myPoints = [[100, -100], [-100, -100], [-100, 100], [100, 100]]
#     sierpinski(myPoints, 3, myTurtle)
#     myWin.exitonclick()
