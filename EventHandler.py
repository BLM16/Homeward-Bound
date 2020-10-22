import pygame as pg

# Initialize variables for later use
msg = None
playAgainDisplayed = False

# Handles all game events
def handle(btns, nova, wolf, window):
    # Get the event
    for event in pg.event.get():
        # If the close button is clicked, stop the game
        if event.type == pg.constants.QUIT: quit(200)

        # Runs when a mouse button is released
        if event.type == pg.constants.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos() # Position of mouse on screen

            # If game isn't done, accept button clicks
            if not playAgainDisplayed:
                # Declare msg globally
                # Reset msg on every click
                global msg
                msg = None

                eat, jog, run, sleep = 0, 1, 2, 3 # Position of each button in btns

                # Check if/what button was clicked
                # Verify that the action can be done
                # Call the method for the button
                # Call the method for Wolf's move

                if btns[eat].collidepoint(pos):
                    if nova.hunger < nova.maxHunger:
                        nova.Eat()
                        wolf.ChooseAction()
                    else: msg = f"Nova is full. The wolves are {abs(nova.dist - wolf.dist)}km away!"

                if btns[jog].collidepoint(pos):
                    nova.Jog()
                    wolf.ChooseAction()

                if btns[run].collidepoint(pos):
                    nova.Run()
                    wolf.ChooseAction()

                if btns[sleep].collidepoint(pos):
                    if nova.sleep < nova.maxSleep:
                        nova.Sleep()
                        wolf.ChooseAction()
                    else: msg = f"Nova isn't tired. The wolves are {abs(nova.dist - wolf.dist)}km away!"
            # If game is done, only accept play again
            else:
                # Check if play again was clicked
                if btnPlayAgain.collidepoint(pos): playAgain()

# Checks if nova died
def isDead(nova, wolf, window):
    global msg

    if wolf.dist >= nova.dist: msg = "Nova died! The wolves caught her, but she was a tasty snack!"
    elif nova.health <= 0: msg = "Nova died! She ran out of health!"
    elif nova.hunger <= 0: msg = "Nova died! She ran out of hunger!"
    elif nova.energy <= 0: msg = "Nova died! She ran out of energy!"
    elif nova.sleep <= 0: msg = "Nova died! She ran out of sleep!"
    else: return False

    return True

# Checks if nova won
def isWon(nova, window):
    if nova.dist >= 200:
        global msg
        
        msg = "Nova won! She made it home safely thanks to your help!"
        return True

# Cover previous layer with forest image
def forestOverlay(window):
    # Add forest image to screen
    bg = pg.transform.scale(pg.image.load("./images/ForestBG.jpg"), (500, 300)) # Load and size the image
    window.blit(bg, (0, 0)) # Output the image

# Updates status bar
def updateStatus(window, nova):
    # Add status bar to screen
    bar = pg.Surface((500, 50)).convert_alpha() # Create and size the status bar
    bar.fill((200, 255, 0, 100)) # Color the status bar
    window.blit(bar, (0, 0)) # Output status bar

    # Add Nova's status to the status bar
    font = pg.font.SysFont('cambria', 15) # Font object for text
    status = font.render(str(nova), True, (0, 0, 0)) # Nova's attributes rendered from class' __repr__()
    width, height = status.get_rect().width, status.get_rect().height # Get the size of the text for use in centering it
    window.blit(status, (250 - width / 2, 25 - height / 2)) # Output the status to the status bar (centered)

# Handles output messages
def handleOutput(window, nova, wolf):
    # Outputs special message if there is one, otherwise outputs default message
    outputMsg(window, msg) if msg else outputMsg(window, f"The wolves are {abs(nova.dist - wolf.dist)}km away!")

# Outputs a message to the output bar
def outputMsg(window, msg):
    # Add output bar to screen
    bar = pg.Surface((500, 50)).convert_alpha() # Create and size the output bar
    bar.fill((200, 255, 0, 130)) # Color the output
    window.blit(bar, (0, 250)) # Output the output bar

    # Add output to the output bar
    font = pg.font.SysFont('cambria', 15) # Font object for text
    output = font.render(f">> {msg}", True, (0, 0, 0)) # Text to output
    height = output.get_rect().height # Get the size of the text for use in alignment
    window.blit(output, (10, 275 - height / 2)) # Output the text to the output bar

# Displays play again dialouge
def showPlayAgainDialogue(window):
    # Declare variables globally
    global btnPlayAgain, playAgainDisplayed

    btnPlayAgain = pg.draw.rect(window, (141, 141, 141), (150, 110, 200, 80)) # Draw the button

    # Add text to the play again button
    font = pg.font.SysFont('cambria', 30) # Font object for text
    text = font.render("Play Again", True, (0, 0, 0)) # Text to output
    width, height = text.get_rect().width, text.get_rect().height # Get the size of the text for use in centering it
    window.blit(text, (250 - width / 2, 150 - height / 2)) # Output the text to the play again button (centered)

    # Update the game to 'play again screen mode'
    playAgainDisplayed = True

# Resets variables and GUI
def playAgain():
    # Declare playAgainDisplayed globally
    global playAgainDisplayed, msg

    # Remove the play again screen
    playAgainDisplayed = False
    msg = None

    # Reinitialize the game
    from Main import init
    init()