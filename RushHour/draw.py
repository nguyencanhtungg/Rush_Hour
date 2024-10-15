import pygame, color, event

pygame.init()

def initial(screen_current, surface_game_current, surface_game_function_current, game_initial):
    global screen, surface_game, surface_game_function, game
    game = game_initial
    screen = screen_current
    surface_game = surface_game_current
    surface_game_function = surface_game_function_current

def next_game(game_current):
    global game
    game = game_current

def draw_vehicles(surface_game, game):
    unit_cell = int(surface_game.get_width()/game.size_game)
    surface_game.fill(color.colors["GREY"])
    for i in range(1, game.len() + 1):
        if game.vehicles.get(i).versus > 0:
            draw_vehicle(surface_game,unit_cell, i,((game.vehicles.get(i).versus),game.vehicles.get(i).get_pos_last()), (game.vehicles.get(i).versus, game.vehicles.get(i).get_pos_last() + game.vehicles.get(i).size - 1))
        else :
            draw_vehicle(surface_game, unit_cell, i, (game.vehicles.get(i).get_pos_last(), -game.vehicles.get(i).versus), (game.vehicles.get(i).get_pos_last() + game.vehicles.get(i).size - 1, -game.vehicles.get(i).versus))

def draw_vehicle(surface_game,unit_cell,name_vehicle, pos1, pos2):

    vehicle_rect = pygame.Rect(int((pos1[1] - 1) * unit_cell),int((pos1[0] - 1) * unit_cell),int((pos2[1] - pos1[1] + 1) * unit_cell),int((pos2[0] - pos1[0] + 1) * unit_cell))
    pygame.draw.rect(surface_game, color.colors.get(name_vehicle), vehicle_rect, border_radius= 25)

def draw_arrow(surface_game,unit_cell, pos, path_arrow):
    arrow_image = pygame.image.load(path_arrow)
    arrow_image = pygame.transform.scale(arrow_image, (unit_cell,unit_cell))
    arrow_image.set_alpha(150)
    surface_game.blit(arrow_image, (int((pos[1] - 1) * unit_cell), int((pos[0] - 1) * unit_cell)))


def draw_game_main():
    global surface_game, game
    unit_cell = int(surface_game.get_width()/game.size_game)
    draw_vehicles(surface_game, game)
    draw_arrow(surface_game, unit_cell, (game.vehicles.get(1).versus, game.size_game), "RushHour/resources/image/arrow.png")

def draw_current_vehicle(surface_game_function, currrent_vehicle):
    surface_game_function.fill(color.colors.get(currrent_vehicle))

def draw_button_icon(surface_game_fuction, rect, path):
    icon = pygame.image.load(path)
    icon = pygame.transform.scale(icon, rect.size)
    surface_game_fuction.blit(icon, rect.topleft)

def draw_function_buttons(surface_game_function):
    pygame.draw.rect(surface_game_function, color.colors.get("BLUE_SKY"), event.rect_button_restart, border_radius=10)
    draw_button_icon(surface_game_function, event.rect_button_restart, "RushHour/resources/image/restart.png")
    pygame.draw.rect(surface_game_function, color.colors.get("BLUE_SKY"), event.rect_button_back, border_radius=10)
    draw_button_icon(surface_game_function, event.rect_button_back, "RushHour/resources/image/back.png")
    if event.admin_mode:
        pygame.draw.rect(surface_game_function, color.colors.get("BLUE_SKY"), event.rect_button_solve, border_radius=10)
        draw_button_icon(surface_game_function, event.rect_button_solve, "RushHour/resources/image/solve.png")
        pygame.draw.rect(surface_game_function, color.colors.get("BLUE_SKY"), event.rect_button_next_level, border_radius=10)
        draw_button_icon(surface_game_function, event.rect_button_next_level, "RushHour/resources/image/right_arrow.png")

        pygame.draw.rect(surface_game_function, color.colors.get("BLUE_SKY"), event.rect_button_prev_level, border_radius=10)
        draw_button_icon(surface_game_function, event.rect_button_prev_level, "RushHour/resources/image/left_arrow.png")






def draw_game_function():
    global surface_game_function
    draw_current_vehicle(surface_game_function, event.currently_selecting)
    draw_function_buttons(surface_game_function)

