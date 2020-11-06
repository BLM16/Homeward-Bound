Homeward Bound
==============
[![Python](https://img.shields.io/static/v1?logo=data:image/png;base64,R0lGODlhEAAQAPZkAOu7GOu+IfPBGvrHGf3LG//MHOvCKv/PI//PJP/QJf/QJv/TLf3SL//TLv/TL+vFNOjHPf/TMP/UMP3VNv/WN/rTOf/XOP/XOf/XOvnVPv/YOuzORf3ZQf/aQf/aQv/bQv/bQ//bRP3dSv/eS//fTf3eTv/fTv/iVf/jV//jWP/mYf/nYf/nYvLhbvXjb/3pav/rbDJghzZmkDZnkTVokjZpkzZplDdoljdqljlsljhslzltmTpvmzpwnDtwnDtwnTxxnj1zoD1zoj10oT50oj51oz92pUB4pkB4p0F5qEJ7qkN8q0N9rUN9rkR9rUR+rUV/r0aAsEaAsUaBskeBskiDtEiEtUiFtkmFt0qHuUqGukuIu0yJvEyKvE2LvkyKv06NwE+NwVCPw1KRxv///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAGUALAAAAAAQABAAAAemgGWCZWFaUkxGQDeDjIJdZFJKRD04jYxXkUQ+ODWWZV9XTEQ5Mjk4lYxjYVxVUEdAPDWnZScjGWViX1RQSrA1vzFlIx0Tn1dUkkCnNMEbxAtlx0tHnY0dFwsHZVLTNGUtLywnJiHYCARlTEpDZS4wLCnk5gUCgkM+Ze/xHRoLCAUFLMEzAeGBgQAAAHiKVy5CgoCeysiTkIAMuohlKjgsMACjx0GBAAA7&label=Python&message=3.7.9&color=brightgreen&link=https://www.python.org/)](https://www.python.org/) [![Pygame](https://img.shields.io/static/v1?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAGFBMVEUAAAAAAACAgAD//wCAgIDAwMD///+AAACPxMkjAAAAAXRSTlMAQObYZgAAAAFiS0dEBmFmuH0AAAAHdElNRQfkChYQOQKCb6wwAAABDElEQVQoz02SwW6DMAyGA9ruhdGdVwf1vNr0vlaOeh1SwgNUS56g1V5/jhMxfADl0///tgnG5OphZ7bVWkJ57Vb6Nnp7MKBUC5Z0J0S2n9UxpfRDdEz3KmmPKUVCeVRgFZxTSlZjmw34UIe4Z78BPZ7TfKVpEJkC6Z88wJjBSTORgIjQ5WGKIp+luGwgGbYApAKaKiCyNG2BGKriUi0CtO0+ruCggmXhCkAFLzG6q54n1t1eox98HgE8f2fwHrphCcxdx8yqCJcu+ChoBfM+DLO7PfhXQRODlBeFeygwLoTRScrtWSymka4Io5eIr/KRe500Z9ar63U7WAWmLQDXq21BCML/H9BDLqurmj9GC08XAMT9WgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMC0xMC0yMlQxNjo1NzowMiswMDowMAOZcKkAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjAtMTAtMjJUMTY6NTc6MDIrMDA6MDByxMgVAAAAAElFTkSuQmCC&label=Pygame&message=1.9.6&color=brightgreen&link=https://www.pygame.org/news)](https://www.pygame.org/news) [![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&link=https://mit-license.org/)](https://mit-license.org/)

![](https://repository-images.githubusercontent.com/305732072/7ed1a500-12d3-11eb-8f60-dac2a3c89610)

## Info

Author: [Bradley Myers](https://github.com/BLM16/)

> Date created: 08-10-2020 | Last updated: 06-11-2020

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
        * Gain hunger
        * Gain health
        * Gain energy
    * Jog
        * Move 5-12 kilometers
        * Uses energy
        * Uses hunger
        * Uses sleep
    * Run
        * Move 10-20 kilometers
        * Uses energy
        * Uses hunger
        * Uses sleep
    * Sleep
        * Gain sleep
        * Gain health
        * Gain energy

## Files

* [Classes.py](./Classes.py)
    * Contains the class structure for all the game objects
    * Contains the methods for the classes

* [EventHandler.py](./EventHandler.py)
    * Handles all game events (such as button clicks and GUI updating)
    * Calls the functions for the events

* [Main.py](./Main.py)
    * Contains the game GUI, class instances, and loop
    * Passes all game events to [EventHandler.py](./EventHandler.py)

## License
This game is licensed under the [MIT License](./LICENSE)