import pygame
import random
import tkinter
from tkinter import *
root = Tk()

##p1 = pygame.image.load("p1.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"p1.png")
##
##p1 = pygame.image.load("p2.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"p2.png")
##
##p1 = pygame.image.load("c4.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"c4.png")
##
##p1 = pygame.image.load("c3.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"c3.png")
##
##p1 = pygame.image.load("b1.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"b1.png")
##
##p1 = pygame.image.load("pi1.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"pi1.png")
##
##p1 = pygame.image.load("pi2.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"pi2.png")
##
##p1 = pygame.image.load("b2.png")
##p1 = pygame.transform.scale(p1,(100,100))
##pygame.image.save(p1,"b2.png")

p2 = pygame.image.load("Question Mark.png")
p2 = pygame.transform.scale(p2,(100,100))
pygame.image.save(p2,"Question Mark.png")

rows = 0
count = 0
x = [1,2,3,4]
clicklist = []
x.append(1)
x.append(2)
x.append(3)
x.append(4)

z = PhotoImage(file = "p1.png")
images = []
images.append((z,1))

z = PhotoImage(file = "p2.png")
images.append((z,1))

z = PhotoImage(file = "b1.png")
images.append((z,2))

z = PhotoImage(file = "b2.png")
images.append((z,2))

z = PhotoImage(file = "c3.png")
images.append((z,3))

z = PhotoImage(file = "c4.png")
images.append((z,3))

z = PhotoImage(file = "pi1.png")
images.append((z,4))

z = PhotoImage(file = "pi2.png")
images.append((z,4))

random.shuffle(images)
print(images)

QuestionMark = PhotoImage(file = "Question Mark.png")

class Tile():
    def __init__(self,row_value,column_value,tile_image):
        self.row_value = row_value
        self.column_value = column_value
        self.tile_image = tile_image
        self.button_state = NORMAL
        self.is_clicked = False
    def show_question_mark(self):
        self.questionmark = Button(root,image = QuestionMark,bg = "aqua",state = self.button_state,command = self.button_click)
        self.questionmark.grid(row = self.row_value, column = self.column_value)
    def show_image(self):
        self.questionmark.config(image = self.tile_image[0])
    def button_click(self):
        if self.is_clicked == False:
            clicklist.append(self)
            self.is_clicked = True
            self.show_image()
            if len(clicklist) == 2:
                if clicklist[0].tile_image[1] == clicklist[1].tile_image[1]:
                    clicklist[0].button_state = DISABLED
                    clicklist[1].button_state = DISABLED
                    clicklist.clear()
                else:
                    clicklist[0].is_clicked = False
                    clicklist[1].is_clicked = False
                    root.update()
                    root.after(1000)
                    clicklist[0].questionmark.config(image = QuestionMark)
                    clicklist[1].questionmark.config(image = QuestionMark)
                    clicklist.clear()
                    
##        else:
##            
        
        
for w in images:
    Tile1 = Tile(rows,count,w)
    count = count + 1
    if count == 4:
        count = 0
        rows = rows + 1
        
        
    Tile1.show_question_mark()


