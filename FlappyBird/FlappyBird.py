#!/usr/bin/env python3
import pygame
import random

def base_animation(window, base_image, x_axis):
    #first
    window.blit(base_image, (x_axis,420))#adds loaded base_image to window and adjusts position
    #second
    window.blit(base_image, (x_axis+190,420))

def bird_animation(window, bird_image_resize, bird_rect):
    window.blit(bird_image_resize, bird_rect)

def pipe_animation(window, pipes, pipe_image):
    for pipe in pipes:
        pipe.centerx -= 5
        window.blit(pipe_image, pipe)

def collision(pipes, bird_rect):
    for pipe in pipes:
        if pipe.colliderect(bird_rect):
            print("COLLIDED")

def game_build():
    pygame.init() #initializing pygame module
    window = pygame.display.set_mode((288, 512)) #1.to display app window 2.set_mode() uses tuple args for specifying size

    #background
    bg_image = pygame.image.load('/home/zoot/Desktop/Python/FlappyBird/background.png')#only loads image

    #base
    base_image = pygame.image.load('/home/zoot/Desktop/Python/FlappyBird/base.png')
    x_axis = 0

    #bird
    bird_image = pygame.image.load('/home/zoot/Desktop/Python/FlappyBird/bird.png')
    bird_image_resize = pygame.transform.scale(bird_image, (60, 60))
    bird_rect = bird_image_resize.get_rect(center = (100, 256)) #create rectangle around bird detect collision

    grv_force = 2
    bird_new_position = 0

    #pipes
    pipe_img = pygame.image.load('/home/zoot/Desktop/Python/FlappyBird/pipe.png')
    pipe_image = pygame.transform.scale(pipe_img, (60, 270))
    pipe_list = []

    TIMER = pygame.USEREVENT
    pygame.time.set_timer(TIMER, 1000 )

    #mainloop
    clock = pygame.time.Clock()
    running = True
    while running:
        #eventloop
        pygame.display.set_caption('Flappy Bird')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_new_position = 10
                    bird_new_position += 1


            if event.type == TIMER:
                random_height = [150, 200, 250, 300, 350]
                pipes = pipe_image.get_rect(midtop = (300, random.choice(random_height )))
                pipe_list.append(pipes)

        #bg logic
        window.blit(bg_image, (0,0))#adds loaded bg_image to window and adjusts position

        #collision detection
        collision(pipe_list, bird_rect)
        #pipe animation
        pipe_animation(window, pipe_list, pipe_image)

        #base animation
        x_axis -= 1
        base_animation(window, base_image, x_axis)
        #if condition for infinite looping of base_image
        if x_axis <= -190:
            x_axis = 0

        #bird animation
        bird_new_position += grv_force
        bird_rect.centery = bird_new_position
        bird_animation(window, bird_image_resize, bird_rect)


        #updates
        clock.tick(60)#fps
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    game_build()
