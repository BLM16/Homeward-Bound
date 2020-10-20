Homeward Bound
==============

## Info

> Author: Bradley Myers

> Date created: 08-10-2020 | Last updated: 20-10-2020

## Gameplay

### Objectives

* Get a dog named Nova to her home which is 200km away
* Keep Nova alive because she is being chased by wolves
* Balance Nova's stats: run out of something and she dies

### Controls/Displays

* Status bar
    > Nova's stats (Health, Hunger, Energy, Sleep, Distance traveled)
* Output bar
    > Game messages (Wolf distance, Win message, Death message)
* Buttons
    * Eat
        > Gain stats: Hunger & Health & Energy
    * Jog
        > Move between 5 and 12 kilometers
        
        > Uses stats: Energy & Hunger & Sleep
    * Run
        > Move between 10 and 20 kilometers
        
        > Uses stats: Energy & Hunger & Sleep
    * Sleep
        > Gain stats: Sleep & Health & Energy

## Files

* [Classes.py](./Classes.py)
    > Contains the class structure for all the game objects
    
    > Contains the methods for the classes

* [EventHandler.py](./EventHandler.py)
    > Handles all game events (such as button clicks and GUI updating)
    
    > Calls the functions for the events

* [Main.py](./Main.py)
    > Contains the game GUI, class instances, and loop
    
    > Passes all game events to [EventHandler.py](./EventHandler.py)