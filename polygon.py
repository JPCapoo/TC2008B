#Display any Polygon
#Import Libraries
import numpy
import pygame

#Variables
pygame.init()
screen = pygame.display.set_mode((600,600))
coordinatesArray = []
coordinatesArray2 = []
running = True
center = (300,300)
radius = 80

sidesCircle = 1000
sidesTriangle = 3

#Colors
purple = (102, 0, 102)

for i in range(1, sidesCircle + 1):
    x = radius * numpy.cos(i * 2 * numpy.pi / sidesCircle ) + center[0]
    y = radius * numpy.sin(i * 2 * numpy.pi / sidesCircle ) + center[1]
    coordinatesArray.append((x,y))

for i in range(1, sidesTriangle + 1):
    x = radius * numpy.cos(i * 2 * numpy.pi / sidesTriangle ) + center[0]
    y = radius * numpy.sin(i * 2 * numpy.pi / sidesTriangle ) + center[1]
    coordinatesArray2.append((x,y))

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        pygame.draw.polygon(screen, purple, coordinatesArray, 4)
        pygame.draw.polygon(screen, purple, coordinatesArray2, 4)
        pygame.display.flip()
pygame.quit();
    