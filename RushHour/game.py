import pygame, sys, resource
import vehicle, vehicles, color, draw, event, level


pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rush Hour")



surface_game = pygame.Surface((800,800))
surface_game_x = 0
surface_game_y = 0

surface_game_function = pygame.Surface((200,800))
surface_game_function_x = screen.get_width() - surface_game_function.get_width()
surface_game_function_y = screen.get_height() - surface_game_function.get_height()
surface_game_function.fill(color.colors.get("GREEN_PASTEL"))





# for row in game1.cells:
#     print(row)

event.initial(screen, surface_game, surface_game_function, level.levels.get(1))
draw.initial(screen, surface_game, surface_game_function, level.levels.get(1))
while event.running:
    
    draw.draw_game_main()
    draw.draw_game_function()



    event.check_win()
    event.check_event()

    

    screen.blit(surface_game,(surface_game_x,surface_game_y))
    screen.blit(surface_game_function, (surface_game_function_x,surface_game_function_y))




    pygame.display.update()
    clock.tick(60)




pygame.quit()
sys.exit()