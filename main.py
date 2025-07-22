import pygame

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
fon = pygame.image.load('img/bg.png')
sund = pygame.image.load('img/sunduk.png')
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
player_speed = 10
player_x = 960
player_y = 625
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
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, self.in_color, (x, y, self.weight, self.height))
                print_text(x + 10, y + 10, message)
        else:
            pygame.draw.rect(screen, self.in_color, (x, y, self.weight, self.height))
            print_text(x + 10, y + 10, message)


btn1 = Button(400,100,'red','green')
run = True
while run:
    pygame.display.update()
    screen.blit(fon, (bg_x, 0))
    screen.blit(sund, (200,200))
    btn1.draw_button(500, 500, 'жмякай')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        screen.blit(walk_up[player_anim_count],(player_x, player_y))
    else:
        screen.blit(walk_stop, (player_x, player_y))

    if player_x < 328 and player_y < 278:
        print_text(100,150, 'Открыть сундук Е')



    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 50:
        player_x -= player_speed
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < 1850:
        player_x += player_speed
    elif (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
        player_y -= player_speed
    elif (keys[pygame.K_DOWN]or keys[pygame.K_s]) and player_y < 944:
        player_y += player_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(30)