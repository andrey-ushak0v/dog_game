import pygame
import sys
from bullet import Bullet
from flowers import Ino
import time

def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:        # вправо нажать
                gun.move_right = True
            elif event.key == pygame.K_a:      # влево нажать
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:       # вправо отпустить
                gun.move_right = False
            elif event.key == pygame.K_a:        # влево отпустить
                gun.move_left = False

def update(color, screen, gun, inos, bullets):    # обновление экрана
    screen.fill(color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)   # столкновение пули с пришельцем
    if len(inos) == 0:     # создание новой армии
        bullets.empty()
        create_army(screen, inos)



def kill_gun(stats, screen, gun, inos, bullets):        #столкновение пушки с пришельцем
    stats.guns_health -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(2)


def update_inos(stats, screen, gun, inos, bullets):     #обновление позиции пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        kill_gun(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)

def inos_check(stats, screen, gun, inos, bullets):    # проверка линии обороны
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            kill_gun(stats, screen, gun, inos, bullets)
            break



def create_army(screen, inos):        # создание армии
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)      # сколько в одном ряду
    ino_height = ino.rect.height
    number_ino_y = int((600 - 100 - 2 * ino_height) / ino_height)      # сколько в одном столбике

    for row_num in range(number_ino_y - 1):
        for ino_num in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_num
            ino.y = ino_height + ino_height * row_num
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_num
            inos.add(ino)







