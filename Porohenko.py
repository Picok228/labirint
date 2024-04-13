import pygame

class Pogonec:
    def __init__(self,x,y,w,h,img,speed, x2,y2):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.x=x
        self.x=x2
        self.y=y
        self.y=y2
    def draw(self,window):
        pygame.draw.rect(window,(225,0,0),self.hitbox)
        window.blit(self.photo,(self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.x += self.speed

        if self.hitbox.x>=self.x:
            self.speed*= -1

        self.hitbox.y += self.speed

        if self.hitbox.y>=self.y:
            self.speed*= -1