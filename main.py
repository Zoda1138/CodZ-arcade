import pygame as py
from sys import exit
from src.Charecters.Playa import Playa
from src.Charecters.Zombie import Zombie

py.init()
h, w = 940, 640
screen = py.display.set_mode((h, w))
py.display.set_caption('CodZ arcade')

# Player
player = py.sprite.GroupSingle()
player.add(Playa())

# Zombies
zombies = py.sprite.Group()
zombies.add(Zombie())


def run():
    while True:
        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()
                exit()

        screen.fill((255, 255, 255))

        player.draw(screen)
        player.update()

        zombies.draw(screen)
        zombies.update()

        py.display.flip()


if __name__ == '__main__':
    run()
