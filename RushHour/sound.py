import pygame

pygame.mixer.init()

sound_wood = pygame.mixer.Sound('RushHour/resources/sound/wood.wav')
background_music = pygame.mixer.music.load("RushHour/resources/sound/funkycat.mp3")
pygame.mixer.music.set_volume(0.5)
def play_sound_wood():
    sound_wood.play()
def play_background_music():
    pygame.mixer.music.play(-1)