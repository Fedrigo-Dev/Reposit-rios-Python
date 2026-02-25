# Criar um programa que toca um MP3

import pygame

pygame.mixer.init()

pygame.mixer.music.load("lifeletters.mp3")

pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)