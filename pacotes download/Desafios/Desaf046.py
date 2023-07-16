from time import sleep
import pygame
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('Pode comemorar')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Desaf046.mp3')
pygame.mixer.music.play()
pygame.event.wait()





