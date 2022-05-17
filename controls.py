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

def update(color, screen, stats, sc, gun, inos, bullets):    # обновление экрана
    screen.fill(color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)   # столкновение пули с пришельцем
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        stats.score += 10
        sc.image_score()
        check_hight_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:     # создание новой армии
        bullets.empty()
        create_army(screen, inos)



def kill_gun(stats, screen, sc, gun, inos, bullets):        #столкновение пушки с пришельцем
    if stats.guns_health > 0:
        stats.guns_health -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):     #обновление позиции пришельцев
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        kill_gun(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos, bullets):    # проверка линии обороны
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            kill_gun(stats, screen, sc, gun, inos, bullets)
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

def check_hight_score(stats, sc):  # проверка рекордов
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sc.image_hight_score()
        with open('hight_score.txt', 'w') as f:
            f.write(str(stats.hight_score))











