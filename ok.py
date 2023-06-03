from pygame import *
from time import sleep
win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.speed = 2
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 640:
            self.speed = 2
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.speed = 2
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <  430:
            self.speed = 2
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.speed = 5
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 640:
            self.speed = 5
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.speed = 5
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <  430:
            self.speed = 5
            self.rect.y += self.speed

class Enemy(Sprite):
    direction = 'left'
    def move_left_right(self,rect_x,rect_x1):
        if self.rect.x < rect_x:
            self.direction = 'right'
        if self.rect.x > rect_x1:
            self.direction = 'left'

        if self.direction == 'left':
            
            self.rect.x -= self.speed
        else:
            
            self.rect.x += self.speed

    def move_up_down(self,rect_y,rect_y1):
        direction2 = 'up'
        if self.rect.y < rect_y:
            self.direction = 'down'
        if self.rect.y > rect_y1:
            self.direction = 'up'
        if self.direction == 'up':    
            self.rect.y-= self.speed
        else:           
            self.rect.y += self.speed
    


class Wall(sprite.Sprite):
    def __init__(self, rgb, x,y,w,h):
        super().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w,h))
        self.wall.fill(rgb)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))


font.init()
font = font.Font(None,70)
win = font.render('YOU WIN',True,(255,255,255))
lose = font.render('YOU LOSE',True,(255,255,255))

player = Player('hero.png', 0, 50,0)








monster1 = Enemy('cyborg.png', 600, 200,5)
monster2 = Enemy('cyborg.png', 150, 20,2)
monster3 = Enemy('cyborg.png', 300, 20,3)
monster4 = Enemy('cyborg.png', 520,280,2)
monster5 = Enemy('cyborg.png', 440,380,2)

final = Sprite('treasure.png', 10,150, 0)

w1 = Wall((2,4,55), 10,30, 290, 10)
w2 = Wall((2,4,55), 10,120, 150, 10)
w3 = Wall((2,4,55), 150,120, 10, 150)
w4 = Wall((2,4,55), 160,260, 250,10)
w5 = Wall((2,4,55), 410,90, 10,180)
w6 = Wall((2,4,55), 410,80, 120,10)
w7 = Wall((2,4,55), 520,90, 10,300)
w8 = Wall((2,4,55), 290,30, 10,150)
w9 = Wall((2,4,55), 530,380, 95,10)
w10 = Wall((2,4,55), 420,480,400,10)
w11 = Wall((2,40,55), 420,340, 10,150)


game = True
clock = time.Clock()
FPS = 60

#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0, 0))
    player.reset()
    monster1.move_left_right(50,650)
    player.move()
    monster2.move_up_down(40,200)
    monster3.move_left_right(300,650)
    monster4.move_left_right(520,650)
    monster5.move_up_down(85,435)


    if sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2)  or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player, monster1) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,w10) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, monster3) or sprite.collide_rect(player, monster4) or sprite.collide_rect(player, monster5):
        window.blit(lose,(200,200))
        mixer.init()
        mixer.music.load('kick.ogg')
        mixer.music.play()
        player.rect.x = 5 
        player.rect.y = 50

    if sprite.collide_rect(player,final):
        mixer.music.load('money.ogg')
        window.blit(win,(200,200))
        mixer.music.play()
        
    monster2.reset()
    monster1.reset()
    monster3.reset()
    monster4.reset()
    monster5.reset()

    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    w7.draw()
    w8.draw()
    w9.draw()
    w10.draw()
    w11.draw()
    final.reset()

    display.update()
    clock.tick(FPS)