from random import randint as rand

class Creature():
    # Called when Creature is created
    def __init__(self, health, hunger, energy, sleep, maxHealth, maxHunger, maxEnergy, maxSleep, dist, runSpeed):
        # Set attributes
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

    # Set Run function for Creature
    def Run(self):
        # Generate random travel distance
        travelDist = rand(self.runSpeed[0], self.runSpeed[1])

        # Generate lost energy and hunger and sleep
        lostEnergy = rand(9, 22)
        lostHunger = rand(9, 22)
        lostSleep = rand(9, 14)

        # Update Creature's attributes
        self.energy = 0 if self.energy - lostEnergy < 0 else self.energy - lostEnergy
        self.hunger = 0 if self.hunger - lostHunger < 0 else self.hunger - lostHunger
        self.sleep = 0 if self.sleep - lostSleep < 0 else self.sleep - lostSleep

        # Update distance traveled (limit to 200)
        self.dist = 200 if self.dist + travelDist > 200 else self.dist + travelDist

class Nova(Creature):
    # Called when Nova is created
    def __init__(self):
        # Set inherited attributes
        Creature.__init__(self, 100, 100, 100, 100, 100, 100, 100, 100, 0, (10, 20))

        # Set Nova's jog speed
        self.jogSpeed = (5, 12)

    # Set functions for Nova's actions
    def Jog(self):
        # Generate random travel distance
        travelDist = rand(self.jogSpeed[0], self.jogSpeed[1])

        # Generate lost energy and hunger and sleep
        lostEnergy = rand(4, 12)
        lostHunger = rand(4, 12)
        lostSleep = rand(6, 9)

        # Update Nova's attributes
        self.energy = 0 if self.energy - lostEnergy < 0 else self.energy - lostEnergy
        self.hunger = 0 if self.hunger - lostHunger < 0 else self.hunger - lostHunger
        self.sleep = 0 if self.sleep - lostSleep < 0 else self.sleep - lostSleep

        # Update distance traveled (limit to 200)
        self.dist = 200 if self.dist + travelDist > 200 else self.dist + travelDist

    def Sleep(self):
        sleepGain = rand(12, 30) # Generate random sleep gain for sleep
        healthGain = rand(6, 17) # Generate random health gain for sleep
        energyGain = rand(17, 25) # Generate random energy gain for sleep

        # Update Nova's attributes
        self.sleep = self.maxSleep if self.sleep + sleepGain > self.maxSleep else self.sleep + sleepGain
        self.health = self.maxHealth if self.health + healthGain > self.maxHealth else self.health + healthGain
        self.energy = self.maxEnergy if self.energy + energyGain > self.maxEnergy else self.energy + energyGain

    def Eat(self):
        hungerGain = rand(7, 18) # Generate random hunger gain for eat
        healthGain = rand(18, 27) # Generate random health gain for eat
        energyGain = rand(14, 23) # Generate random energy gain for eat

        # Update Nova's attributes
        self.hunger = self.maxHunger if self.hunger + hungerGain > self.maxHunger else self.hunger + hungerGain
        self.health = self.maxHealth if self.health + healthGain > self.maxHealth else self.health + healthGain
        self.energy = self.maxEnergy if self.energy + energyGain > self.maxEnergy else self.energy + energyGain

    # Used to display Nova's stats
    def __repr__(self):
        return '|\tHealth: {}\t|\tHunger: {}\t|\tEnergy: {}\t|\tSleep: {}\t|\tTraveled: {}km\t|'.format(self.health, self.hunger, self.energy, self.sleep, self.dist)

class Wolf(Creature):
    # Called when Wolf is created
    def __init__(self):
        # Set inherited attributes
        Creature.__init__(self, 300, 60, 200, 80, 300, 60, 200, 100, -100, (7, 14))

    # Set function to choose Wolf's action
    def ChooseAction(self):
        if self.hunger < 11: self.hunger = self.maxHunger
        elif self.sleep < 7: self.sleep = self.maxSleep
        else: self.Run()