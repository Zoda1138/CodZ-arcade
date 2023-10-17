import pygame as py


class Someone(py.sprite.Sprite):

    def __init__(self, imgPath, pos):
        super().__init__()
        self.image = py.image.load(imgPath).convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)