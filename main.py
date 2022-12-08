# import pygame library
import pygame
import numpy as np
 
TILE_NUMBER = 10
TILE_WIDTH = 50

WIDTH = max((TILE_NUMBER + 1) * 50, 260)
HEIGHT = 300

# initialise the pygame font
pygame.font.init()
 
# Total window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)

board = np.zeros(TILE_NUMBER)
 
x = 0
y = 0
#dif = 500 / 9
dif = TILE_WIDTH
val = 0
font = pygame.font.SysFont("comicsans", 20)

txt_S = font.render("S", 1, (0, 0, 0))
txt_O = font.render("O", 1, (0, 0, 0))

def get_coord(pos):
    x = (pos[0] + dif / 2) // dif - 1
    y = (pos[1] + dif / 2) // dif - 1
    return int(x), int(y)
 
# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i)* dif, y * dif), ((x + i) * dif, y * dif + dif), 7)  
 
# Function to draw required lines for making Sudoku grid        
def draw():
    # Draw lines horizontally and vertically to form the board
    for i in range(TILE_NUMBER + 1):
        if i == 0 or i == TILE_NUMBER:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (i * dif + dif/2, dif/2), (i * dif + dif/2, dif + dif/2), thick)     
    for i in range(TILE_NUMBER):
        if board[i] == 1:
            screen.blit(txt_S, ((i+1) * dif - dif/8, 2 * dif / 3))
        if board[i] == -1:
            screen.blit(txt_O, ((i+1) * dif - dif/8, 2 * dif / 3))

    pygame.draw.line(screen, (0, 0, 0), (dif / 2, dif / 2), (TILE_NUMBER * dif + dif / 2, dif / 2), thick)
    pygame.draw.line(screen, (0, 0, 0), (dif / 2, dif + dif / 2), (TILE_NUMBER * dif + dif / 2, dif + dif / 2), thick)
 
# Fill value entered in cell     
def draw_val(val):
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
 
# Display instruction for the game
def instruction(player):
    text_player = font.render(f"Player {player % 2 +1} to play", 1, (0, 0, 0))
    text_S = font.render("Left Click to put an 'S'", 1, (0, 0, 0))
    text_O = font.render("Right Click to put an 'O'", 1, (0, 0, 0))
    screen.blit(text_player, (dif / 2, HEIGHT - 100))
    screen.blit(text_S, (dif / 2, HEIGHT - 80))       
    screen.blit(text_O, (dif / 2, HEIGHT - 60))
 
run = True
rs = 0
error = 0
player = 0
# The loop thats keep the window running
while run:
     
    # White color background
    screen.fill((255, 255, 255))
    valid = False
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 

        # Get the mouse position to insert S or O
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = get_coord(pos)
            if event.button == 1:
                if y == 0 and x >= 0 and x < TILE_NUMBER and board[x] == 0:
                    board[x] = 1
                    valid = True
            if event.button == 3:
                if y == 0 and x >= 0 and x < TILE_NUMBER and board[x] == 0:
                    board[x] = -1
                    valid = True
    draw() 
    if valid:
        player += 1
    # Test if someone wins
    instruction(player)   

 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    
    
