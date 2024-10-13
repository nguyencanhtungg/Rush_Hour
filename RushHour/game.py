import pygame, sys, resource
import vehicle, vehicles, color, draw, event


pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rush Hour")


surface_game = pygame.Surface((800,800))
surface_game_x = 0
surface_game_y = 0
game1 = vehicles.Vehicles(12)
game1.add_vehicle(2,3,4)
game1.add_vehicle(2,1,4)
game1.add_vehicle(2,4,5)
game1.add_vehicle(2,6,5)
game1.add_vehicle(2,5,2)
game1.add_vehicle(2,-1,5)
game1.add_vehicle(3,-3,1)
# game1.add_vehicle(3,-6,1)
game1.add_vehicle(3,-4,4)



for row in game1.cells:
    print(row)

# running = True





while event.running:
    
    draw.draw_elements(surface_game, game1)
    event.check_win(game1)
    event.check_event(surface_game, game1)

    

                
    screen.blit(surface_game,(surface_game_x,surface_game_y))




    pygame.display.update()
    clock.tick(60)

    # # Get memory usage in kilobytes
    # memory_usage_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # # Convert to MB
    # memory_usage_mb = memory_usage_kb / 1024

    # print(f"Memory used: {memory_usage_mb:.2f} MB")




pygame.quit()
sys.exit()