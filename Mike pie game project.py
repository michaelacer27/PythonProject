#Import library
import pygame
from pygame.locals import *
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))



self.surf.fill((255, 255, 255))
self.rect = self.surf.get_rect_(

           


       #Initialize pygame modules
pygame.init()
  
#Create your screen
screen = pygame.display.set_mode((800, 600))
 
#Instantiate our player; right now he's just a rectangle
player = Player()
 
#Set background color
background = pygame.Surface(screen.get_size())
background.fill((0,0,23 ))
 
running = True
while running:
     
    #For loop through the event queue
    for event in pygame.event.get():
        #Check for KEYDOWN event
        #KEYDOWN is a constant defined in pygame.locals, imported earlier
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
            print("Escape")
        #Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
            print("QUIT")        
 
    #Draw background
    screen.blit(background, (0, 0))
    #Draw surf onto screen at coordinates x:400, y:300
    screen.blit(player.surf, (400, 300))
     
    pygame.display.flip()
 
#Exit the Game
pygame.quit()


