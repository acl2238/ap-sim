from turtle import Screen
import pygame, sys, pygame_gui, time, button
from pygame.locals import *
from typing_area import TypingArea # Code for making dialogue boxes
import dialogue # All lines

pygame.init() # Init all modules
pygame.display.set_caption('The C Programming Language (Second Edition)') # Captions window

# Determining screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Filling background Columbia Blue
#background = pygame.Surface((800, 600))
screen.fill(pygame.Color('#9BCBEB'))

# Init GUI
manager = pygame_gui.UIManager((800,600))

#Fonts
titlefont = pygame.font.Font('./EBGaramond-Regular.ttf', 52)
garamond = pygame.font.Font('./EBGaramond-Regular.ttf', 32)
garamondbold = pygame.font.Font('./EBGaramond-Bold.ttf', 32) 

# Colors
whitefont = (255,255,255)
blackfont = (0,0,0)
navyfont = (0,56,101)
bluefont = (155,203,235) 

# Load button images

# Helper method to load images (for buttons)
def loadimage(imgfile):
    return pygame.image.load(imgfile).convert_alpha()

# Loading images and turning them into buttons

yes_img = loadimage('button_yes.png') 
no_img = loadimage('button_no.png') 
start_img = loadimage('button_start.png') 
quit_img = loadimage('button_quit.png') 
continue_img = loadimage('button_continue.png')
yes_button = button.Button(50, 350, yes_img, 1)
no_button = button.Button(484, 350, no_img, 1)
start_button = button.Button(215, 100, start_img, 1)
quit_button = button.Button(243, 350, quit_img, 1)
continue_button = button.Button(246, 400, continue_img, 1)

# Pygame clock (made to tick faster later)
clock = pygame.time.Clock()
is_running = True

# States
has_started = False # Starts game after intro
weekcount = 1 # Counts week
yesorno = 2 # Yes = 1, No = 0
giveup_gamestart = 0 # For first week if player quits
cheater = False # If player decides to cheat, this set to true

# Misc variables
typespeed = 60 # How fast text will scroll 

# Used to determine midterm results and final grade
# Will always increment if yes is chosen, decrement if no is chosen
gradepoints = 1 # Tracks inter-week progress 
grade_checkpoint1 = 0 # After first exam, if done well, this will increment
grade_checkpoint2 = 0 # After second exam, if done well, this will increment
grade_checkpoint3 = 0 # Based on choices in 3rd exam, may increment

# Helper method to create textboxes
def textbox(msg):
    return TypingArea(msg, pygame.Rect(25,0,750,300), garamond, whitefont, bluefont, typespeed)

# All week dialogues, these lines make the text boxes

line1 = textbox(dialogue.week1_intro)
line1yes = textbox(dialogue.week1_yes)
line1no = textbox(dialogue.week1_no)

line2 = textbox(dialogue.week2_intro)
line2yes = textbox(dialogue.week2_yes)
line2no = textbox(dialogue.week2_no)

line3 = textbox(dialogue.week3_intro)
line3yes = textbox(dialogue.week3_yes)
line3no = textbox(dialogue.week3_no)

line4 = textbox(dialogue.week4_intro)
line4yes = textbox(dialogue.week4_yes)
line4no = textbox(dialogue.week4_no)

line5 = textbox(dialogue.week5_intro)
line5prep = textbox(dialogue.week5_intro_prep)
line5yes = textbox(dialogue.week5_yes)
line5no = textbox(dialogue.week5_no)

line6 = textbox(dialogue.week6_intro)
line6yes = textbox(dialogue.week6_yes)
line6no = textbox(dialogue.week6_no)

line7 = textbox(dialogue.week7_intro)
line7yes = textbox(dialogue.week7_yes)
line7no = textbox(dialogue.week7_no)

line8 = textbox(dialogue.week8_intro)
line8yes = textbox(dialogue.week8_yes)
line8no = textbox(dialogue.week8_no)

line9 = textbox(dialogue.week9_intro)
line9yes = textbox(dialogue.week9_yes)
line9no = textbox(dialogue.week9_no)

line10 = textbox(dialogue.week10_intro)
line10yes = textbox(dialogue.week10_yes)
line10no = textbox(dialogue.week10_no)

line11 = textbox(dialogue.week11_intro)
line11yes = textbox(dialogue.week11_yes)
line11no = textbox(dialogue.week11_no)

line12cheat = textbox(dialogue.week12_cheat)
line12a = textbox(dialogue.week12_a)
line12b = textbox(dialogue.week12_b)
line12c = textbox(dialogue.week12_c)


def week(intro, yes, no): # What the week does, calling choice and getting a y/n resp
    global giveup_gamestart
    global yesorno
    global weekcount
    global gradepoints
    global cheater
    global grade_checkpoint3
    intro.next_time = time.time() # Resets time so that text doesn't render early
    intro.update()
    intro.draw(screen)
    #pygame.display.flip() # Honestly not sure whether I need this or not
    choice(intro)
    if(yesorno == 0):
        no.next_time = time.time()
        no.update()
        no.draw(screen)
        if no.finished() == True:
            continue_button.show() # Blit continue button to screen
            if continue_button.draw(screen) == True: # If continue is pressed
                continue_button.hide()
                clearscreen()
                if weekcount == 10: # Special case if user cheats in Week 10
                    cheater = True
                yesorno = 2 # reset condition
                weekcount += 1
                # debugging
                print("wk", weekcount, "pts", gradepoints, "gcp1", grade_checkpoint1, "gcp2", grade_checkpoint2, "cht", cheater)    
    elif(yesorno == 1):
        yes.next_time = time.time()
        yes.update()
        yes.draw(screen)
        if yes.finished() == True:
            continue_button.show()
            if continue_button.draw(screen) == True:
                continue_button.hide()
                clearscreen()
                # Special case at start of game
                if weekcount == 1:
                    giveup_gamestart = 1
                if weekcount == 8: # Special case if user cheats in week 8
                    cheater = True
                if weekcount == 11:
                    grade_checkpoint3 = 1
                yesorno = 2
                if weekcount != 5: # Excludes test weeks
                    gradepoints += 1 
                weekcount += 1
                # debugging
                print("wk", weekcount, "pts", gradepoints, "gcp1", grade_checkpoint1, "gcp2", grade_checkpoint2, "cht", cheater)
    else:
        pass

