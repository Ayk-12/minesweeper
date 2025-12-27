import pygame, time, random
pygame.init()

WIDTH, HEIGHT = 810, 760 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

global side
side = 30

TILE_NOT_OPENED_IMAGE = pygame.image.load("Assets\\tile_not_opened.png")
TILE_NOT_OPENED = pygame.transform.scale(TILE_NOT_OPENED_IMAGE, (side, side))

TILE_NOT_OPENED_SAFE_IMAGE = pygame.image.load("Assets\\tile_not_opened_safe.png")
TILE_NOT_OPENED_SAFE = pygame.transform.scale(TILE_NOT_OPENED_SAFE_IMAGE, (side, side))

TILE_NOT_OPENED_SELECTABLE_IMAGE = pygame.image.load("Assets\\tile_not_opened_selectable.png")
TILE_NOT_OPENED_SELECTABLE = pygame.transform.scale(TILE_NOT_OPENED_SELECTABLE_IMAGE, (side, side))

TILE_NOT_OPENED_FLAGGED_IMAGE = pygame.image.load("Assets\\tile_not_opened_flagged.png")
TILE_NOT_OPENED_FLAGGED = pygame.transform.scale(TILE_NOT_OPENED_FLAGGED_IMAGE, (side, side))

TILE_NOT_OPENED_FLAGGED_SELECTABLE_IMAGE = pygame.image.load("Assets\\tile_not_opened_flagged_selectable.png")
TILE_NOT_OPENED_FLAGGED_SELECTABLE = pygame.transform.scale(TILE_NOT_OPENED_FLAGGED_SELECTABLE_IMAGE, (side, side))

TILE_OPENED_IMAGE = pygame.image.load("Assets\\tile_opened.png")
TILE_OPENED = pygame.transform.scale(TILE_OPENED_IMAGE, (side, side))

TILE_OPENED_1_IMAGE = pygame.image.load("Assets\\tile_opened_1.png")
TILE_OPENED_1 = pygame.transform.scale(TILE_OPENED_1_IMAGE, (side, side))

TILE_OPENED_2_IMAGE = pygame.image.load("Assets\\tile_opened_2.png")
TILE_OPENED_2 = pygame.transform.scale(TILE_OPENED_2_IMAGE, (side, side))

TILE_OPENED_3_IMAGE = pygame.image.load("Assets\\tile_opened_3.png")
TILE_OPENED_3 = pygame.transform.scale(TILE_OPENED_3_IMAGE, (side, side))

TILE_OPENED_4_IMAGE = pygame.image.load("Assets\\tile_opened_4.png")
TILE_OPENED_4 = pygame.transform.scale(TILE_OPENED_4_IMAGE, (side, side))

TILE_OPENED_5_IMAGE = pygame.image.load("Assets\\tile_opened_5.png")
TILE_OPENED_5 = pygame.transform.scale(TILE_OPENED_5_IMAGE, (side, side))

TILE_OPENED_6_IMAGE = pygame.image.load("Assets\\tile_opened_6.png")
TILE_OPENED_6 = pygame.transform.scale(TILE_OPENED_6_IMAGE, (side, side))

TILE_OPENED_7_IMAGE = pygame.image.load("Assets\\tile_opened_7.png")
TILE_OPENED_7 = pygame.transform.scale(TILE_OPENED_7_IMAGE, (side, side))

TILE_OPENED_8_IMAGE = pygame.image.load("Assets\\tile_opened_8.png")
TILE_OPENED_8 = pygame.transform.scale(TILE_OPENED_8_IMAGE, (side, side))

TILE_OPENED_BOMB_IMAGE = pygame.image.load("Assets\\tile_opened_bomb.png")
TILE_OPENED_BOMB = pygame.transform.scale(TILE_OPENED_BOMB_IMAGE, (side, side))

HAPPY_FACE_IMAGE = pygame.image.load("Assets\\happy_face.png")
HAPPY_FACE = pygame.transform.scale(HAPPY_FACE_IMAGE, (66, 66))

SHOCKED_FACE_IMAGE = pygame.image.load("Assets\\shocked_face.png")
SHOCKED_FACE = pygame.transform.scale(SHOCKED_FACE_IMAGE, (66, 66))

DEAD_FACE_IMAGE = pygame.image.load("Assets\\dead_face.png")
DEAD_FACE = pygame.transform.scale(DEAD_FACE_IMAGE, (66, 66))

TEXT_FONT = pygame.font.SysFont('times new roman', 55)
TEXT_FONT_2 = pygame.font.SysFont('times new roman', 20)


