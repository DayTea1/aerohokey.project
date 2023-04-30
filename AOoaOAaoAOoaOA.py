from pygame import *
from random import randint 
import pygame
pygame.init()
from time import sleep
'''Необхідні класи'''

# клас- батько для спрайтів 
class GameSprite(sprite.Sprite):
#Конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        #кожен спрайт повинен зберігати властивості image - зображення
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


        

    #клас-спадкоємець для спрайту-гравця(керується стрілками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
                self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 540:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed



    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 650:
            self.rect.x += self.speed


#Ігрова сцена:
back = (255, 255, 255) #колір фону(background)
win_width = 1100
win_height = 600
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("фоооон.png"), (win_width, win_height))
window.fill(back)

#Прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
FPS = 60

#створення м'яма та ракетки
racket1 = Player('racket.png', 30, 200, 15, 100, 100)
racket2 = Player('racket.png', 1020, 200, 15, 100, 100)
ball = GameSprite('tenis_ball.png', 500, 200, 15, 75, 75)

mixer.init()
mixer.music.load('Megafonk.mp3')
mixer.music.play()

font.init()
font1 = font.SysFont("Arial", 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0 ,0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0 ,0))
reset = font1.render('PRESS Y TO RESET', True, (0, 0, 0))
speed_x = 3
speed_y = 4
score1 = 0
score2 = 0
font2 = font.SysFont("Arial", 25)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        keys = key.get_pressed()
        window.blit(background, (0,0))
       
        
        racket1.update_l()
        racket2.update_r()  
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball):
            speed_x = 16
            speed_y = -19

        if sprite.collide_rect(racket2, ball):
            speed_x = -15
            speed_y = 14
            #якщо м'яч досягає меж екрана, змінюємо напрямок його руху
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
            #Якщо мяч відлетів далі ракетки, виводимо умову програшу для першого гравця
        if ball.rect.x < 0:
            window.blit(lose1, (450,200))
            window.blit(reset, (440,250))
            finish = True
            finish = False
            keys = key.get_pressed()
            if keys[K_r] and ball.rect.x < 0:
                ball.rect.x = 500
                ball.rect.y = 300
                score1 = score1 + 1
            
             #Якщо мяч полетів далі ркетки, виводимо умову програшу другого гравця
        if ball.rect.x > win_width:
            
            window.blit(lose2, (450,200)) 
            window.blit(reset, (440,250))
            finish = True
            finish = False
            keys = key.get_pressed()
            if keys[K_r] and ball.rect.x > win_width:
                ball.rect.x = 500
                ball.rect.y = 300
                score2 = score2 + 1
        if keys[K_y]:
            score1 = 0
            score2 = 0
        
        win1 = font2.render('Player2:' + str(score1), 1, (180, 0, 0))
        window.blit(win1, (980, 10))
        win2 = font2.render('Player1:' + str(score2), 1, (180, 0, 0))
        window.blit(win2, (980, 40))
    
                
        racket1.reset()
        racket2.reset()
        ball.reset()
   
    display.update()
    clock.tick(FPS)

            