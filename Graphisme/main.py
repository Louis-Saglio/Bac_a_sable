# coding: utf-8

import pygame
from pygame.locals import *


def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    # On instancie une fenêtre
    screen = pygame.display.set_mode((640, 450))
    # On instancie un fond
    fond = pygame.image.load("background.jpg").convert()
    # On colle le fond à la fenêtre
    screen.blit(fond, (0, 0))
    # On instancie une balle
    balle = pygame.image.load("ball.bmp")
    balle_rect = balle.get_rect()
    vitesse = (1, 1)
    # On valide les modifications
    pygame.display.flip()

    # Boucle d'évènements
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return "exit"
        balle_rect.move(vitesse)
        screen.blit(balle, balle_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
