from random import randint as rand

class Creature:
    def __init__(self, health, hunger, energy, sleep, maxHealth, maxHunger, maxEnergy, maxSleep, dist, runSpeed):
        """Sets attributes when Creature is initialized"""

        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.sleep = sleep

        self.maxHealth = maxHealth
        self.maxHunger = maxHunger
        self.maxEnergy = maxEnergy
        self.maxSleep = maxSleep

        self.dist = dist

        self.runSpeed = runSpeed

    def Run(self):
        """Generates travel distance and stat loss for run action and updates Creature's attributes"""

        travelDist = rand(self.runSpeed[0], self.runSpeed[1])

        lostEnergy = rand(9, 22)
        lostHunger = rand(9, 22)
        lostSleep = rand(9, 14)

        self.energy = 0 if self.energy - lostEnergy < 0 else self.energy - lostEnergy
        self.hunger = 0 if self.hunger - lostHunger < 0 else self.hunger - lostHunger
        self.sleep = 0 if self.sleep - lostSleep < 0 else self.sleep - lostSleep

        self.dist = 200 if self.dist + travelDist > 200 else self.dist + travelDist

class Nova(Creature):
    def __init__(self):
        """Sets attributes (and inheritance) when Nova is initialized"""

        # Set inherited attributes
        Creature.__init__(self, 100, 100, 100, 100, 100, 100, 100, 100, 0, (10, 20))

        self.jogSpeed = (5, 12)

    def Jog(self):
        """Generates travel distance and stat loss for jog action and updates Nova's attributes"""

        travelDist = rand(self.jogSpeed[0], self.jogSpeed[1])

        lostEnergy = rand(4, 12)
        lostHunger = rand(4, 12)
        lostSleep = rand(6, 9)

        self.energy = 0 if self.energy - lostEnergy < 0 else self.energy - lostEnergy
        self.hunger = 0 if self.hunger - lostHunger < 0 else self.hunger - lostHunger
        self.sleep = 0 if self.sleep - lostSleep < 0 else self.sleep - lostSleep

        self.dist = 200 if self.dist + travelDist > 200 else self.dist + travelDist

    def Sleep(self):
        """Generate stat gain for sleep action and update Nova's attributes"""

        sleepGain = rand(12, 30)
        healthGain = rand(6, 17)
        energyGain = rand(17, 25)

        self.sleep = self.maxSleep if self.sleep + sleepGain > self.maxSleep else self.sleep + sleepGain
        self.health = self.maxHealth if self.health + healthGain > self.maxHealth else self.health + healthGain
        self.energy = self.maxEnergy if self.energy + energyGain > self.maxEnergy else self.energy + energyGain

    def Eat(self):
        """Generate stat gain for eat action and update Nova's attributes"""

        hungerGain = rand(7, 18)
        healthGain = rand(18, 27)
        energyGain = rand(14, 23)

        self.hunger = self.maxHunger if self.hunger + hungerGain > self.maxHunger else self.hunger + hungerGain
        self.health = self.maxHealth if self.health + healthGain > self.maxHealth else self.health + healthGain
        self.energy = self.maxEnergy if self.energy + energyGain > self.maxEnergy else self.energy + energyGain

    def __repr__(self):
        """
        Defines Nova's computational representation

        Returns Nova's stats as a formated string (used for outputing stats to the status bar)

        Called like `print(Nova)` or `str(Nova)`

        For more info on special methods, see: https://docs.python.org/2.0/ref/customization.html
        """

        return '|\tHealth: {}\t|\tHunger: {}\t|\tEnergy: {}\t|\tSleep: {}\t|\tTraveled: {}km\t|'.format(self.health, self.hunger, self.energy, self.sleep, self.dist)

class Wolf(Creature):
    def __init__(self):
        """Sets attributes (and inheritance) when Wolf is initialized"""

        Creature.__init__(self, 300, 60, 200, 80, 300, 60, 200, 100, -100, (7, 14))

    def ChooseAction(self):
        """Chosses what action Wolf does based off of it's stats"""

        if self.hunger < 11: self.hunger = self.maxHunger
        elif self.sleep < 7: self.sleep = self.maxSleep
        else: self.Run()