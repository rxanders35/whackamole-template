import pygame
import random

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        mole_image = pygame.image.load("mole.png")
        mole_size = mole_image.get_width()
        clock = pygame.time.Clock()
        x, y = 0, 0  
        running = True
        while running:
            screen.fill("light green")
            for row in range(0, screen.get_height(), mole_size):
                pygame.draw.line(screen, "black", (0, row), (screen.get_width(), row))
            for col in range(0, screen.get_width(), mole_size):
                pygame.draw.line(screen, "black", (col, 0), (col, screen.get_height()))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(x, y, mole_size, mole_size).collidepoint(event.pos):
                        x = random.randrange(0, screen.get_width(), mole_size)
                        y = random.randrange(0, screen.get_height(), mole_size)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
