"""
Authors: Akshaya Nishanthan and Amy Zhang
Date Created: 05/27/2022
Date Revised: 
Name: ICS_Culminating_Project
Desciption: testing and preparing to makea an interactive adventure story about the wonders of minerals
"""
# 
import pygame

pygame.init()

display_width = 800
display_height = 600
salmon = ("#FA8072")
clock = pygame.time.Clock()
potatoImg = pygame.image.load("potato.jpg")


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("testy test test!")
def potato(x,y):
    gameDisplay.blit(potatoImg,(x, y))
    
def gameLoop():
    gameExit = False
    x = display_width *0.5
    y = display_height * 0.5
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)
        gameDisplay.fill(salmon)
        potato(x,y) 
        

        
gameLoop()