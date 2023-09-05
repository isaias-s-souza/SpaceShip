import pygame.key

from scripts.obj import Obj
from scripts.scene import Scene
from scripts.animatedBg import AnimatedBg

class Game(Scene):
    def __init__(self):
        super().__init__()

        #depois iremos remover:
        self.bg = AnimatedBg("assets/menu/bg.png", [0, 0], [0, -720], [self.all_sprites])

        self.spaceship = SpaceShip("assets/nave/nave0.png", [600, 600], [self.all_sprites])

    def update(self):
        self.bg.update()
        self.spaceship.update()
        return super().update()


class SpaceShip(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):

        #também serve para verificar se a tecla está
        #pressionada só que fica em loop enquanto tiver
        #apertada
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self):
        self.rect.center += self.direction * self.speed

    def update(self):
        self.input()
        self.move()

    def pra_cima(self, vel):
        self.rect.y -= vel

    def pra_baixo(self, vel):
        self.rect.y += vel

    def pra_esquerda(self, vel):
        self.rect.x -= vel

    def pra_direita(self, vel):
        self.rect.x += vel