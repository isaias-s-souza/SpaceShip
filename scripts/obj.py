import pygame

#Classe Sprite trás uma séries de recursos para tratar imagens
class Obj(pygame.sprite.Sprite):
    def __init__(self, img, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)