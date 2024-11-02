import pygame, color, event, vehicles, draw, level, sound

screen = None
surface_board = None
surface_function = None
game = None
current_vehicle = 1
game_size = 6
unit_cell = None

rect_car = None
rect_truck = None

dragging_car = False
dragging_truck = False
rect_car_dragging = None
rect_truck_dragging = None
vertical = True
show_pop_button = False

def initial(screen_current, surface_board_current, surface_function_current):
    global screen, surface_board, surface_function, game, unit_cell, game_size
    global rect_car, rect_truck, rect_car_dragging, rect_truck_dragging
    global rect_button_reset, rect_button_back, rect_button_save, rect_button_exit, rect_button_pop_level
    screen = screen_current
    surface_board = surface_board_current
    surface_function = surface_function_current
    game = vehicles.Vehicles(game_size)
    unit_cell = int(surface_board.get_width() / game_size)
    
    rect_car = pygame.Rect(10,10,130,90)
    rect_truck = pygame.Rect(10,120,180,90)

    rect_car_dragging = pygame.Rect(10 + 800,10,unit_cell * 2,unit_cell)
    rect_truck_dragging = pygame.Rect(10 + 800,120,unit_cell * 3,unit_cell)

    rect_button_reset = pygame.Rect(surface_function.get_width() - 50, 250, 50, 50)
    rect_button_back = pygame.Rect(surface_function.get_width() - 50, 300, 50, 50)
    rect_button_save = pygame.Rect(surface_function.get_width() - 50, 350, 50, 50)
    rect_button_exit = pygame.Rect(surface_function.get_width() - 50, 400, 50, 50)
    rect_button_pop_level = pygame.Rect(surface_function.get_width() - 50, 500, 50, 50)

    load_image()


def load_image():
    # global image_grid
    # image_grid = pygame.image.load("RushHour/resources/image/grid.png")
    pass





def draw_board():
    global surface_board, game
    draw_background()
    draw.draw_vehicles(surface_board, game)
    screen.blit(surface_board, (0,0))

    

def draw_function():
    global screen
    global surface_function, current_vehicle, rect_car, rect_truck, rect_car_dragging, rect_truck_dragging
    global rect_button_reset, rect_button_back, show_pop_button
    pygame.draw.rect(surface_function, color.colors.get(current_vehicle), rect_car, border_radius=10)
    pygame.draw.rect(surface_function, color.colors.get(current_vehicle), rect_truck, border_radius=10)

    pygame.draw.rect(surface_function, color.colors.get("BLUE_SKY"), rect_button_reset, border_radius=10)
    draw.draw_button_icon(surface_function, rect_button_reset, "RushHour/resources/image/restart.png")

    pygame.draw.rect(surface_function, color.colors.get("BLUE_SKY"), rect_button_back, border_radius=10)
    draw.draw_button_icon(surface_function, rect_button_back, "RushHour/resources/image/back.png")

    pygame.draw.rect(surface_function, color.colors.get("BLUE_SKY"), rect_button_save, border_radius=10)
    draw.draw_button_icon(surface_function, rect_button_save, "RushHour/resources/image/save.png")

    pygame.draw.rect(surface_function, color.colors.get("BLUE_SKY"), rect_button_exit, border_radius=10)
    draw.draw_button_icon(surface_function, rect_button_exit, "RushHour/resources/image/exit.png")

    if show_pop_button:
        pygame.draw.rect(surface_function, color.colors.get("BLUE_SKY"), rect_button_pop_level, border_radius=10)
        draw.draw_button_icon(surface_function, rect_button_pop_level, "RushHour/resources/image/pop.png")

    
    


    screen.blit(surface_function, (surface_board.get_width(),0))


    surface_function.fill(color.colors.get("GREEN_PASTEL"))
    if dragging_car:
        pygame.draw.rect(screen, color.colors.get(current_vehicle), rect_car_dragging, border_radius=10)
    if dragging_truck:
        pygame.draw.rect(screen, color.colors.get(current_vehicle), rect_truck_dragging, border_radius=10)



def draw_background():
    # global surface_board, image_grid
    # surface_board.blit(image_grid, (0,0))
    pass

    



def check_event():
    global surface_board, surface_function, game, vertical
    for event in pygame.event.get():
        check_event_quit(event)
        check_event_mouse(event)
        check_event_keyboard(event)



def check_event_mouse(eve):
    global dragging, offset_x, offset_y, rect_car, rect_truck, rect_car_dragging, rect_truck_dragging
    global rect_button_reset
    check_dragging_car(eve)
    check_dragging_truck(eve)
    check_button(eve)

def check_button(eve):
    global show_pop_button
    if eve.type == pygame.MOUSEBUTTONDOWN:
        if rect_button_reset.collidepoint((eve.pos[0] - surface_board.get_width(), eve.pos[1])):
            game.reset_game()
        if rect_button_back.collidepoint((eve.pos[0] - surface_board.get_width(), eve.pos[1])):
            game.pop_last_vehicle()
        update_current_vehicle()
        if rect_button_exit.collidepoint((eve.pos[0] - surface_board.get_width(), eve.pos[1])):
            exit()
        if rect_button_save.collidepoint((eve.pos[0] - surface_board.get_width(), eve.pos[1])):
            save_level()
        if show_pop_button and rect_button_pop_level.collidepoint((eve.pos[0] - surface_board.get_width(), eve.pos[1])):
            level.pop_level()
        sound.play_sound_wood()

        
