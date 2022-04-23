#Tictactoe.py
#A program to show the graphical representation of the result
#of a tic-tac-toe game
#By Ashley Cook

import graphics
from graphics import*

def main():
    print("Here is a graphical representation of a game of Tic-Tac-Toe")
    win = graphics.GraphWin("Tic-Tac-Toe", 300, 300)
    win.setCoords(0,0,3,3)
    win.setBackground('black')
    #Setup Grid
    Line(Point(1,0),Point(1,3)).draw(win).setOutline('cyan')
    Line(Point(2,0),Point(2,3)).draw(win).setOutline('cyan')
    Line(Point(0,1),Point(3,1)).draw(win).setOutline('cyan')
    Line(Point(0,2),Point(3,2)).draw(win).setOutline('cyan')    
    #Plot X1
    line1 =Line(Point(0.2, 0.2),Point(0.8,0.8))
    line2 = Line(Point(0.8,0.2),Point(0.2,0.8))
    line1.setWidth(3)
    line1.setFill('pink')
    line1.draw(win)
    line2.setWidth(3)
    line2.setFill('pink')
    line2.draw(win)
    #Plot X2
    line3= line1.clone()
    line3.move(0,1)
    line3.draw(win)
    line4=line2.clone()
    line4.move(0,1)
    line4.draw(win)
    #Plot X3
    line5=line3.clone()
    line5.move(0,1)
    line5.draw(win)
    line6=line4.clone()
    line6.move(0,1)
    line6.draw(win)
    #Plot X4
    line7=line5.clone()
    line7.move(2,0)
    line7.draw(win)
    line8=line6.clone()
    line8.move(2,0)
    line8.draw(win)
    #Plot O1
    o1= Circle(Point(1.5,2.5),0.35)
    o1.setOutline('lime')
    o1.setWidth(3)
    o1.draw(win)
    #Plot O2
    o2= o1.clone()
    o2.move(0, -1)
    o2.draw(win)
    #Plot O3
    o3=o2.clone()
    o3.move(1,-1)
    o3.draw(win)
    


    
    
    
main()
