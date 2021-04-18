#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += 5
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if keys_pressed[K_d] and self.rect.x < 680:
            self.rect.x += 5
class Enemy(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 500:
            self.side = 'right'
        if self.rect.x >= 680:
            self.side = 'left'
        if self.side == 'right':
            self.rect.x += self.speed
        if self.side == 'left':
            self.rect.x -= self.speed
class Walls(sprite.Sprite):
    def __init__(self,col1,col2,col3,wid,hei,cor_x, cor_y):
        self.color1 =col1
        self.color2 =col2
        self.color3 =col3
        self.width = wid
        self.height = hei
        self.image = Surface((self.width, self.height))
        self.image.fill((col1,col2,col3))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def secret_wall(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_f]:
            self.rect.y = -1000


font.init()
font = font.Font(None, 70)
secret_wall = font.render('Press F',True,(0,0,0))
lose_font = font.render('SCORPION WIN',True,(255,255,255))
wall_dr = font.render('YOU LOSE',True,(255,255,255))
win_font = font.render('SUB ZERO WIN',True,(255,255,255))

h = 500
w = 750
window = display.set_mode((w,h))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background_mk.png'),(w,h))
lose_background = transform.scale(image.load('win_scorpion.jpg'),(w,h))
win_background = transform.scale(image.load('win_sub_zero.jpg'),(w,h))

mixer.init()
mixer.music.load('mk_music.ogg')
mixer.music.play()
hero = Player('sub-zero.png', 20, 20, 5)
enemy = Enemy('scorpion.png', 650, 300, 5)
gold = GameSprite('treasure.png', 650, 420, 0)
or1 = GameSprite('yes_no.png', 340,280,0)
kick = mixer.Sound('fun.ogg')
win_sub = mixer.Sound('sub-zero_mixer.wav')
wall_1 = Walls(0,255,255,10,100,150,0)
wall_2 = Walls(0,255,255,10,150,150,110)
wall_3 = Walls(0,255,255,10,100,150,250)
wall_4 = Walls(0,255,255,100,10,150,350)
wall_5 = Walls(0,255,255,10,110,250,250)
wall_6 = Walls(0,255,255,117,10,260,250)
wall_7 = Walls(255,0,0,113,10,377,250)
wall_8 = Walls(255,0,0,10,350,490,150)
wall_9 = Walls(0,255,255,210,10,150,100)
wall_10 = Walls(255,0,0,10,150,490,0)

game = True
clock = time.Clock()
FPS = 120
finish = False
#win = transform.scale(image.load('cyborg.png'),(100,100))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

       
    if finish != True:
        window.blit(background,(0,0))
        hero.reset()
        hero.update()
        enemy.reset()
        enemy.update()
        gold.reset()
        or1.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_10.secret_wall()
        if sprite.collide_rect(hero,wall_1) or  sprite.collide_rect(hero,wall_2) or sprite.collide_rect(hero,wall_3) or sprite.collide_rect(hero,wall_4) or sprite.collide_rect(hero,wall_5) or sprite.collide_rect(hero,wall_6) or sprite.collide_rect(hero,wall_7) or sprite.collide_rect(hero,wall_8) or sprite.collide_rect(hero,wall_9) or  sprite.collide_rect(hero,wall_10):
            finish = True
            mixer.music.stop()
            kick.play()
            window.blit(wall_dr,(228,215))
        if sprite.collide_rect(hero,enemy):
            finish = True
            mixer.music.stop()
            kick.play()
            window.blit(lose_background,(0,0))
            window.blit(lose_font,(199,215))
        if sprite.collide_rect(hero,or1):
            wall_2.rect.x = -100
            window.blit(secret_wall,(165,5))
        if sprite.collide_rect(hero,gold):
            finish = True
            window.blit(win_background,(0,0))
            window.blit(win_font,(199,215))
            win_sub.play()
            mixer.music.stop()
            
    display.update()
    clock.tick(FPS)

