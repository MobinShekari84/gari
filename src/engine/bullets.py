import pygame
from engine.physics import Physics

class Bullet(Physics):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.speed = 10
        self.direction = direction
        self.alive = True

    def gravity(self):
        if self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed
    
    def collision(self, other):
        pass #!

    def coordinates(self):
        return self.x, self.y
    
    def border(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)