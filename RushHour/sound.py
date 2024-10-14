import pygame

pygame.mixer.init()

sound_wood = pygame.mixer.Sound('RushHour/resources/sound/wood.wav')

def play_sound_wood():
    sound_wood.play()
