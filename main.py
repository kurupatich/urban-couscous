import pygame, random

clock = pygame.time.Clock()

#база настройки
pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Моностырь")
icon = pygame.image.load('img/sun_iconn.png')
pygame.display.set_icon(icon)

#шрифт и текст
myfont = pygame.font.Font('fonts/OpenSans-VariableFont_wdth,wght.ttf', 40)


#картинки
fon = pygame.image.load('img/fon.jpg')
shop = pygame.image.load('img/shop.png')
casino = pygame.image.load('img/casino.png')
bg_store = pygame.image.load('img/store_bg.png')
walk_left = [pygame.image.load('img/player_left/left1.png'),
    pygame.image.load('img/player_left/left2.png'),
    pygame.image.load('img/player_left/left3.png'),
    pygame.image.load('img/player_left/left4.png'),
]
walk_right = [pygame.image.load('img/player_right/right1.png'),
    pygame.image.load('img/player_right/right2.png'),
    pygame.image.load('img/player_right/right3.png'),
    pygame.image.load('img/player_right/right4.png')]

walk_up = [pygame.image.load('img/back/back1.png'),
    pygame.image.load('img/back/back2.png'),
    pygame.image.load('img/back/back3.png'),
    pygame.image.load('img/back/back4.png')]

walk_stop = pygame.image.load('img/front.png')



bg_x = 0
player_anim_count = 0
player_speed = 30
player_x = 960
player_y = 625
cash = 100
#bg_sound = pygame.mixer.Sound('sounds/Lida- Фото со звездой(slowed+reverb).mp3')
#bg_sound.play()

class Person:
    def __init__(self):
        self.name = ''
        self.hp = 100
    def print_name(self):
        pass

def print_text(x,y,msg):
    txt = myfont.render(msg, True, 'white')
    screen.blit(txt, (x, y))


class Button:
    def __init__(self, weight, height, inactive_color, active_color):
        self.weight = weight
        self.height = height
        self.in_color = inactive_color
        self.act_color = active_color

    def draw_button(self, x, y, message):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.weight:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.act_color, (x,y, self.weight, self.height))
                print_text(x + 10, y + 10, message)
                if click[0] == 1:
                    global cash
                    x = random.randint(1,3)
                    if x > 1:
                        cash += 100
                    else:
                        cash -= 100

                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, self.in_color, (x, y, self.weight, self.height))
                print_text(x + 10, y + 10, message)
        else:
            pygame.draw.rect(screen, self.in_color, (x, y, self.weight, self.height))
            print_text(x + 10, y + 10, message)

scene_ch = 0
def scene_main():
    global player_y
    player_y = 625
    keys1 = pygame.key.get_pressed()
    screen.fill('black')
    screen.blit(fon, (bg_x, 0))
    screen.blit(shop, (50, 478))
    screen.blit(casino,(1500,529))
    if player_x < 328:
        print_text(120,368, 'Войти Е')
        if keys1[pygame.K_e]:
            global scene_ch
            scene_ch = 1
    if player_x > 1480:
        print_text(1570, 400, 'Войти Е')

def store():
    screen.blit(bg_store, (bg_x, 0))
    global player_y
    player_y = 825
    keys2 = pygame.key.get_pressed()
    if player_x < 388:
        print_text(220,668, 'Выйти Q')
        if keys2[pygame.K_q]:
            global scene_ch
            scene_ch = 0
    if (player_x > 750) and (player_x < 1000):
        print_text(900, 607, 'Б/У Виталики')
        print_text(900, 648, 'Открыть Е')

btn1 = Button(400,100,(155,30,30),(155,30,30))
run = True
while run:
    pygame.display.update()
    if scene_ch == 0:
        scene_main()
    if scene_ch == 1:
        store()
    #btn1.draw_button(760, 900, 'Крутануть')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_stop, (player_x, player_y))


    print_text(20,20,f'БазаВиталики:{cash}')

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 50:
        player_x -= player_speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < 1850:
        player_x += player_speed
#    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
#        player_y -= player_speed
#    elif (keys[pygame.K_DOWN]or keys[pygame.K_s]) and player_y < 944:
#        player_y += player_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(30)