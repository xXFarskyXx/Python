import pygame

# Initialize Pygame
pygame.init()



# Create the display window
width, height = 960 , 540
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chokun Slave") 
white = (255, 255, 255)

imp = pygame.image.load("Image Asset\Chan Pillow.jpg").convert()
imp = pygame.transform.scale(imp , (200 , 200))
# Using blit to copy content from one surface to other

# Main game loop
pygame.display.flip() # Update Entire Screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    screen.blit(imp, (0, 0))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.update() #Update At Specific Rectangular Area

# Quit Pygame when the loop exits
pygame.quit()