# Courtesy of Coding with Russ on YouTube
# Button class

import pygame

class Button():
    def __init__(self, x ,y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.ishidden = False

    def draw(self, surface):
        if not self.ishidden:
            action = False
            # mouse pos
            pos = pygame.mouse.get_pos()
            #print(pos)
            
            #check conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action
        return False
    
    def hide(self):
        self.ishidden = True

    def show(self):
        self.ishidden = False