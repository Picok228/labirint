import pygame
from Budanov import Player


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

bacground = pygame.transform.scale(
    pygame.image.load("optimys_prime/img.png"),(700,500)
)

budan = Player(100,300,60,50, "optimys_prime/img_2.png", 3)
poroh = Player(100,300,60,50, "optimys_prime/img_3.png", 3)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    budan.move2()
    budan.move()
    budan.move3()
    budan.move4()
    pygame.display.flip()
    window.blit(bacground,(5,5))
    budan.draw(window)
    poroh.draw(window)
    fps.tick(60)