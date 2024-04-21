import move
import pygame
from Budanov import Player
from Porohenko import Pogonec
from WALL import Wall
pygame.mixer.init()
sount = pygame.mixer.Sound("optimys_prime/pirati_karibskogo_morja.mp3")
pygame.mixer.music.load("optimys_prime/pirati_karibskogo_morja.mp3")
pygame.mixer.music.play(-1)
window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

bacground = pygame.transform.scale(
    pygame.image.load("optimys_prime/img_6.png"),(700,500)
)

budan = Player(543,10,39,32, "optimys_prime/img_2.png", 2)
poroh = Pogonec(100,300,39,32, "optimys_prime/img_3.png", 2,10,11)

walls = []
walls.append(Wall(94,70,40,119))
walls.append(Wall(94,247,40,170))
walls.append(Wall(94,69,229,28))
walls.append(Wall(368,69,229,28))
walls.append(Wall(182,132,347,28))
walls.append(Wall(444,97,40,50))
walls.append(Wall(488,135,41,56))
walls.append(Wall(400,256,42,60))
walls.append(Wall(181,350,347,28))
walls.append(Wall(488,258,40,119))
walls.append(Wall(180,215,40,152))
walls.append(Wall(134,255,50,30))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
    if budan.hitbox.colliderect(poroh.hitbox):
        breaks
    for wall in walls:
        if wall.rect.colliderect(budan.hitbox):
            if budan.dir == "up":
                budan.hitbox.y +=6
            if budan.dir == "down":
                budan.hitbox.y -=6
            if budan.dir == "right":
                budan.hitbox.x -=6
            if budan.dir == "left":
                budan.hitbox.x +=6




    budan.move()
    pygame.display.flip()
    window.blit(bacground,(5,5))
    budan.draw(window)
    #poroh.move()

    for wall in walls :
        wall.draw(window)
    poroh.draw(window)

    fps.tick(60)