# Clears screen
def clearscreen():
    screen.fill(pygame.Color('#9BCBEB'))

# Pushes yes/no buttons to screen, stores response in global yesorno
def choice(msg): 
    global yesorno
    if msg.finished() == True:
        if yesorno == 2:
            yes_button.show()
            no_button.show()
            if yes_button.draw(screen) == True:
                yesorno = 1
                print('yes')
                yes_button.hide()
                no_button.hide()
                clearscreen()
            if no_button.draw(screen) == True:
                yesorno = 0
                print('no')
                yes_button.hide()
                no_button.hide()
                clearscreen()

# Event loop

apsim = """AP Simulator (Jae approved!)""" # Game title
title = TypingArea(apsim, pygame.Rect(110,0,750,300), titlefont, whitefont, bluefont, typespeed)

while is_running:

    time_delta = clock.tick(30) # Clock set to run at x fps
    # print(weekcount) # test
    # Menu screen
    if has_started == False:
        title.update()
        title.draw(screen)
        if title.finished() == True:
            # If user changes their mind and doesn't want to play
            if quit_button.draw(screen) == True:
                is_running = False
            # If game is started, fill over menu
            if start_button.draw(screen) == True:
                has_started = True
                clearscreen()

    # Once user has pressed start
    if has_started == True:

        # Note: content wise, weeks don't actually resemble full weeks
        # There are some 'weeks' where multiple weeks worth of content pass
        # Weeks are just numbered for chronological convenience

        # Week 1
        if weekcount == 1:
            week(line1, line1yes, line1no)
            # If user decides to quit in first week
            if giveup_gamestart == 1:
                is_running = False
        
        # Week 2
        elif weekcount == 2:
            week(line2, line2yes, line2no)
        
        # Week 3
        elif weekcount == 3:
            week(line3, line3yes, line3no)

        # Week 4            
        elif weekcount == 4:
            week(line4, line4yes, line4no)
        
        # Week 5 - Midterm week
        elif weekcount == 5:
            # The choice here doesn't actually matter because cramming doesn't do shit
            # Result is based on prior grade points
            if gradepoints < 3:
                week(line5, line5no, line5no)
            else:
                week(line5prep, line5yes, line5yes)
                grade_checkpoint1 = 1

        # Week 6
        elif weekcount == 6:
            gradepoints = 0
            week(line6, line6yes, line6no)
            
        # Week 7
        elif weekcount == 7:
            week(line7, line7yes, line7no)

        # Week 8
        elif weekcount == 8:
            week(line8, line8yes, line8no)

        # Week 9 - Second midterm week
        elif weekcount == 9:
            if gradepoints > 1:
                grade_checkpoint2 = 1
            week(line9, line9yes, line9no)

         # Week 10
        elif weekcount == 10:
            gradepoints = 0
            week(line10, line10yes, line10no)     

        # Week 11 - Last exam
        elif weekcount == 11:
            week(line11, line11yes, line11no)

        # Final
        elif weekcount == 12:
            # Case 1: user gets caught cheating
            if cheater == True:
                line12cheat.next_time = time.time() # Resets time so that text doesn't render early
                line12cheat.update()
                line12cheat.draw(screen)
                if line12cheat.finished() == True:
                    continue_button.show()
                    if continue_button.draw(screen) == True:
                        is_running = False
                
            # Case 2: user made all the right choices, gets A
            if cheater == False and (grade_checkpoint1 + grade_checkpoint2 + grade_checkpoint1) == 3:
                line12a.next_time = time.time() # Resets time so that text doesn't render early
                line12a.update()
                line12a.draw(screen) 
                if line12a.finished() == True:
                    continue_button.show()
                    if continue_button.draw(screen) == True:
                        is_running = False

            # Case 3: user messed up 1 exam, gets B+
            if cheater == False and (grade_checkpoint1 + grade_checkpoint2 + grade_checkpoint3) == 2:
                line12b.next_time = time.time() # Resets time so that text doesn't render early
                line12b.update()
                line12b.draw(screen)
                if line12b.finished() == True:
                    continue_button.show()
                    if continue_button.draw(screen) == True:
                        is_running = False 

            # Case 3: user messed up 2 or 3 exams, gets C
            if cheater == False and (grade_checkpoint1 + grade_checkpoint2 + grade_checkpoint3) < 2:
                line12c.next_time = time.time() # Resets time so that text doesn't render early
                line12c.update()
                line12c.draw(screen) 
                if line12c.finished() == True:
                    continue_button.show()
                    if continue_button.draw(screen) == True:
                        is_running = False


    #print(gradepoints) # test
        
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)
    
    manager.update(time_delta)

    pygame.display.update()
