import pygame
import random
import pygame.display
import time
pygame.init()
# расшифровка элементов: r - room, m - monster, t - table(планшет), c - coridor, l - left, r - right
# загрузка картинки
def load_image(name):
    image_1 = pygame.image.load(name)
    return image_1
# Объявление констант и флагов
energy = 12015
energy_minus = 1
gmt = 1
gst = 0
grd, gld = 0, 0
table_state = 0
t1, t2, t3, t4, t5, t6, t7 = 1, 0, 0, 0, 0, 0, 0
# Массив комнат
list_room_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 0]]
time_minute = 1302
rc, lc = 0, 0
clock = pygame.time.Clock()
# создание окна
size = wight, height = 1400, 900
screen = pygame.display.set_mode(size)
running = True
c = 0
# добавление фоновой музыки и звуков
pygame.mixer.music.load('resources/kuler.mp3')
pygame.mixer.music.play(0)
sound_open = pygame.mixer.Sound('resources/open_close_door.mp3')
sound_close = pygame.mixer.Sound('resources/close.mp3.mp3')
sound_button = pygame.mixer.Sound('resources/button.mp3')
sound_scary = pygame.mixer.Sound('resources/scary.mp3')
sound_knock = pygame.mixer.Sound('resources/knock.mp3')
sound_screamer = pygame.mixer.Sound('resources/screamer.mp3')
# создание групп спрайтов и спрайтов
menu_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/menu.png")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
menu_sprites.add(sprite)
sprite.rect.x = 0
sprite.rect.y = 20


r_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("resources/1r.PNG")
sprite.rect = sprite.image.get_rect()
r_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20

rr_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("resources/1r_r.PNG")
sprite.rect = sprite.image.get_rect()
rr_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20

rl_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("resources/1r_l.PNG")
sprite.rect = sprite.image.get_rect()
rl_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20

rrl_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("resources/1r_rl.PNG")
sprite.rect = sprite.image.get_rect()
rrl_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20

table1_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/1t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table1_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20


table2_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/2t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table2_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/2r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table2_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0


table3_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/3t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table3_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/3r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table3_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0


table4_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/4t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table4_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/4r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table4_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0


table5_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/5t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table5_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/5r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table5_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0


table6_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/6t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table6_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/6r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table6_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0

m1_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/1m.png")
image1 = pygame.transform.scale(image, (200, 120))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
m1_sprites.add(sprite)
sprite.rect.x = 900
sprite.rect.y = 300

m2_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/2m.png")
image1 = pygame.transform.scale(image, (200, 120))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
m2_sprites.add(sprite)
sprite.rect.x = 1100
sprite.rect.y = 300

table7_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/7t.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
table7_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
sprite1 = pygame.sprite.Sprite()
image = load_image("resources/7r.PNG")
image1 = pygame.transform.scale(image, (700, 520))
sprite1.image = image1
sprite1.rect = sprite.image.get_rect()
table7_sprites.add(sprite1)
sprite1.rect.x = 700
sprite1.rect.y = 0

