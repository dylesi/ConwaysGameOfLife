import pygame

class Automata:
    def __init__(self, screen):
        self.automataAmountX = 100
        self.automataAmountY = 100
        self.padding = 1
        self.automataWidth = 5
        self.automataHeight = 5
        self.automataRect = (self.automataWidth, self.automataHeight)