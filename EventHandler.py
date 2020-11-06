import pygame as pg

# Load image resources
IMG_EATING = pg.transform.scale(pg.image.load('./images/dog_eating.png'), (200, 100))
IMG_MOVING = pg.transform.scale(pg.image.load('./images/dog_move.png'), (200, 100))
IMG_SLEEPING = pg.transform.scale(pg.image.load('./images/dog_sleeping.png'), (200, 100))

# Initialize variables for later use
msg = None
playAgainDisplayed = False

def handle(btns, nova, wolf, window):
    """Handles all game events such as button clicks and UI updates"""

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
                # Play the animation for the action

                if btns[eat].collidepoint(pos):
                    if nova.hunger < nova.maxHunger:
                        nova.Eat()
                        wolf.ChooseAction()

                        animateAction("eat", window, nova, wolf)
                    else: msg = f"Nova is full. The wolves are {abs(nova.dist - wolf.dist)}km away!"

                if btns[jog].collidepoint(pos):
                    nova.Jog()
                    wolf.ChooseAction()

                    animateAction("jog", window, nova, wolf)

                if btns[run].collidepoint(pos):
                    nova.Run()
                    wolf.ChooseAction()

                    animateAction("run", window, nova, wolf)

                if btns[sleep].collidepoint(pos):
                    if nova.sleep < nova.maxSleep:
                        nova.Sleep()
                        wolf.ChooseAction()
                    
                        animateAction("sleep", window, nova, wolf)
                    else: msg = f"Nova isn't tired. The wolves are {abs(nova.dist - wolf.dist)}km away!"
            # If game is done, only accept play again
            elif btnPlayAgain.collidepoint(pos): playAgain()

def isDead(nova, wolf, window):
    """Checks if Nova is dead and sets the output message to reflect her death"""

    global msg

    if wolf.dist >= nova.dist: msg = "Nova died! The wolves caught her, but she was a tasty snack!"
    elif nova.health <= 0: msg = "Nova died! She ran out of health!"
    elif nova.hunger <= 0: msg = "Nova died! She ran out of hunger!"
    elif nova.energy <= 0: msg = "Nova died! She ran out of energy!"
    elif nova.sleep <= 0: msg = "Nova died! She ran out of sleep!"
    else: return False

    return True

def isWon(nova, window):
    """Checks if Nova has won and sets the output message to reflect that"""

    if nova.dist >= 200:
        global msg
        
        msg = "Nova won! She made it home safely thanks to your help!"
        return True

def forestOverlay(window):
    """Covers screen with forest image to hide previous frame"""

    bg = pg.transform.scale(pg.image.load("./images/ForestBG.jpg"), (500, 300)) # Load and size the image
    window.blit(bg, (0, 0)) # Output the image

def updateStatus(window, nova):
    """Updates the status bar to reflect Nova's stats"""

    # Add status bar to screen
    bar = pg.Surface((500, 50)).convert_alpha() # Create and size the status bar
    bar.fill((200, 255, 0, 100)) # Color the status bar
    window.blit(bar, (0, 0)) # Output status bar

    # Add Nova's status to the status bar
    font = pg.font.SysFont('cambria', 15) # Font object for text
    status = font.render(str(nova), True, (0, 0, 0)) # Nova's attributes rendered from class' __repr__()
    width, height = status.get_width(), status.get_height() # Get the size of the text for use in centering it
    window.blit(status, (250 - width / 2, 25 - height / 2)) # Output the status to the status bar (centered)

def handleOutput(window, nova, wolf):
    """Handles message output by calling outputMsg() with the output message (if it exists) or the default message"""

    outputMsg(window, msg) if msg else outputMsg(window, f"The wolves are {abs(nova.dist - wolf.dist)}km away!")

def outputMsg(window, msg):
    """Outputs the message from handleOutput() to the output bar"""

    # Add output bar to screen
    bar = pg.Surface((500, 50)).convert_alpha() # Create and size the output bar
    bar.fill((200, 255, 0, 130)) # Color the output
    window.blit(bar, (0, 250)) # Output the output bar

    # Add output to the output bar
    font = pg.font.SysFont('cambria', 15) # Font object for text
    output = font.render(f">> {msg}", True, (0, 0, 0)) # Text to output
    height = output.get_height() # Get the size of the text for use in alignment
    window.blit(output, (10, 275 - height / 2)) # Output the text to the output bar

def animateAction(action, window, nova, wolf):
    """Animates an image to reflect the player's action"""

    # Create a dictionary to link actions to images
    actionImgs = {
        "eat": IMG_EATING,
        "jog": IMG_MOVING,
        "run": IMG_MOVING,
        "sleep": IMG_SLEEPING
    }

    # Get the image for the action
    img = actionImgs[action]
    
    if action == "jog" or action == "run":
        # Define animation speed
        speed = 2 if action == "jog" else 3

        x = -200 # Set starting x position for animation

        # Runs while the image is still on screen
        while x < 500:
            # Redraw static parts to hide previous frame
            forestOverlay(window)
            updateStatus(window, nova)
            handleOutput(window, nova, wolf)

            # Draw the image at the correct position
            window.blit(img, (x, 200 - img.get_height() / 2))

            # Update display and increase animation's x position
            pg.display.update()
            x += speed
    else:
        # Initialize variables used for timing
        CLOCK = pg.time.Clock()
        time_elapsed = 0

        # While time elapsed is less than animation's FPS * (number of seconds for animation to last)
        while time_elapsed <= 60 * 2:
            # Redraw static parts to hide previous frame
            forestOverlay(window)
            updateStatus(window, nova)
            handleOutput(window, nova, wolf)

            # Draw the image at the correct position
            window.blit(img, (250 - img.get_width() / 2, 200 - img.get_height() / 2))

            # Add (1/FPS)/second to time_elapsed
            time_elapsed += 1

            # Preserve 60 FPS frame rate and update display
            CLOCK.tick(60)
            pg.display.update()

def showPlayAgainDialogue(window):
    """Displays the play again button and dialogue"""

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

def playAgain():
    """Resets the game variables and GUI and calls the init() method in Main.py"""

    # Declare variables globally
    global playAgainDisplayed, msg

    # Remove the play again screen
    playAgainDisplayed = False
    msg = None

    # Reinitialize the game
    from Main import init
    init()