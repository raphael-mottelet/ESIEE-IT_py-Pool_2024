## FILE DECRIPTOR
## ESIEE-IT PYTHON POOL 2024
## The goal of this project is to build a full maze/rpg like game from the pygame module.
##
##

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mon Premier Jeu Pygame")

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logique du jeu (à ajouter)

    # Mise à jour de l'affichage
    pygame.display.flip()
