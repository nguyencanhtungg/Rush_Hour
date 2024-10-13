import pygame
currently_selecting = 1
currentle_pos_x = -99
currentle_pos_y = -99
running = True
dragging = False


def check_win(game):
    if game.get_vehicle(1).get_pos_last() == game.size_game - 1:
        print("Win")
        global running
        running = False
def next_selecting(game):
    global currently_selecting
    currently_selecting = currently_selecting + 1
    if currently_selecting == game.len() + 1:
        currently_selecting = 1
def check_event(surface_game, game):
    global dragging, currently_selecting, currentle_pos_x, currentle_pos_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False
        # KEYBOARD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                next_selecting(game)
                print(currently_selecting)

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                game.move(currently_selecting,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                game.move(currently_selecting,1)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game.move(currently_selecting,-1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game.move(currently_selecting, 1)
            if event.key == pygame.K_r:
                game.restart_game()

            if event.key == pygame.K_c:
                for row in game.cells:
                    print(row)

        # MOUSE
        unit_cell = int(surface_game.get_width()/game.size_game)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 0 < mouse_x < surface_game.get_width() - 5 and 0 < mouse_y < surface_game.get_height() - 5:
                cell_y = mouse_x // unit_cell + 1
                cell_x = mouse_y // unit_cell + 1
                if game.cells[cell_x - 1][cell_y - 1] != 0:
                    dragging = True
                    currently_selecting = game.cells[cell_x - 1][cell_y - 1]
                    currentle_pos_x = cell_x
                    currentle_pos_y = cell_y
                print(event.pos)
                print(cell_x,cell_y)
                print(currentle_pos_x,currentle_pos_y)

                

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                cell_y = mouse_x // unit_cell + 1
                cell_x = mouse_y // unit_cell + 1
                if game.vehicles.get(currently_selecting).versus > 0:
                    if cell_y != currentle_pos_y:
                        game.move(currently_selecting, cell_y - currentle_pos_y)
                        currentle_pos_y = cell_y
                elif game.vehicles.get(currently_selecting).versus < 0:
                    if cell_x != currentle_pos_x:
                        game.move(currently_selecting, cell_x - currentle_pos_x)
                        currentle_pos_x = cell_x