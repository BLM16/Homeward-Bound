import pygame as pg

msg = None

# Handles all game events
def handle(btns, nova, wolf, window):
    # Get the event
    for event in pg.event.get():
        # If the close button is clicked, stop the game
        if event.type == pg.constants.QUIT: quit(200)

        # Runs when a mouse button is released
        if event.type == pg.constants.MOUSEBUTTONUP:
            # Declare msg globally
            # Reset msg on every click
            global msg
            msg = None

            eat, jog, run, sleep = 0, 1, 2, 3 # Position of each button in btns
            pos = pg.mouse.get_pos() # Position of mouse on screen

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

# Checks if nova is dead
def isDead(nova, wolf, window):
    if wolf.dist >= nova.dist: outputMsg(window, "Nova died! The wolves caught her, but she was a tasty snack!")
    elif nova.health <= 0: outputMsg(window, "Nova died! She ran out of health!")
    elif nova.hunger <= 0: outputMsg(window, "Nova died! She ran out of hunger!")
    elif nova.energy <= 0: outputMsg(window, "Nova died! She ran out of energy!")
    elif nova.sleep <= 0: outputMsg(window, "Nova died! She ran out of sleep!")

# Checks if nova won
def isWon(nova, window):
    if nova.dist >= 200: outputMsg(window, "Nova won! She made it home safely thanks to your help!")

# Update status bar
def updateStatus(window, nova):
    pg.draw.rect(window, (141, 141, 141), (0, 0, 500, 50)) # Draw the status bar

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
    pg.draw.rect(window, (141, 141, 141), (0, 250, 500, 50)) # Draw the output bar

    # Font object for text
    font = pg.font.SysFont('cambria', 15)

    # Draw the output bar
    pg.draw.rect(window, (141, 141, 141), (0, 250, 500, 50))

    # Add output to the output bar
    output = font.render(f">> {msg}", True, (0, 0, 0))
    height = output.get_rect().height
    window.blit(output, (10, 275 - height / 2))