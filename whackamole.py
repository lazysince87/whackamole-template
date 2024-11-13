import pygame, random, sys
from constants import *

pygame.init()

# star stuff
STAR_SPEED = 1
NUM_STARS = 20

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Whack-a-Mole')

# mole and star
mole_image = pygame.image.load("mole.png")
star_image = pygame.image.load("star.png")
star_image = pygame.transform.scale(star_image, (16, 16))
mole_pos = [0, 0]  # mole starts at the top-left
stars = []

class Star:
    def __init__(self):
        self.x = self.x = random.randint(0, WIDTH - star_image.get_width())
        self.y = self.y = random.randint(-HEIGHT, 0)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)  # Reset to the top
            self.x = random.randint(0, WIDTH - star_image.get_width())  # random horizontal reset

    def draw(self):
        screen.blit(star_image, (self.x, self.y))

# initial list of stars
for _ in range(NUM_STARS):
    stars.append(Star())

# draw grid
def draw_grid():
    """ 20x16 grid """
    for row in range(ROWS):
        pygame.draw.line(screen, GRID_COLOR, (0, row * GRID_SIZE), (WIDTH, row * GRID_SIZE))  # horizontal lines
    for col in range(COLS):
        pygame.draw.line(screen, GRID_COLOR, (col * GRID_SIZE, 0), (col * GRID_SIZE, HEIGHT))  # vertical lines

# draw mole at its current position
def draw_mole():
    """ mole at its current position"""
    mole_rect = mole_image.get_rect(topleft=(mole_pos[1] * GRID_SIZE, mole_pos[0] * GRID_SIZE))
    screen.blit(mole_image, mole_rect)

# move mole to random position on the grid
def move_mole():
    """move mole to new random position"""
    mole_pos[0] = random.randrange(ROWS)
    mole_pos[1] = random.randrange(COLS)

def main():
    global mole_pos
    clock = pygame.time.Clock()

    while True:
        screen.fill(BG_COLOR)
        for star in stars:
            star.fall()
            star.draw()
        draw_grid()
        draw_mole()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // GRID_SIZE
                row = mouse_y // GRID_SIZE

                # check mole was clicked?
                if row == mole_pos[0] and col == mole_pos[1]:
                    move_mole()

        pygame.display.update()
        clock.tick(30)

# Run the game
if __name__ == "__main__":
    main()