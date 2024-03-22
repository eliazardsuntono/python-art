from abc import ABC, abstractclassmethod
import pygame

class Shape(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    @abstractclassmethod
    def draw(self, surface):
        pass
    
    def getLocation(self):
        return(self.__x, self.__y)
    
    # Sets location as an array with first index being x and the second being y
    def setLocation(self, location):
        self.__x = location[0]
        self.__y = location[1]

class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getColor(self):
        return self.__color
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.getColor(), (self.getLocation()[0], self.getLocation()[1], self.getWidth(), self.getHeight()))

class Snowflake(Shape):
    def __init__(self, x, maxY):
        super().__init__(x)
        self.__color = (255,255,255)
        self.__maxY = int(maxY)
    
    def getColor(self):
        return self.__color
    
    def getMaxY(self):
        return self.__maxY
    
    def draw(self, surface):
        pygame.draw.line(surface, self.getColor(), (self.getLocation()[0] - 5, self.getLocation()[1]), (self.getLocation()[0] + 5, self.getLocation()[1]))
        pygame.draw.line(surface, self.getColor(), (self.getLocation()[0], self.getLocation()[1] - 5), (self.getLocation()[0], self.getLocation()[1] + 5))
        pygame.draw.line(surface, self.getColor(), (self.getLocation()[0] - 5, self.getLocation()[1] - 5), (self.getLocation()[0] + 5, self.getLocation()[1] + 5))
        pygame.draw.line(surface, self.getColor(), (self.getLocation()[0] - 5, self.getLocation()[1] + 5), (self.getLocation()[0] + 5, self.getLocation()[1] - 5))