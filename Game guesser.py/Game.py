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
screen.blit(ludo_image,(100,350))
screen.blit(candy_crush_image,(100,150))
screen.blit(temple_run_image,(100,250))

subway_rect = pygame.Rect(300, 70, 300, 50)
ludo_rect   = pygame.Rect(300, 170, 300, 50)
candy_rect  = pygame.Rect(300, 270, 300, 50)
temple_rect = pygame.Rect(300, 370, 300, 50)
subway_img_rect = pygame.Rect(100, 50, 100, 100)
ludo_img_rect   = pygame.Rect(100, 350, 100, 100)
candy_img_rect  = pygame.Rect(100, 150, 100, 100)
temple_img_rect = pygame.Rect(100, 250, 100, 100)


correct_answers = [(ludo_img_rect,ludo_rect),(subway_img_rect,subway_rect),(temple_img_rect,temple_rect),(candy_img_rect,candy_rect)]
start_pos = None
end_pos = None
start_rect = None
end_rect = None
score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            clicked_on_valid_area = False
            for i,t in correct_answers:
                if i.collidepoint(start_pos):
                    clicked_on_valid_area = True
                    start_rect = i
                    break
            if clicked_on_valid_area == True:
                pygame.draw.circle(screen,"black",start_pos,7)
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            released_on_valid_area = False
            for i,t in correct_answers:
                if t.collidepoint(end_pos):
                    released_on_valid_area = True
                    end_rect = t
                    break
            if released_on_valid_area == True:
                for i,t in correct_answers:
                    if i == start_rect and t == end_rect:
                        pygame.draw.circle(screen,"green",end_pos,7)
                        pygame.draw.circle(screen,"green",start_pos,7)
                        pygame.draw.line(screen,"green",start_pos,end_pos,7)
                        score += 1
                        break
                    else:
                        pygame.draw.circle(screen,"red",end_pos,7)
                        pygame.draw.circle(screen,"red",start_pos,7)
                        pygame.draw.line(screen,"red",start_pos,end_pos,7)
                


            

    
    
    pygame.display.update()