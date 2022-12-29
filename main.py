import pygame
import os
import sys

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
    for line in text_list:
        font = pygame.font.SysFont('MathSans', 27)
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 50 and 10 <= event.pos[1] <= 50:
                    start_screen()
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


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
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


# spaceship = Spaceship(load_image("Picture\spaceship.png"), 1, 5, 63, 32)
pygame.display.set_caption('Космическая оборона')
pygame_icon = pygame.image.load(f'data\\Picture\\icon.png')
pygame.display.set_icon(pygame_icon)
start_screen()

terminate()