scream_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = load_image("resources/scrimer.PNG")
image1 = pygame.transform.scale(image, (1400, 900))
sprite.image = image1
sprite.rect = sprite.image.get_rect()
scream_sprites.add(sprite)
sprite.rect.x = 5
sprite.rect.y = 20
while running:
    if gst:
        energy -= energy_minus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_s] and table_state == 1:
                sound_scary.stop()
                sound_scary.play()
                energy -= 500
                if t2:
                    list_room_state[1][2] = 1
                if t3:
                    list_room_state[2][2] = 1
                if t4:
                    list_room_state[3][2] = 1
                if t5:
                    list_room_state[4][2] = 1
                if t6:
                    list_room_state[5][2] = 1
                if t7:
                    list_room_state[6][2] = 1
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                gst = 1
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if table_state == 0:
                    table_state = 1
                    energy_minus += 9
                else:
                    table_state = 0
                    energy_minus -= 9
            if pygame.key.get_pressed()[pygame.K_1] and table_state == 1:
                t1 = 1
                t2, t3, t4, t5, t6, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_2] and table_state == 1:
                t2 = 1
                t1, t3, t4, t5, t6, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_3] and table_state == 1:
                t3 = 1
                t2, t1, t4, t5, t6, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_4] and table_state == 1:
                t4 = 1
                t2, t3, t1, t5, t6, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_5] and table_state == 1:
                t5 = 1
                t2, t3, t4, t1, t6, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_6] and table_state == 1:
                t6 = 1
                t2, t3, t4, t5, t1, t7 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_7] and table_state == 1:
                t7 = 1
                t2, t3, t4, t5, t6, t1 = 0, 0, 0, 0, 0, 0
                sound_button.play()
            if pygame.key.get_pressed()[pygame.K_a] and table_state == 0:
                if grd == 1:
                    grd = 0
                    sound_close.play()
                else:
                    grd = 1
                    sound_open.play()
            if pygame.key.get_pressed()[pygame.K_d] and table_state == 0:
                if gld == 1:
                    gld = 0
                    sound_close.play()
                else:
                    gld = 1
                    sound_open.play()
    if gst:
        c += 1
    if gmt:
        menu_sprites.draw(screen)
    if gst:
        r_sprites.draw(screen)
    if grd and gld and gst:  # закрой все двери
        rrl_sprites.draw(screen)
    elif grd:  # закрой правую
        rr_sprites.draw(screen)
    elif gld:  # закрой левую
        rl_sprites.draw(screen)
    if table_state and gst:  # открой планшет
        table1_sprites.draw(screen)
        if t1:
            table1_sprites.draw(screen)
            if list_room_state[0][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[0][1] == 1:
                m2_sprites.draw(screen)
        if t2:
            table2_sprites.draw(screen)
            if list_room_state[1][1] == 1:
                m2_sprites.draw(screen)
            if list_room_state[1][0] == 1:
                m1_sprites.draw(screen)
        if t3:
            table3_sprites.draw(screen)
            if list_room_state[2][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[2][1] == 1:
                m2_sprites.draw(screen)
        if t4:
            table4_sprites.draw(screen)
            if list_room_state[3][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[3][1] == 1:
                m2_sprites.draw(screen)
        if t5:
            table5_sprites.draw(screen)
            if list_room_state[4][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[4][1] == 1:
                m2_sprites.draw(screen)
        if t6:
            table6_sprites.draw(screen)
            if list_room_state[5][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[5][1] == 1:
                m2_sprites.draw(screen)
        if t7:
            table7_sprites.draw(screen)
            if list_room_state[6][0] == 1:
                m1_sprites.draw(screen)
            if list_room_state[6][1] == 1:
                m2_sprites.draw(screen)
    print(c)
    if c % 100 == 0 and gst:
        if list_room_state[6][0]:
            list_room_state[random.choice([3, 5])][0] = 1
            list_room_state[6][0] = 0
        elif list_room_state[5][0]:
            list_room_state[4][0] = 1
            list_room_state[5][0] = 0
        elif list_room_state[4][0]:
            list_room_state[random.choice([3, 2, 5])][0] = 1
            list_room_state[4][0] = 0
        elif list_room_state[3][0]:
            list_room_state[random.choice([4, 1])][0] = 1
            list_room_state[3][0] = 0
        elif list_room_state[1][0]:
            list_room_state[1][0] = 0
            list_room_state[0][0] = 1
            lc = 0
            rc = 1
        elif list_room_state[2][0]:
            list_room_state[2][0] = 0
            list_room_state[0][0] = 1
            rc = 0
            lc = 1
        elif list_room_state[0][0]:
            print(rc, lc)
            if lc == gld and lc == 1 or rc == grd and rc == 1:
                list_room_state[6][0] = 1
                list_room_state[0][0] = 0
                lc = 0
                rc = 0
                sound_knock.play()
            else:  # скример и конец игры
                scream_sprites.draw(screen)
                sound_screamer.play()
                pygame.display.flip()
                time.sleep(3)
                running = 0
    if c % 100 == 0 and gst:
        if list_room_state[6][1]:
            list_room_state[random.choice([3, 5])][1] = 1
            list_room_state[6][1] = 0
        elif list_room_state[5][1]:
            list_room_state[random.choice([4, 6])][1] = 1
            list_room_state[5][1] = 0
            if list_room_state[5][2]:
                list_room_state[5][2] = 0
                list_room_state[5][1] = 0
                list_room_state[6][1] = 1
        elif list_room_state[4][1]:
            list_room_state[random.choice([3, 2, 5])][1] = 1
            list_room_state[4][1] = 0
            if list_room_state[4][2]:
                list_room_state[4][2] = 0
                list_room_state[4][1] = 0
                list_room_state[6][1] = 1
        elif list_room_state[3][1]:
            list_room_state[random.choice([4, 6, 1])][1] = 1
            list_room_state[3][1] = 0
            if list_room_state[3][2]:
                list_room_state[3][2] = 0
                list_room_state[3][1] = 0
                list_room_state[6][1] = 1
        elif list_room_state[1][1]:
            list_room_state[1][1] = 0
            list_room_state[0][1] = 1

            if list_room_state[1][1]:
                list_room_state[1][1] = 0
                list_room_state[1][1] = 0
                list_room_state[6][1] = 1
        elif list_room_state[2][1]:
            list_room_state[2][1] = 0
            list_room_state[0][1] = 1

            if list_room_state[2][2]:
                list_room_state[2][2] = 0
                list_room_state[2][1] = 0
                list_room_state[6][1] = 1
        else:
            # скример и конец игры
            sound_screamer.play()
            scream_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(3)
            running = 0
    if energy <= 0:
        sound_screamer.play()
        scream_sprites.draw(screen)
        pygame.display.flip()
        time.sleep(3)
        running = 0
        list_room_state[1][2], list_room_state[2][2], list_room_state[3][2], list_room_state[4][2], list_room_state[5][2], list_room_state[6][2] = 0, 0, 0, 0, 0, 0
    pygame.display.flip()
pygame.quit()
