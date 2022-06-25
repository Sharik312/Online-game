import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLient")

clientNumber = 0
FPS = 75
VEL = 10


class Player:
    def __init__(self, x, y, width, height, colour, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = vel
    
    def draw(self, win):
        pygame.draw.rect(WIN, self.colour, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)



def draw_window(WIN, player):
    WIN.fill(WHITE)
    player.draw(WIN)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    p = Player(250, 250, 100, 100, GREEN, VEL)
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT
        
        p.move()
        draw_window(WIN, p)


if __name__ == "__main__":
    main()