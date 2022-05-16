import  pygame


class Ino(pygame.sprite.Sprite):   # класс пришельца

    def __init__(self, screen):     # инициалиируем пришельцев
        super(Ino, self).__init__()
        self.screen = screen
        self. image = pygame.image.load('image/pixil-frame-001.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)   # выводим пришельца на экран

    def update(self):
        self.y += 0.4
        self.rect.y = self.y



