import pygame
import time
import random
import sys  
from pygame.locals import *

class BulletObject(pygame.sprite.Sprite):

    def __init__(self,bulletImage,bulletPosX,bulletPosY):
        pygame.sprite.Sprite.__init__(self)
        self.bulletImage = pygame.image.load(bulletImage)
        self.rect = self.bulletImage.get_rect()
        self.width, self.height = 1280,720
        self.rect.left, self.rect.top = bulletPosX,bulletPosY
        self.bulletPosX = bulletPosX
        self.bulletPosY = bulletPosY
        self.active = True
        if self.bulletPosX < 640:
            self.speed = 15
        else:
            self.speed = -15
    
    def setBulletMove(self):
        if self.rect.left + self.speed > 0 and self.rect.left + self.speed <1280:
            self.rect.left += self.speed
        else:
            self.active = False
    def setActive(self,active):
        self.active = active
        
    def getActive(self):
        return self.active
            
    def setSpeed(self,speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed
    
    def setBulletPosX(self,newPosX):
        self.bulletPosX = newPosX

    def setBulletPosY(self,newPosY):
        self.bulletPosY = newPosY

    def getBulletImage(self):
        return self.bulletImage

    def getBulletPosX(self):
        return self.bulletPosX

    def getBulletPosY(self):
        return self.bulletPosY
