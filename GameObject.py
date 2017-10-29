import pygame
import time
import random
import sys
from BulletObject import *
from PlayerHPModule import *
from pygame.locals import *


class GameObject(pygame.sprite.Sprite):
    
    
    def __init__(self,playerImage,playerHP,playerPosX,playerPosY):
        pygame.sprite.Sprite.__init__(self)
        
        self.playerImage = pygame.image.load(playerImage)
        self.playerHPModule = PlayerHPModule(playerHP,playerPosX)
        self.rect = self.playerImage.get_rect()
        self.width, self.height = 1280,720
        self.rect.left, self.rect.top = playerPosX , playerPosY
        self.playerPosX = playerPosX
        self.playerPosY = playerPosY
        self.speed = 0
        
    def beAttacked(self,damage):
        self.playerHPModule.reduceHP(damage)

    def checkLife(self):
        if self.playerHP <= 0:
            return False
        else:
            return True
        
    def shotBulletObject(self,bulletImage,bulletPosX,bulletPosY):
        self.bulletObject = BulletObject(bulletImage,bulletPosX,bulletPosY)
        return self.bulletObject
        
    def setSpeed(self,speed):
        self.speed = speed
        
    def getSpeed(self):
        return self.speed
    
    def setPlayerMove(self):
        if self.rect.top + self.speed > 0 and self.rect.top + self.speed < 620:
            self.rect.top += self.speed
        
    def setPlayerPosX(self,newPosX):
        self.playerPosX = newPosX

    def setPlayerPosY(self,newPosY):
        self.playerPosY = newPosY

    def setPlayerHP(self,newHP):
        self.playerHPModule.setHP(newHP)
        
    def getPlayerImage(self):
        return self.playerImage

    def getPlayerHP(self):
        return self.playerHPModule.getHP()
    
    def getPlayerPosX(self):
        return self.rect.left

    def getPlayerPosY(self):
        return self.rect.top
    
    
    
    
