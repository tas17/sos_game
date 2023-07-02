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
dif = TILE_WIDTH
val = 0
font = pygame.font.SysFont("comicsans", 20)

txt_S = font.render("S", 1, (0, 0, 0))
txt_O = font.render("O", 1, (0, 0, 0))


class Button:
    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.font = font

        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    # TODO: Give a method rather than hardcoding
                    reset_board()


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
def draw_board():
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


# Returns if the sequence of 3 starting with index "start" is winning
def is_winning_sequence(start):
    if start < 0 or start + 2 >= TILE_NUMBER:
        return False
    if board[start] == 1 and board[start+1] == -1 and board[start+2] == 1:
        return True
    return False


# Returns if there are winning positions including x
def move_was_winning(x):
    for i in range (3):
        start = x - 2 + i
        if is_winning_sequence(start):
            return True
    return False
 

# Display instructions for the game
def instruction(player):
    # TODO: Some instructions should not be reprinted every time
    text_player = font.render(f"Player {player % 2 +1} to play", 1, (0, 0, 0))
    text_S = font.render("Left Click to put an 'S'", 1, (0, 0, 0))
    text_O = font.render("Right Click to put an 'O'", 1, (0, 0, 0))
    screen.blit(text_player, (dif / 2, HEIGHT - 100))
    screen.blit(text_S, (dif / 2, HEIGHT - 80))       
    screen.blit(text_O, (dif / 2, HEIGHT - 60))


def reset_board():
    global board
    board = np.zeros(TILE_NUMBER)


reset_button = Button("Reset", (dif / 2, HEIGHT - 40), font=font)
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
            reset_button.click(event)
            if valid:
                player_won = move_was_winning(x)
#                 if player_won:

                   # TODO: add that a player wins, until resetting 
    draw_board()
    reset_button.show()
    if valid:
        player += 1
    instruction(player)
    # TODO: button to reset

 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    
    
