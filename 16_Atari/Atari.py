
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import pygame

BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Block:
    color = BLACK

    x = 0
    y = 0
    width = 100
    height = 50

    def __init__(self, color, x, y, width = 100, height = 25):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def initPos(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y = 0):
        self.x += x
        self.y += y

    def getArgForDraw(self):
        return (self.x, self.y, self.width, self.height)

class Ball:
    color = RED

    x = 0
    y = 0
    width = 100
    height = 50

    def __init__(self, color, x, y, width = 25, height = 25):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def initPos(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y = 0):
        self.x += x
        self.y += y

    def getArgForDraw(self):
        return (self.x, self.y, self.width, self.height)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Atari')

    TARGET_FPS = 30
    clock = pygame.time.Clock()
    
    steve = Block(WHITE, pygame.display.get_surface().get_width() // 2, 10)
    bill = Block(BLUE, pygame.display.get_surface().get_height() // 2, \
                        pygame.display.get_surface().get_height() - 25 - 10)

    ball = Ball(RED, pygame.display.get_surface().get_width() // 2, \
                    pygame.display.get_surface().get_height() // 2)

    running = True
    while running:
        for event in pygame.event.get():
            # Handle Events(Keyboard, Mouse...)          
            if event.type == pygame.QUIT:
                running = False

            # Keyboard Events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:                  
                    steve.move(10)
                elif event.key == pygame.K_LEFT:
                    steve.move(-10)
                if event.key == pygame.K_a:
                    bill.move(-10)
                elif event.key == pygame.K_d:
                    bill.move(10)

        # Update Game

        # Update Drawing
        screen.fill(BLACK)

        pygame.draw.rect(screen, steve.color, steve.getArgForDraw())
        pygame.draw.rect(screen, bill.color, bill.getArgForDraw())
        pygame.draw.ellipse(screen, ball.color, ball.getArgForDraw())

        pygame.display.update()
        clock.tick(TARGET_FPS)

if __name__=="__main__":
    main()