def game(WIDTH, HEIGHT):
    BLACK = (0,0,0)
    GRAY = (230, 230, 230)

    y_board = 100

    Cells_list = []
    left_click_variable = 0
    right_click_variable = 0
    game_over_variable = 0
    initial_variable = 0
    dummy_variable = 1
    adjacent = int((HEIGHT - y_board)/side) #22
    correct = 0
    other_dummy_variable = 0
    y = 0

    class Cells:

        cell_number = 0
        win_variable = 0

        def __init__(self, cell_x, cell_y, opened, bomb, bomb_counter, flagged, cell_win, safe):
            self.cell_x = cell_x
            self.cell_y = cell_y
            self.opened = opened
            self.bomb = bomb
            self.bomb_counter = bomb_counter
            self.flagged = flagged
            self.cell_win = cell_win
            self.safe = safe

            self.coords = (self.cell_x, self.cell_y)
            self.act_coords = ((self.cell_x - 1) * side, (self.cell_y - 1) * side + y_board)
            self.selectable_tile =  pygame.Rect(self.act_coords[0], self.act_coords[1], side, side)
            self.adjacents_list = []

            Cells_list.append(self)
            
            Cells.cell_number += 1
            self.number = Cells.cell_number

        def ChainReaction(self):
            chain_dummy = 0
            for other_cell in self.adjacents_list:
                if other_cell.bomb == False and other_cell.flagged == False and self.bomb == False:
                    other_cell.opened = True
                if other_cell.bomb_counter == 0 and other_cell.bomb == False:
                    chain_dummy += 1
                if chain_dummy >= 5:
                    Cells.ChainReaction(other_cell)

        @classmethod
        def CheckSurroundings(cls): # adjacent cells: -1, +1, -22, +22, -23, -21, +21, +23
            for cell in Cells_list:
                for other_cell in cell.adjacents_list:
                    if other_cell.bomb == True:
                        cell.bomb_counter += 1

        @classmethod
        def GameOver(cls):
            for cell in Cells_list:
                if cell.bomb == True:
                    screen.blit(TILE_OPENED_BOMB, (cell.act_coords[0], cell.act_coords[1]))

    for i in range(int(WIDTH/side)): #27
        for j in range(int((HEIGHT - y_board)/side)): #22
            Cells(i+1, j+1, False, False, 0, False, 0, False)
    number_of_bombs, original_number_of_bombs = int(0.2 * len(Cells_list)), int(0.2 * len(Cells_list))

    for _ in range(number_of_bombs):
        x = 0
        while x == 0:
            random_cell = random.choice(Cells_list)
            if random_cell.bomb == False:
                random_cell.bomb = True
                x += 1
      
    for cell in Cells_list:
        for other_cell in Cells_list:
            if other_cell.number == cell.number - 1 and other_cell.cell_y == cell.cell_y - 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number + 1 and other_cell.cell_y == cell.cell_y + 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number - adjacent and other_cell.cell_x == cell.cell_x - 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number + adjacent and other_cell.cell_x == cell.cell_x +  1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number - adjacent - 1 and other_cell.cell_x == cell.cell_x - 1 and other_cell.cell_y == cell.cell_y - 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number - adjacent + 1 and other_cell.cell_x == cell.cell_x - 1 and other_cell.cell_y == cell.cell_y + 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number + adjacent - 1 and other_cell.cell_x == cell.cell_x +  1 and other_cell.cell_y == cell.cell_y - 1:
                cell.adjacents_list.append(other_cell)
            elif other_cell.number == cell.number + adjacent + 1 and other_cell.cell_x == cell.cell_x +  1 and other_cell.cell_y == cell.cell_y + 1:
                cell.adjacents_list.append(other_cell)

    Cells.CheckSurroundings()

    while y == 0: #turns one cell green
        random_cell = random.choice(Cells_list)
        if random_cell.bomb == False and random_cell.bomb_counter == 0:
            random_cell.safe = True
            y += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        left, middle, right = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse[0], mouse[1], 1, 1)
        keys_pressed = pygame.key.get_pressed()

        screen.fill(GRAY)
        
        face_rect = pygame.Rect(WIDTH/2 - 34, 20, 66, 66)

        if game_over_variable == 0:
            if initial_variable == 0 and left:
                start = time.time()
                initial_variable += 1

            if initial_variable == 1:
                if dummy_variable > 0:  
                    end = time.time()
                    time_elapsed = round(end - start, 1)
                TIME = TEXT_FONT.render(str(time_elapsed), True, BLACK)
                screen.blit(TIME, (WIDTH - 135, 20))

            screen.blit(HAPPY_FACE, (WIDTH/2 - 34, 20))

            if left:
                screen.blit(SHOCKED_FACE, (WIDTH/2 - 34, 20))

        if mouse_rect.colliderect(face_rect):
            screen.blit(SHOCKED_FACE, (WIDTH/2 - 34, 20))

        for cell in Cells_list:
            if cell.opened == False:
                if cell.flagged == False:
                    screen.blit(TILE_NOT_OPENED, (cell.act_coords[0], cell.act_coords[1]))
                elif cell.flagged == True:
                    screen.blit(TILE_NOT_OPENED_FLAGGED, (cell.act_coords[0], cell.act_coords[1]))
                if cell.safe == True:
                    screen.blit(TILE_NOT_OPENED_SAFE, (cell.act_coords[0], cell.act_coords[1]))
                if mouse_rect.colliderect(cell.selectable_tile):
                    screen.blit(TILE_NOT_OPENED_SELECTABLE, (cell.act_coords[0], cell.act_coords[1]))
                    if cell.flagged == True:
                        screen.blit(TILE_NOT_OPENED_FLAGGED_SELECTABLE, (cell.act_coords[0], cell.act_coords[1]))

                if mouse_rect.colliderect(cell.selectable_tile) and cell.opened == False:

                    if left and left_click_variable == 0:
                        left_click_variable = 1
                    elif right and right_click_variable == 0:
                        right_click_variable = 1

                    if left_click_variable == 1 and not left and mouse[1] > y_board:
                        cell.opened = True
                        if cell.flagged == True:
                            number_of_bombs += 1
                        if cell.bomb == True:
                            game_over_variable += 1
                        Cells.ChainReaction(cell)
                        left_click_variable = 0
                        
                    if right_click_variable == 1 and not right and mouse[1] > y_board:
                        if cell.flagged == False:
                            cell.flagged = True
                            number_of_bombs -= 1
                        else:
                            cell.flagged = False
                            number_of_bombs += 1
                        right_click_variable = 0
            
            if cell.opened == True:
                if cell.bomb == False:
                    if cell.bomb_counter == 0:
                        screen.blit(TILE_OPENED, (cell.act_coords[0], cell.act_coords[1]))               
                    elif cell.bomb_counter == 1:
                        screen.blit(TILE_OPENED_1, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 2:
                        screen.blit(TILE_OPENED_2, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 3:
                        screen.blit(TILE_OPENED_3, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 4:
                        screen.blit(TILE_OPENED_4, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 5:
                        screen.blit(TILE_OPENED_5, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 6:
                        screen.blit(TILE_OPENED_6, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 7:
                        screen.blit(TILE_OPENED_7, (cell.act_coords[0], cell.act_coords[1]))
                    elif cell.bomb_counter == 8:
                        screen.blit(TILE_OPENED_8, (cell.act_coords[0], cell.act_coords[1]))
                else:
                    screen.blit(TILE_OPENED_BOMB, (cell.act_coords[0], cell.act_coords[1]))

        if keys_pressed[pygame.K_LCTRL]:
            for cell in Cells_list:
                if cell.bomb == True:
                    screen.blit(TILE_OPENED_BOMB, (cell.act_coords[0], cell.act_coords[1]))

        if game_over_variable != 0:
            dummy_variable = -1
            Cells.GameOver()
            screen.blit(DEAD_FACE, (WIDTH/2 - 34, 20))
            end_time = str(round(end - start, 1))
            END_TIME = TEXT_FONT.render(str(end_time), True, BLACK)
            screen.blit(END_TIME, (WIDTH - 110, 20))
            if other_dummy_variable == 0:
                for cell in Cells_list:
                    if cell.flagged == True and cell.bomb == True:
                        correct += 1
                other_dummy_variable += 1
            if correct == 1:
                CORRECT = TEXT_FONT_2.render(f'You had {str(correct)} correct guess.', True, BLACK)
            else:
                CORRECT = TEXT_FONT_2.render(f'You had {str(correct)} correct guesses.', True, BLACK)
            screen.blit(CORRECT, (125, 40))

        if mouse_rect.colliderect(face_rect) and left:
            game(WIDTH, HEIGHT)

        if number_of_bombs == 0:
            for cell in Cells_list:
                if cell.flagged == True and cell.bomb == True and cell.cell_win == 0:
                    Cells.win_variable += 1
            if Cells.win_variable >= original_number_of_bombs:
                    dummy_variable = -1
                    end_time = str(round(end - start, 1))
                    END_TIME = TEXT_FONT.render(str(end_time), True, BLACK)
                    screen.blit(END_TIME, (WIDTH - 110, 20))
                    WIN_TEXT = TEXT_FONT_2.render('Congratulations. You Won!', True, BLACK)
                    screen.blit(WIN_TEXT, (110, 40))

        NUMBER_OF_BOMBS_TEXT = TEXT_FONT.render(str(number_of_bombs), True, BLACK)
        screen.blit(NUMBER_OF_BOMBS_TEXT, (20, 20))

        pygame.display.update()
        clock.tick(60)

game(WIDTH, HEIGHT)
