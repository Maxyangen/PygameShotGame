import pygame
import time
import random
import sys
from pygame.locals import *

class PlayerHPModule:

    def __init__(self,playerHP,playerPosX):
        self.playerHP = playerHP

    
    def reduceHP(self,damage):
        self.playerHP -= damage

    def getHP(self):
        return self.playerHP

    def setHP(self,newHP):
        self.playerHP = newHP

    
