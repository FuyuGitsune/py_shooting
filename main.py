import pygame
import sys

SURFACE_WIDTH = 800 #画面幅
SURFACE_HEIGHT = 600 #画面高さ
FPS = 30 #計算実行間隔

def main():
    pygame.init()
    pygame.display.set_caption('PyShooting') #この文字列がウィンドウ名になります。
    surface = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT)) #もし全画面にしたいならpygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGIT), FULLSCREEN)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        pygame.display.update()
        clock.tick(FPS)

main()