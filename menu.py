# Program to create a basic window using the pygame_menu module 

import pygame as py
import pygame_menu as pm

py.init()

WIDTH, HEIGHT = 800, 600

# Screen and caption 
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Window using Pygame_menu")

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass
# Main Function 
def mainFun():
	menu = pm.Menu('Welcome to game', 400, 300,
							theme=pm.themes.THEME_BLUE)

	menu.add.text_input('Name :', default='John Doe')
	menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
	menu.add.button('Play', start_the_game)
	menu.add.button('Quit', pm.events.EXIT)

	# Displaying the menu on the screen using the "mainloop" method of pygame_menu.Menu 
	menu.mainloop(screen) 


if __name__ == "__main__": 
	mainFun() # Calling the main function 


# This code is contributed by Teja 
