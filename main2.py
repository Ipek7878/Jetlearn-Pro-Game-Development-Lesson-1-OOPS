import pygame

pygame.init()

screen=pygame.display.set_mode((800,800))

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

screen.fill('pink')

class Rect():
    def __init__(self,color,dimensions):
        self.screen=screen
        self.color=color
        self.dimensions=dimensions
    
    def draw_rect(self):
        self.rect_draw=pygame.draw.rect(self.screen,self.color,self.dimensions)
    

#The first 2 numbers indicate the position while the last 2 numbers show the size of the rectangle
greenRect= Rect(green,(50,20,100,120))
greenRect.draw_rect()

redRect = Rect(red,(100,380,150,186))
redRect.draw_rect()

blueRect=Rect(blue,(500,100,100,50))
blueRect.draw_rect()

yellowRect=Rect('yellow',(700,200,100,80))
yellowRect.draw_rect()

lightblueRect= Rect('light blue',(280,470,300,250))
lightblueRect.draw_rect()

purpleRect= Rect('purple',(80,600,100,20))
purpleRect.draw_rect()









while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()