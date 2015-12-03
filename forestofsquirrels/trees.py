import pygame


class Tree(pygame.sprite.Sprite):
    def __init__(self, forest, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, forest)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("forestofsquirrels/graphics/tree.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x - self.width / 2
        self.rect.y = self.y - self.height
