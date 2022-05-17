import pygame.font
from space_banger import Gun
from pygame.sprite import Group


class Scores():   #вывод информации из игры

    def __init__(self, screen, stats):    #инициализируем подсчет очков
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (121, 85, 72)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_hight_score()
        self.image_guns()

    def image_score(self):  #преобразовывает счет в графическое изображение
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_hight_score(self):  # преобразует рекорд в изображение
        self.hight_score_image = self.font.render(str(self.stats.hight_score), True, self.text_color, (0, 0, 0))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20

    def image_guns(self): # количество жизней
        self.guns = Group()
        for gun_number in range(self.stats.guns_health):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)



    def show_score(self):   #вывод счета на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.guns.draw(self.screen)







