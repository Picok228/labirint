import move
import pygame
from Budanov import Player
from Porohenko import Pogonec
from WALL import Wall

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

bacground = pygame.transform.scale(
    pygame.image.load("optimys_prime/img.png"),(700,500)
)

budan = Player(0,0,60,50, "optimys_prime/img_2.png", 2)
poroh = Pogonec(100,300,60,50, "optimys_prime/img_3.png", 2,10,11)

walls = []
walls.append(Wall(100,0,40,160))
walls.append(Wall(100,220,40,160))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
    for wall in walls:
        if wall.rect.colliderect(budan.hitbox):
            if budan.dir == "up":
                budan.hitbox.y +=3
            if budan.dir == "down":
                budan.hitbox.y -=3
            if budan.dir == "right":
                budan.hitbox.x -=3
            if budan.dir == "left":
                budan.hitbox.x +=3

    budan.move()
    pygame.display.flip()
    window.blit(bacground,(5,5))
    budan.draw(window)
    poroh.move()

    for wall in walls :
        wall.draw(window)
    poroh.draw(window)

    fps.tick(60)