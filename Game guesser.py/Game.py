import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("#FEFFFEFF")
subway_surfers_image_b = pygame.image.load("pygame/Game guesser.py/images/subwaysurfer.png")
ludo_image_b = pygame.image.load("pygame/Game guesser.py/images/ludo.png")
candy_crush_image_b = pygame.image.load("pygame/Game guesser.py/images/candycrush.jpg")
temple_run_image_b = pygame.image.load("pygame/Game guesser.py/images/templerun.png")
subway_surfers_image = pygame.transform.scale(subway_surfers_image_b,(100,100))
ludo_image = pygame.transform.scale(ludo_image_b,(100,100))
candy_crush_image = pygame.transform.scale(candy_crush_image_b,(100,100))
temple_run_image = pygame.transform.scale(temple_run_image_b,(100,100))
font = pygame.font.SysFont("sansserifcollection",40)
Subway_surfers = font.render("Subway surfers",True,"#000000")
Candy_crush = font.render("Candy crush",True,"#000000")
Ludo = font.render("Ludo",True,"#000000")
Temple_run = font.render("Temple run",True,"#000000")
screen.blit(Subway_surfers,(300,50))
screen.blit(Ludo,(300,150))
screen.blit(Candy_crush,(300,250))
screen.blit(Temple_run,(300,350))

screen.blit(subway_surfers_image,(100,50))
screen.blit(ludo_image,(100,150))
screen.blit(candy_crush_image,(100,250))
screen.blit(temple_run_image,(100,350))

# Rechthoeken voor de teksten
subway_rect = pygame.Rect(300, 70, 300, 50)
ludo_rect   = pygame.Rect(300, 170, 300, 50)
candy_rect  = pygame.Rect(300, 270, 300, 50)
temple_rect = pygame.Rect(300, 370, 300, 50)
subway_img_rect = pygame.Rect(100, 50, 100, 100)
ludo_img_rect   = pygame.Rect(100, 150, 100, 100)
candy_img_rect  = pygame.Rect(100, 250, 100, 100)
temple_img_rect = pygame.Rect(100, 350, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()