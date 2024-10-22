import os 
import pygame
import time

pygame.init()
pygame.mixer.init()

WHITE = (255,255,255)
BLACK = (0, 0, 0)
DARK_GREEN = (2, 48, 32)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano")

BORDER = pygame.Rect(WIDTH//4, 0, 100, 200)


FPS = 60


def C_note():
    pygame.draw.rect(WIN, WHITE, pygame.Rect(1, 300, 100, 300))
    
    


def draw_window():
    WIN.fill(DARK_GREEN)
    C_note()
    
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "C3.mp3"))
                    sounda.play()    
                if event.key == pygame.K_d:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "D3.mp3"))
                    sounda.play()   
                if event.key == pygame.K_e:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "E3.mp3"))
                    sounda.play() 
                if event.key == pygame.K_f:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "F3.mp3"))
                    sounda.play() 
                if event.key == pygame.K_g:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "G3.mp3"))
                    sounda.play() 
                if event.key == pygame.K_a:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "A3.mp3"))
                    sounda.play() 
                if event.key == pygame.K_b:
                    sounda = pygame.mixer.Sound(os.path.join("Assets", "B3.mp3"))
                    sounda.play() 
    
        draw_window()



if __name__ == "__main__":
    main()