import pygame
import time
import random
import sys
from BulletObject import *
from PlayerHPModule import *
from GameObject import *
from pygame.locals import *

class AIBossObject(GameObject):
    
    def __init__(self,bossImage,bossHP,bossPosX,bossPosY):
        super(AIBossObject,self).__init__(bossImage,bossHP,bossPosX,bossPosY)
        self.index = 0
        self.BossImage = ['Image/Boss_1.png','Image/Boss_2.png','Image/Boss_3.png','Image/Boss_4.png','Image/Boss_5.png']
        self.speed = 10
    
    def getPlayerImage(self):
        self.index += 1
        if self.index == 50:
            self.index = 0
            
        if self.index < 10 :
            return pygame.image.load(self.BossImage[0])
        
        elif self.index >=10 and self.index < 20 :
            return pygame.image.load(self.BossImage[1])
        
        elif self.index >=20 and self.index < 30 :
            return pygame.image.load(self.BossImage[2])
        
        elif self.index >=30 and self.index < 40 :
            return pygame.image.load(self.BossImage[3])
        
        elif self.index >=40 and self.index < 50 :
            return pygame.image.load(self.BossImage[4])
        
    def setPlayerMove(self):
        if self.rect.top + self.speed <= 20 or self.rect.top + self.speed >= 600:
            self.speed *= -1
            
        if self.rect.top + self.speed > 0 and self.rect.top + self.speed < 620:
            self.rect.top += self.speed
    
