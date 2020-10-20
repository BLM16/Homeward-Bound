import pygame as pg
import pygame.freetype as pg_ft
import EventHandler as EH
from Classes import Nova, Wolf

# Initialize used pygame modules
pg_ft.init()
pg.font.init()

# Called to initialize game
def init():
    # Declare variables globally
    global window, btns, Nova, Wolf

    # Setup the game window
    window = pg.display.set_mode((500, 400))
    pg.display.set_caption('Homeward Bound')
    pg.display.set_icon(pg.image.load("icon.png"))
    window.fill((255, 255, 255))

    # Create list of game buttons
    btns = [
        pg.draw.rect(window, (141, 141, 141), (15, 310, 110, 80)), # Eat button
        pg.draw.rect(window, (141, 141, 141), (135, 310, 110, 80)), # Jog button
        pg.draw.rect(window, (141, 141, 141), (255, 310, 110, 80)), # Run button
        pg.draw.rect(window, (141, 141, 141), (375, 310, 110, 80)) # Sleep button
    ]

    font = pg_ft.SysFont('cambria', 32) # Font object for button text

    # Add name of action to the buttons
    font.render_to(window, (48, 342), 'Eat', (0, 0,0))
    font.render_to(window, (168, 342), 'Jog', (0, 0, 0))
    font.render_to(window, (282, 342), 'Run', (0, 0, 0))
    font.render_to(window, (393, 342), 'Sleep', (0, 0, 0))

    # Initialize Nova and Wolf
    Nova, Wolf = Nova(), Wolf()

init() # Initialize the game

# Game loop
while True:
    # Call the event handler
    EH.handle(btns, Nova, Wolf, window)

    # Update status bar
    EH.updateStatus(window, Nova)

    # Handle output to the screen
    EH.handleOutput(window, Nova, Wolf)

    EH.isDead(Nova, Wolf, window) # Check if Nova died    
    EH.isWon(Nova, window) # Check if Nova won

    # Update the game display
    pg.display.update()