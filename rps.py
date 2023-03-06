# file created by Luke Nocos

from time import sleep

from random import randint 

import sys

import pygame as pg

import os


# sets asset folder - images and sounds 

# tells the location of where this folder is 
game_folder = os.path.dirname(__file__)
print(game_folder)


# game settings

WIDTH = 500
HEIGHT = 500
80
FPS = 30

# defining colors 

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# init pygame and create a window


# start screen function creates a window indicating if the user wants to play the game 
# uses buttons such as start and exit 

def start_screen():
    pg.init()
    pg.mixer.init()
    welcome_screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Welcome')
    clock = pg.time.Clock()

    # sets a font and uses global to make the font the same throughout the code
    global font
    font = pg.font.Font('freesansbold.ttf', 32)

    # creates text
    text = font.render('ROCK PAPER SCISSORS', True, GREEN, BLUE)
    text_rect = text.get_rect()
    text_rect.center = (HEIGHT/2, WIDTH/4)

    # creates text
    start = font.render('START', True, GREEN, BLUE )
    start_rect = start.get_rect()
    start_rect.x = WIDTH/5.5
    start_rect.y = HEIGHT/2

    # creates text
    exit = font.render('EXIT', True, GREEN, BLUE)
    exit_rect = exit.get_rect()
    exit_rect.x = WIDTH/1.5
    exit_rect.y = HEIGHT/2

    # displays the text and fills screen black
    while True:
        welcome_screen.fill(BLACK)
        welcome_screen.blit(text, text_rect)
        welcome_screen.blit(start, start_rect)
        welcome_screen.blit(exit, exit_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            pg.display.update()

        running = True
        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONUP:
                    # get function gets something right away
                    global mouse_coords
                    mouse_coords = pg.mouse.get_pos()
                    if start_rect.collidepoint(mouse_coords):
                        choose()
                    if exit_rect.collidepoint(mouse_coords):
                        pg.display.quit()


        pg.quit()


# choose function creates a window to display the options the user can choose
# using mouse coordinates and images to select user choice 

def choose():
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Rock Paper Scissors')
        clock = pg.time.Clock()

        # sets a variable to where the location of the image is 
        global rock_image
        rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
        # gets geometry of the image 
        global rock_rect
        rock_rect = rock_image.get_rect()
        global paper_image
        paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
        global paper_rect
        paper_rect = paper_image.get_rect()
        global scissors_image
        scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
        global scissors_rect
        scissors_rect = scissors_image.get_rect()

        # changes the location of the buttons
        paper_rect.y = HEIGHT/2
        scissors_rect.x = WIDTH/2
        scissors_rect.y = HEIGHT/3

        running = True
        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONUP:
                    # get function gets something right away
                    global mouse_coords
                    mouse_coords = pg.mouse.get_pos()
                    
                    # if you click on the image it will do a specific function
                    if rock_rect.collidepoint(mouse_coords):
                        print ("You chose rock")
                        global user_choice
                        user_choice = "rock"
                        compare()
                    
                    elif paper_rect.collidepoint(mouse_coords):
                        print ("You chose paper")
                        user_choice = "paper"
                        compare()
                        

                    elif scissors_rect.collidepoint(mouse_coords):
                        print ("You chose scissors")
                        user_choice = "scissors"
                        compare()
                        
                    return user_choice    
                    
                        

            # draw
            screen.fill(WHITE)
            screen.blit(rock_image, rock_rect)
            screen.blit(paper_image, paper_rect)
            screen.blit(scissors_image, scissors_rect)


            pg.display.flip()

pg.quit()

# choices for terminal and developer use 
choices = ["rock", "paper", "scissors"]

# cpu_select function creates a random choice for the CPU using randint
def cpu_select():
    return choices[randint(0,2)]

# compare function compares the user choice to the CPU and routes it to the versus_screen function
def compare():

    global cpu

    cpu = cpu_select()
    # compares user choice and cpu and leads to the versus screen
    if user_choice == "rock" and cpu == "scissors":
        print ("You win")
        versus_screen()
    elif user_choice == "scissors" and cpu == "paper":
        print ("You win")
        versus_screen()
    elif user_choice == "paper" and cpu == "rock":
        print ("You win")
        versus_screen()
    elif user_choice == "rock" and cpu == "paper":
        print ("You lose")
        versus_screen()
    elif user_choice == "scissors" and cpu == "rock":
        print("You Lose")
        versus_screen()
    elif user_choice == "paper" and cpu == "scissors":
        print("You Lose")
        versus_screen()
    elif user_choice == cpu:
        print ("You Tied! Please try again!")
        versus_screen()
    else:
        print ("Improper input! Please use lowercase letters")


    print ("Computer chose: " + cpu)
    return cpu 


# size of screen 2    

WIDTH2 = 800
HEIGHT2 = 800

# versus_screen function creates a window to show the user choice picture vs the CPU choice picture
# added a play button at the bottom that will show the results of the game 
def versus_screen():
    pg.init()
    pg.mixer.init()
    screen2 = pg.display.set_mode((WIDTH2, HEIGHT2))
    pg.display.set_caption('Versus Screen')
    clock2 = pg.time.Clock()
    running = True
    while running:
        clock2.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONUP:
                    # get function gets something right away
                    global mouse_coords
                    mouse_coords = pg.mouse.get_pos()

        # gets image from folder
        versus_image = pg.image.load(os.path.join(game_folder, 'versus.jpg')).convert()
        versus_rect = versus_image.get_rect()
        screen2.fill(WHITE)
        versus_rect.x = WIDTH/2
        versus_rect.y = HEIGHT/3
        global draw_image
        draw_image = pg.image.load(os.path.join(game_folder, 'draw.jpg')).convert()
        global draw_rect
        draw_rect = draw_image.get_rect()
        draw_rect.x = WIDTH/2
        draw_rect.y = HEIGHT/3

        play_image = pg.image.load(os.path.join(game_folder, 'play.jpg')).convert()
        play_rect = play_image.get_rect()
        play_rect.x = WIDTH/1.5
        play_rect.y = HEIGHT/1.025

        # creates text
        go = font.render('PRESS PLAY BUTTON TO CONTINUE', True, GREEN, BLUE )
        go_rect = go.get_rect()
        go_rect.center = (HEIGHT/1.2, WIDTH/3)
        play_again = font.render('PLAY AGAIN', True, GREEN, BLUE )
        play_again_rect = play_again.get_rect()
        play_again_rect.x = WIDTH2/3
        play_again_rect.y = HEIGHT2/1.25

        # click on play again button to go back to start screen
        if play_again_rect.collidepoint(mouse_coords):
                start_screen()
    
    
        if user_choice == "rock" and cpu == "scissors":
            # displays images on window
            screen2.blit(versus_image, versus_rect)
            screen2.blit(rock_image,rock_rect)
            screen2.blit(scissors_image, scissors_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)


            rock_rect.y = HEIGHT/2
            scissors_rect.x = WIDTH/0.85
            scissors_rect.y = HEIGHT/2

        elif user_choice == "scissors" and cpu == "paper":
            # displays images on window
            screen2.blit(versus_image, versus_rect)
            screen2.blit(scissors_image,scissors_rect)
            screen2.blit(paper_image, paper_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)

            scissors_rect.y = HEIGHT/2
            scissors_rect.x = WIDTH/5
            paper_rect.x = WIDTH/0.85
            paper_rect.y = HEIGHT/2
            
        elif user_choice == "paper" and cpu == "rock":
            # displays images on window
            screen2.blit(versus_image, versus_rect)
            screen2.blit(paper_image,paper_rect)
            screen2.blit(rock_image, rock_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)

            paper_rect.y = HEIGHT/2
            rock_rect.x = WIDTH/0.85
            rock_rect.y = HEIGHT/2
        elif user_choice == "rock" and cpu == "paper":
            # displays images on window
            screen2.blit(versus_image, versus_rect)
            screen2.blit(rock_image,rock_rect)
            screen2.blit(paper_image, paper_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)

            rock_rect.y = HEIGHT/2
            paper_rect.x = WIDTH/0.85
            paper_rect.y = HEIGHT/2
        elif user_choice == "scissors" and cpu == "rock":
            # displays images on window
            screen2.blit(versus_image, versus_rect)
            screen2.blit(rock_image, rock_rect)
            screen2.blit(scissors_image,scissors_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)

            scissors_rect.y = HEIGHT/2
            scissors_rect.x = WIDTH/5
            rock_rect.x = WIDTH/0.85
            rock_rect.y = HEIGHT/2
        elif user_choice == "paper" and cpu == "scissors":
            # displays images on window
            screen2.blit(paper_image,paper_rect)
            screen2.blit(versus_image, versus_rect)
            screen2.blit(scissors_image, scissors_rect)
            screen2.blit(play_image, play_rect)
            screen2.blit(go, go_rect)
            
            paper_rect.y = HEIGHT/2
            scissors_rect.x = WIDTH/0.85
            scissors_rect.y = HEIGHT/2

        elif user_choice == cpu:
            # displays images on window
            screen2.blit(draw_image, draw_rect)
            screen2.blit(play_again, play_again_rect)
            
        pg.display.flip()

        # if play button is clicked, result page will show 
        if play_rect.collidepoint(mouse_coords):
            result_page()
            pg.quit()

        



# size of screen for screen 3
WIDTH3 = 550
HEIGHT3 = 550


# result_page function shows if the user won or loss through images 
def result_page():
    pg.init()
    pg.mixer.init()
    screen3 = pg.display.set_mode((WIDTH3, HEIGHT3))
    pg.display.set_caption('Game Results')
    clock2 = pg.time.Clock()
    running = True
    while running:
        clock2.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        #pulls winner image from folder
        winner_image = pg.image.load(os.path.join(game_folder, 'winner.jpg')).convert()
        winner_rect = winner_image.get_rect()
        #pulls loser image from folder
        loser_image = pg.image.load(os.path.join(game_folder, 'loser.jpg')).convert()
        loser_rect = loser_image.get_rect()
        # creates text
        play_again = font.render('PLAY AGAIN', True, GREEN, BLUE )
        play_again_rect = play_again.get_rect()
        play_again_rect.x = WIDTH/3
        play_again_rect.y = HEIGHT/1.25

        # fills screen 3 with white
        screen3.fill(WHITE)
    
        if user_choice == "rock" and cpu == "scissors":
            # displays images on window
            screen3.blit(winner_image, winner_rect)
            screen3.blit(play_again, play_again_rect)
        elif user_choice == "scissors" and cpu == "paper":
            # displays images on window
            screen3.blit(winner_image, winner_rect)
            screen3.blit(play_again, play_again_rect)
        elif user_choice == "paper" and cpu == "rock":
            # displays images on window
            screen3.blit(winner_image, winner_rect)
            screen3.blit(play_again, play_again_rect)
        elif user_choice == "rock" and cpu == "paper":
            # displays images on window
            screen3.blit(loser_image, loser_rect)
            screen3.blit(play_again, play_again_rect)
        elif user_choice == "scissors" and cpu == "rock":
            # displays images on window
            screen3.blit(loser_image, loser_rect)
            screen3.blit(play_again, play_again_rect)
        elif user_choice == "paper" and cpu == "scissors":
            
            screen3.blit(loser_image, loser_rect)
            screen3.blit(play_again, play_again_rect)
       
        pg.display.flip()

        # if button is clicked, will return to start screen
        running = True
        while running:
            clock2.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.MOUSEBUTTONUP:
                    # get function gets something right away
                    global mouse_coords
                    mouse_coords = pg.mouse.get_pos()
                    if play_again_rect.collidepoint(mouse_coords):
                        start_screen()
  

pg.quit()

# calls the starting function
start_screen()










