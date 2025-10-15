from graphics import*

def japan():
    win = GraphWin("yapan", 1200, 700)
    win.setBackground(color_rgb(255, 255, 255))
    pt = Point(600, 350)
    cir = Circle(pt, 150)
    cir.setFill(color_rgb(255,0, 0))
    cir.draw(win)
    #line = Line(Point(450, 350), Point(750, 350))
    #line.setWidth(5)
    #line.draw(win)
    #line2 = Line(Point(600, 500), Point(600, 200))
    #line2.setWidth(5)
    #line2.draw(win)
    win.getMouse()
    win.close()
#japan()

def phil(): 
    x = 1400
    y = 800
    x2 = x / 2
    y2 = y / 2
    xcp = 690
    
    blue = color_rgb(0, 71, 171)
    red = color_rgb(230, 43, 43)
    white = color_rgb(255, 255, 255)
    yellow = color_rgb(250, 215 , 30)
    
    win = GraphWin("pilipens", x, y)
    win.setBackground(white)
    
    #upper star
    star1 = Polygon(Point(25, 85),  #Point 1
                    Point(53, 105), #Point 2
                    Point(80, 85),  #Point 3
                    Point(53, 168)) #Point 4
    
    star2 = Polygon(Point(10, 135), #Point 5
                    Point(80, 85),  #Point 6
                    Point(70, 115), #Point 7
                    Point(95,135))  #Point 8
    
    #lower star
    star3 = Polygon(Point(25, 710), #Point 1
                    Point(53, 690), #Point 2
                    Point(80, 710), #Point 3
                    Point(53, 628)) #Point 4

    
    star4 = Polygon(Point(10, 660), #Point 5
                    Point(80, 710), #Point 6
                    Point(70, 680), #Point 7
                    Point(95, 660)) #Point 8

    #middle star
    star5 = Polygon(Point(592, 400),    #Point 1
                    Point(510, 428),    #Point 2
                    Point(529, 400),    #Point 3
                    Point(510, 372))    #Point 4
    
    star6 = Polygon(Point(560, 443),    #Point 5
                    Point(560, 358),    #Point 6
                    Point(510, 428),    #Point 7
                    Point(540, 416)   #Point 8
                    )
    
    

    star1.setFill(yellow)
    star1.setOutline(yellow)
    star1.draw(win)
    
    star2.setFill(yellow)
    star2.setOutline(yellow)
    star2.draw(win)
    
    star3.setFill(yellow)
    star3.setOutline(yellow)
    star3.draw(win)
    
    star4.setFill(yellow)
    star4.setOutline(yellow)
    star4.draw(win)
    
    star5.setFill(yellow)
    star5.setOutline(yellow)
    star5.draw(win)
    
    star6.setFill(yellow)
    star6.setOutline(yellow)
    star6.draw(win)
    
    sun = Circle(Point(225, y2), 90)
    sun.setFill(yellow)
    sun.draw(win)
    sun.setOutline(yellow)
    
    box1 = Rectangle(Point(xcp, 0), Point(x, y2))
    box1.setFill(blue)
    box1.draw(win)
    
    box2 = Rectangle(Point(xcp, y), Point(x, y2))
    box2.setFill(red)
    box2.draw(win)
    
    tri1 = Polygon(Point(0, 0), Point(xcp, y2), Point(xcp, 0))
    tri1.setFill(blue)
    tri1.setOutline(blue)
    tri1.draw(win)
    
    tri2 = Polygon(Point(0, y), Point(xcp, y2), Point(xcp, y))
    tri2.setFill(red)
    tri2.setOutline(red)
    tri2.draw(win)

    win.getMouse()
    win.close()
        
phil()