from shape import *
import pygame
import random

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snow')
    clock = pygame.time.Clock()
    paused = False
    
    # Variables for the screen
    background = []
    ground = Rectangle(0, 300, 800, 300, (0, 255, 0))
    sky = Rectangle(0, 0, 800, 300, (0,0,255))
    background.append(ground)
    background.append(sky)
    
    while True:
        for event in pygame.event.get():
            # Quits when 'q' is typed 
            if (event.type == pygame.QUIT) or event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q: 
                pygame.quit()
                exit()
            
            # Pauses animation
            if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
                paused = not paused

        # Checks if paused, if not then it continues to animate
        if not paused:
            background.append(Snowflake(random.randint(0, 800), random.randint(300, 600))) #Iterates and draws snowflakes
            for drawable in background:
                drawable.draw(screen)
                if isinstance(drawable, Snowflake) and drawable.getMaxY() >= drawable.getLocation()[1]:
                    drawable.setLocation([drawable.getLocation()[0], drawable.getLocation()[1] + 1])

        pygame.display.update()
        clock.tick(30)
