import pygame

class Bullet(pygame.sprite.Sprite):   # создаем пулю в пушке
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 10)
        self.color = 121, 85, 72
        self.speed = 16
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):      # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):    #отрисовка пули на экране
        pygame.draw.rect(self.screen, self.color, self.rect)


