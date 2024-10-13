import pygame, color

pygame.init()

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


def draw_elements(surface_game, game):
    unit_cell = int(surface_game.get_width()/game.size_game)
    draw_vehicles(surface_game, game)
    draw_arrow(surface_game, unit_cell, (game.vehicles.get(1).versus, game.size_game), "/Users/nguyencanhtung/Program/python/Game/RushHour/resources/arrow.png")