def check_event_keyboard(eve):
    global vertical, game, show_pop_button
    if eve.type == pygame.KEYDOWN:
        if eve.key == pygame.K_SPACE:
            change_vertical()

        if eve.key == pygame.K_c:
            print(vertical)
            for row in game.cells:
                print(row)
                
        if eve.key == pygame.K_x:
            show_pop_button = not show_pop_button
        

def check_dragging_car(eve):
    global dragging_car, dragging_truck, offset_x, offset_y, rect_car, rect_truck, rect_car_dragging, rect_truck_dragging
    global vertical
    if eve.type == pygame.MOUSEBUTTONDOWN:
        if rect_car.collidepoint((eve.pos[0] - surface_board.get_width(),eve.pos[1] - 0)):  # Kiểm tra xem chuột có nằm trong hình chữ nhật không
            dragging_car = True
            mouse_x, mouse_y = eve.pos
            offset_x = rect_car_dragging.x - mouse_x  # Tính khoảng cách giữa chuột và góc trái trên của hình chữ nhật
            offset_y = rect_car_dragging.y - mouse_y
        
    # Khi nhả chuột ra
    if eve.type == pygame.MOUSEBUTTONUP:
        reset_vehicle_dragging()
        if dragging_car:
            add_vehicle(eve, 2)
            dragging_car = False
            vertical = True
            sound.play_sound_wood()


    # Khi di chuyển chuột
    if eve.type == pygame.MOUSEMOTION:
        if dragging_car:  # Chỉ di chuyển hình chữ nhật khi đang kéo
            mouse_x, mouse_y = eve.pos
            rect_car_dragging.x = mouse_x + offset_x  # Cập nhật vị trí của hình chữ nhật
            rect_car_dragging.y = mouse_y + offset_y




def add_vehicle(eve, size_vehicle):
    global game_size, current_vehicle, vertical
    mouse_x, mouse_y = eve.pos
    if 0 < mouse_x < surface_board.get_width() - 5 and 0 < mouse_y < surface_board.get_height() - 5:
        cell_y = mouse_x // unit_cell + 1
        cell_x = mouse_y // unit_cell + 1
        print(cell_x,cell_y)
        if vertical:
            if 0 <= cell_x <= game_size and 0 <= cell_y <= game_size - size_vehicle + 1:
                game.add_vehicle(size_vehicle, cell_x, cell_y)
                update_current_vehicle()
        else :
            if 0 <= cell_x <= game_size - size_vehicle + 1 and 0 <= cell_y <= game_size:
                game.add_vehicle(size_vehicle, -cell_y, cell_x)
                update_current_vehicle()

        

def check_dragging_truck(eve):
    global dragging_car, dragging_truck, offset_x, offset_y, rect_car, rect_truck, rect_car_dragging, rect_truck_dragging
    global vertical
    if eve.type == pygame.MOUSEBUTTONDOWN:
        if rect_truck.collidepoint((eve.pos[0] - surface_board.get_width(),eve.pos[1] - 0)):  # Kiểm tra xem chuột có nằm trong hình chữ nhật không
            dragging_truck = True
            mouse_x, mouse_y = eve.pos
            offset_x = rect_truck_dragging.x - mouse_x  # Tính khoảng cách giữa chuột và góc trái trên của hình chữ nhật
            offset_y = rect_truck_dragging.y - mouse_y
        
    # Khi nhả chuột ra
    if eve.type == pygame.MOUSEBUTTONUP:
        reset_vehicle_dragging()
        if dragging_truck:
            add_vehicle(eve, 3)
            dragging_truck = False
            vertical = True
            sound.play_sound_wood()


    # Khi di chuyển chuột
    if eve.type == pygame.MOUSEMOTION:
        if dragging_truck:  # Chỉ di chuyển hình chữ nhật khi đang kéo
            mouse_x, mouse_y = eve.pos
            rect_truck_dragging.x = mouse_x + offset_x  # Cập nhật vị trí của hình chữ nhật
            rect_truck_dragging.y = mouse_y + offset_y






def reset_vehicle_dragging():
    global rect_car_dragging, rect_truck_dragging
    rect_car_dragging = pygame.Rect(10 + 800,10,unit_cell * 2,unit_cell)
    rect_truck_dragging = pygame.Rect(10 + 800,120,unit_cell * 3,unit_cell)

def change_vertical():
    global vertical, rect_car_dragging, rect_truck_dragging
    vertical = not vertical
    change_rect_vertical()

def change_rect_vertical():
    global rect_car_dragging, rect_truck_dragging
    width_car = rect_car_dragging.width
    rect_car_dragging.width = rect_car_dragging.height
    rect_car_dragging.height = width_car
    width_truck = rect_truck_dragging.width
    rect_truck_dragging.width = rect_truck_dragging.height
    rect_truck_dragging.height = width_truck


def update_current_vehicle():
    global current_vehicle
    current_vehicle = game.len() + 1

def exit():
    event.custom_map_mode = False

def save_level():
    global game
    if game.len() > 0:
        level.add_level(game)
        game = vehicles.Vehicles(game_size)
        update_current_vehicle()
    else :
        print("A game can't empty")

def check_event_quit(eve):
    if eve.type == pygame.QUIT:
                event.running = False



