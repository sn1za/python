import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

block_size = 30
left_margin = 40
upper_margin = 50

size = (left_margin + 30*block_size, upper_margin+15*block_size)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("SEA BATTLE")

font_size = int(block_size//1.5)

font = pygame.font.SysFont('notosans', font_size)

def draw_grid():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for y in range(11):
        for x in range(11):
            #Horizontal lines
            pygame.draw.line(screen, BLACK, (left_margin, upper_margin+y*block_size), (left_margin+10*block_size, upper_margin+y*block_size), 1)
            #vertical lines
            pygame.draw.line(screen, BLACK, (left_margin+x*block_size, upper_margin), (left_margin+x * block_size, upper_margin+10*block_size), 1)

            #Horizontal lines
            pygame.draw.line(screen, BLACK, (left_margin+15*block_size, upper_margin+y*block_size), (left_margin+25*block_size, upper_margin+y*block_size), 1)
            #vertical lines
            pygame.draw.line(screen, BLACK, (left_margin+x*block_size+15*block_size, upper_margin), (left_margin+x*block_size+15*block_size, upper_margin+10*block_size), 1)

        if y < 10:
            num_ver = font.render(str(y+1), True, BLACK)
            letters_hor = font.render(letters[y], True, BLACK)

            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()

            #vertical number at left
            screen.blit(num_ver, (left_margin - (block_size//2+num_ver_width//2), upper_margin + y*block_size + (block_size//2 - num_ver_height//2)))
            #Horizontal
            screen.blit(letters_hor, (left_margin + y*block_size + (block_size//2 - letters_hor_width//2), block_size * 0.8))

            # vertical number at right
            screen.blit(num_ver, (left_margin - (block_size // 2 + num_ver_width // 2) + 15 * block_size, upper_margin + y * block_size + (block_size // 2 - num_ver_height // 2)))
            #Horizontal left blank
            screen.blit(letters_hor, (left_margin + y*block_size + (block_size//2 - letters_hor_width//2)+ 15 * block_size, block_size * 0.8))



def main():

    game_over = False
    screen.fill(WHITE)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        draw_grid()
        pygame.display.update()

main()
pygame.quit()

