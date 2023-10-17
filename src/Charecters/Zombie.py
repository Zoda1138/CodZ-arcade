import pygame as py
from src.Charecters.Someone import Someone


class Zombie(Someone):

    def __init__(self):
        zombies = ('src/Resources/z_1.png', 'src/Resources/z_2.png')
        zIndex = 0
        super().__init__(zombies[zIndex], (40, 75))
