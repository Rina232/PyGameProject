import pygame
import os
import sys
import random

pygame.init()

FPS = 50
WIDTH = 500
HEIGHT = 600
STEP = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():

    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    main_text = "КОСМИЧЕСКАЯ ОБОРОНА"
    font = pygame.font.SysFont('MathSansBold', 35)
    text = font.render(main_text, 1, pygame.Color(252, 242, 255))
    m_rect = text.get_rect()
    m_rect.top = 210
    m_rect.x = WIDTH // 2 - text.get_width() // 2
    pygame.draw.rect(screen, (97, 69, 107), (m_rect.x - 10, m_rect.y - 10,
                                             m_rect.width + 20, m_rect.height + 20))
    screen.blit(text, m_rect)

    text_coord = 345
    x = 0
    h = 0
    w = 0
    text_list = ["Правила игры", "Играть"]
    font = pygame.font.SysFont('MathSans', 27)
    for line in text_list:
        text = font.render(line, 1, pygame.Color(97, 69, 107))
        m_rect = text.get_rect()
        m_rect.top = text_coord
        m_rect.x = WIDTH // 2 - text.get_width() // 2
        if h == 0:
            h = m_rect.h + 20
            x = m_rect.x - 10
            w = m_rect.width + 20
        pygame.draw.rect(screen, (252, 242, 255), (x, m_rect.y - 10,
                                                   w, h))
        screen.blit(text, m_rect)
        text_coord -= 45

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x <= event.pos[0] <= x + w:
                    if m_rect.y - 10 <= event.pos[1] <= m_rect.y - 10 + h:
                        level_screen()
                    if m_rect.y + 35 <= event.pos[1] <= m_rect.y + 35 + h:
                        rules_screen()
        pygame.display.flip()
        clock.tick(FPS)


def level_screen():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground2.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                               40, 40))
    pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

    text_list = ["Уровень 1", "Уровень 2", "Уровень 3", "Уровень 4",
                 "Уровень 5", "Скоро...", "Скоро...", "Скоро...", "Скоро..."]
    font = pygame.font.SysFont('MathSansBold', 27)
    text_y = 120
    y = 80
    k = 0
    for i in range(3):
        x = 60
        text_x = 73
        for j in range(3):
            text = font.render(text_list[k], 1, pygame.Color(252, 242, 255))
            m_rect = text.get_rect()
            m_rect.y = text_y
            m_rect.x = text_x
            pygame.draw.rect(screen, (97, 69, 107), (x, y, 120, 100))
            screen.blit(text, m_rect)
            text_x += 140
            x += 140
            k += 1
        text_y += 140
        y += 140

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    start_screen()
                elif 60 <= event.pos[0] <= 180:
                    if 80 <= event.pos[1] <= 180:
                        level_1()
                    elif 220 <= event.pos[1] <= 320:
                        level_4()
                elif 200 <= event.pos[0] <= 320:
                    if 80 <= event.pos[1] <= 180:
                        level_2()
                    elif 220 <= event.pos[1] <= 320:
                        level_5()
                elif 340 <= event.pos[0] <= 460 and 80 <= event.pos[1] <= 180:
                    level_3()
        pygame.display.flip()
        clock.tick(FPS)


def rules_screen():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                               40, 40))
    pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    start_screen()
        pygame.display.flip()
        clock.tick(FPS)


def level_1():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'),
                                 (WIDTH, HEIGHT))
    spaceship = Spaceship()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    level_screen()

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                                   40, 40))
        pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


def level_2():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'),
                                 (WIDTH, HEIGHT))
    spaceship = Spaceship()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    level_screen()

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                                   40, 40))
        pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


def level_3():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'),
                                 (WIDTH, HEIGHT))
    spaceship = Spaceship()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    level_screen()

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                                   40, 40))
        pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


def level_4():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'),
                                 (WIDTH, HEIGHT))
    spaceship = Spaceship()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    level_screen()

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                                   40, 40))
        pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


def level_5():
    fon = pygame.transform.scale(load_image(f'Picture\\SpaceBackground3.png'),
                                 (WIDTH, HEIGHT))
    spaceship = Spaceship()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    level_screen()

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (252, 242, 255), (10, 10,
                                                   40, 40))
        pygame.draw.polygon(screen, (97, 69, 107), [(20, 30), (35, 40), (35, 20)], 3)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(pygame.transform.scale(load_image("Picture\spaceship.png"),
                                              (450, 600)), 3, 4)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(175, 440)
        self.k = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.k += 1
        if self.k % 5 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.health = 0
        self.frames = []
        self.cur_frame = 0
        self.k = 0
        hits = ['hit1', 'hit2', 'hit3', 'hit4', 'hit5', 'hit6']
        self.hit = random.choice(hits)
        if self.hit == 'hit1' or self.hit == 'hit3':
            self.cut_sheet(pygame.transform.scale(load_image(f"Picture\{self.hit}.png"),
                                                  (64, 320)), 1, 5)
            self.n = 25
        else:
            self.cut_sheet(pygame.transform.scale(load_image(f"Picture\{self.hit}.png"),
                                                  (64, 448)), 1, 7)
            self.n = 35

    def update(self):
        if self.health == 0 and self.k < self.n:
            self.k += 1
            if self.k % 5 == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames)
                self.image = self.frames[self.cur_frame]
        if self.k >= self.n:
            self.rect = self.rect.move(1000, 1000)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


class Meteorite_1(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.speed = 35
        self.image = pygame.transform.scale(load_image("Picture\Meteorite_1.png"), (100, 100))
        self.rect = self.image.get_rect()


class Meteorite_2(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.speed = 15
        self.image = load_image("Picture\Meteorite_2.png")
        self.rect = self.image.get_rect()


class Asteroid_1(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.speed = 20
        self.image = load_image("Picture\Asteroid_1.png")
        self.rect = self.image.get_rect()


class Asteroid_2(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 150
        self.speed = 15
        self.image = load_image("Picture\Asteroid_2.png")
        self.rect = self.image.get_rect()


class Comet(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.speed = 25
        self.image = load_image("Picture\Comet.png")
        self.rect = self.image.get_rect()


class Satellite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.speed = 15
        self.image = load_image("Picture\Satellite.png")
        self.rect = self.image.get_rect()


pygame.display.set_caption('Космическая оборона')
pygame_icon = pygame.image.load(f'data\\Picture\\icon.png')
pygame.display.set_icon(pygame_icon)
start_screen()

terminate()
