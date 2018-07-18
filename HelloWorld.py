import pygame
import sys

FPS = 30
windowSize = (800, 600)

pygame.init()  # initialize the pygame

pygame.mixer.init()  # initialize the sound mixer

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("PS circle.png")

# myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
# helloWorld = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("Pluralsight.wav")

pygame.mouse.set_visible(0)

x, y = 0, 0
directionX, directionY = 1, 1

clock = pygame.time.Clock()

while 1:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_DOWN:
                y += 5
            if event.key == pygame.K_UP:
                y -= 5

    screen.fill((0, 0, 0))

    mousePosition = pygame.mouse.get_pos()
    x, y = mousePosition

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]
        sound.stop()
        sound.play()

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]
        sound.stop()
        sound.play()

    if x <= 0:
        sound.stop()
        sound.play()

    if y <= 0:
        sound.stop()
        sound.play()



    screen.blit(helloWorld, (x, y))

    # x += 5 * directionX
    # y += 5 * directionY
    #
    # if x + helloWorldSize[0] > 800 or x <= 0:
    #     directionX *= -1
    #
    # if y + helloWorldSize[1] > 600 or y <= 0:
    #     directionY *= -1

    pygame.display.update()
