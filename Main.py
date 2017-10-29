import pygame
import time
import random
import sys  
from pygame.locals import *
from GameObject import *
from AIBossObject import *



pygame.init()
pygame.mixer.init()

display_width = 1280
display_height = 720
white = (255,255,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('2P Shooting Game')
__StartBackground = pygame.image.load('Image/StartBackground.png')
__TwoPBackground = pygame.image.load('Image/TwoPBackground.jpg')
__GameResetBackground = pygame.image.load('Image/GameOverBackground.png')
__BossGameBackground = pygame.image.load('Image/BossGameBackground.png')


clock = pygame.time.Clock()





#刷新玩家
def display_Player(player):
    gameDisplay.blit(player.getPlayerImage(),player.rect )
    
#刷新子彈
def display_Bullet(bullet):
    if bullet.getActive() == True:
        gameDisplay.blit(bullet.getBulletImage(),bullet.rect)
        
#刷新玩家血量
def DrawPlayer1Hp(player1_HP):
        pygame.draw.rect(gameDisplay,(255, 0, 0), (1000,20,player1_HP,30))
        
def DrawPlayer2Hp(player2_HP):
        pygame.draw.rect(gameDisplay,(255, 0, 0), (100,20,player2_HP,30))
        
def checkGaming(player1,player2):
    if player1.getPlayerHP() <= 0 or player2.getPlayerHP() <= 0 :
        gameover()
        
def gameover():
    gameExit = False
    while not gameExit:
        gameDisplay.blit(__GameResetBackground,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    SetGameStart()
        pygame.display.update()
        clock.tick(60)
        
def SetGameStart():
    pygame.mixer.music.load('Sound/backgroundSound.mp3')
    pygame.mixer.music.play(-1,0)
    pygame.mixer.music.set_volume(0.3)
    gameExit = False
    while not gameExit:
    #gameDisplay.blit(StartBackground,(0,0))
        gameDisplay.blit(__StartBackground,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Boss = AIBossObject('Image/Boss_1.png',200,50,10 * random.randint(5,50))
                    Player1 = GameObject('Image/Player_1.png',100,1150,10 * random.randint(5,50))
                    AIBossGame(Boss,Player1)
                    
                if event.key == pygame.K_k:
                    Player1 = GameObject('Image/Player_1.png',200,1150,10 * random.randint(5,50))
                    Player2 = GameObject('Image/Player_2.png',200,50,10 * random.randint(5,50))
                    TwoPlayerVS(Player1,Player2)
                 
        pygame.display.update()
        clock.tick(60)
def AIBossGame(Boss,Player1):
    #--------------起始設定區--------------
    running = True
    _moveYSize = 10
    _moveXSize = 10
    _damage = 20
    _player1_bullet = []
    _player2_bullet = []
    _BossBulletTick = 0
    objects = pygame.sprite.Group()
    players = pygame.sprite.Group()
    players.add(Boss)
    players.add(Player1)
    #--------------起始設定區--------------
    
    while running:
        gameDisplay.blit(__BossGameBackground,(0,0))
        DrawPlayer1Hp(Player1.getPlayerHP())
        DrawPlayer2Hp(Boss.getPlayerHP())
        checkGaming(Boss,Player1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Player1.setSpeed(_moveYSize*-1)
                elif event.key == pygame.K_DOWN:
                    Player1.setSpeed(_moveYSize)
                                  

                if event.key == pygame.K_l:
                    temp_bullet = Player1.shotBulletObject('Image/Bullet_0.png',Player1.getPlayerPosX()-100,Player1.getPlayerPosY())
                    _player1_bullet.append(temp_bullet)
                    objects.add(temp_bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    Player1.setSpeed(0)
                    
        for b in  range(len(_player1_bullet)):
            _player1_bullet[b].setBulletMove()
            display_Bullet(_player1_bullet[b])
            #判斷玩家一是否被打中
            if pygame.sprite.spritecollide(Player1, objects, True) and _player1_bullet[b].getActive():
                Player1.beAttacked(_damage)
                _player1_bullet[b].setActive(False)
                
            #判斷BOSS是否被打中
            if pygame.sprite.spritecollide(Boss, objects, True) and _player1_bullet[b].getActive():
                Boss.beAttacked(_damage)
                _player1_bullet[b].setActive(False)
                   
        if Boss.rect.top == Player1.rect.top :
            temp_bullet = Boss.shotBulletObject('Image/Bullet_2.png',Boss.getPlayerPosX()+100,Boss.getPlayerPosY())
            _player1_bullet.append(temp_bullet)
            objects.add(temp_bullet)
             
        if _BossBulletTick % 50 == 0 :
            temp_bullet = Boss.shotBulletObject('Image/Bullet_3.png',Boss.getPlayerPosX()+100,Boss.getPlayerPosY())
            _player1_bullet.append(temp_bullet)
            objects.add(temp_bullet)
            
        
        display_Player(Player1)           
        display_Player(Boss)
        
        Player1.setPlayerMove()
        Boss.setPlayerMove()
        _BossBulletTick += 1
        pygame.display.update()

        clock.tick(60)
        
def TwoPlayerVS(Player1,Player2):
    #--------------起始設定區--------------
    running = True
    _moveYSize = 10
    _moveXSize = 10
    _damage = 20
    _player1_bullet = []
    _player2_bullet = []
    objects = pygame.sprite.Group()
    players = pygame.sprite.Group()
    players.add(Player1)
    players.add(Player2)
    #--------------起始設定區--------------
    while running:
        gameDisplay.blit(__TwoPBackground,(0,0))
        DrawPlayer1Hp(Player1.getPlayerHP())
        DrawPlayer2Hp(Player2.getPlayerHP())
        checkGaming(Player1,Player2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Player1.setSpeed(_moveYSize*-1)
                elif event.key == pygame.K_DOWN:
                    Player1.setSpeed(_moveYSize)
                    
                elif event.key == pygame.K_w:
                    Player2.setSpeed(_moveYSize*-1)
                elif event.key == pygame.K_s:
                    Player2.setSpeed(_moveYSize)

                if event.key == pygame.K_l:
                    temp_bullet = Player1.shotBulletObject('Image/Bullet_0.png',Player1.getPlayerPosX()-100,Player1.getPlayerPosY())
                    _player1_bullet.append(temp_bullet)
                    objects.add(temp_bullet)

                elif event.key == pygame.K_h:
                    temp_bullet = Player2.shotBulletObject('Image/Bullet_1.png',Player2.getPlayerPosX()+100,Player2.getPlayerPosY())
                    _player1_bullet.append(temp_bullet)
                    objects.add(temp_bullet)
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    Player1.setSpeed(0)
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    Player2.setSpeed(0)
                   
        for b in  range(len(_player1_bullet)):
            _player1_bullet[b].setBulletMove()
            display_Bullet(_player1_bullet[b])
            #判斷玩家一是否被打中
            if pygame.sprite.spritecollide(Player1, objects, True) and _player1_bullet[b].getActive():
                Player1.beAttacked(_damage)
                _player1_bullet[b].setActive(False)
                #被射中的音效
                pygame.mixer.music.load("Sound/shoot1Sound.mp3")
                pygame.mixer.music.play()
            #判斷玩家二是否被打中
            if pygame.sprite.spritecollide(Player2, objects, True) and _player1_bullet[b].getActive():
                Player2.beAttacked(_damage)
                _player1_bullet[b].setActive(False)
                #被射中的音效
                pygame.mixer.music.load("Sound/shoot2Sound.mp3")
                pygame.mixer.music.play()
            
            
        
            
        
        display_Player(Player1)           
        display_Player(Player2)
        
        Player1.setPlayerMove()
        Player2.setPlayerMove()
        
        pygame.display.update()

        clock.tick(60)

SetGameStart()                
#game_loop()
pygame.quit()
quit()	
