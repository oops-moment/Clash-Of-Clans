import numpy as np
import points as pt
# imported time and stealth archers here
import time 
from characters import barbarians, dragons, balloons, archers , stealth_archers ,healers


class Building:
    def destroy(self,King):
        self.destroyed = True
        if self.type == 'wall':
            if(self.level >= 3):
             self.explode=1
             self.scan_for_targets(King)
            self.V.remove_wall(self)
        elif self.type == 'hut':
            self.V.remove_hut(self)
        elif self.type == 'cannon':
            self.V.remove_cannon(self)
        elif self.type == 'wizardtower':
            self.V.remove_wizard_tower(self)
        elif self.type == 'townhall':
            self.V.remove_town_hall(self)


class Hut(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
        self.health = 40           
        self.max_health = 40
        self.type = 'hut'
       

class Cannon(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (2, 2)
        self.V = V
        self.destroyed = False
                          
        self.type = 'cannon'       
        self.isShooting = False
        # DONE AS THE BONUS
        self.level = 2  # this level can be between 1 to 5
        self.attack_radius = 5 + (self.level)/2
        self.health = 60 + 30*self.level
        self.max_health = 60 + 30*self.level
        self.attack = 4+self.level



    def scan_for_targets(self, King):
        self.isShooting = False

        troops =barbarians + archers + [stealth_archer for stealth_archer in stealth_archers if stealth_archer.alive and (time.time() - stealth_archer.invisible_start_time) > 10]
  
        for troop in troops:
            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop)
                return
            
        if King.alive == False:
            return
    
        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King)

    def attack_target(self, target):

        if(self.destroyed == True):
            return
        target.deal_damage(self.attack)


class Wall(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False
                         #wall health 20
        self.type = 'wall'
        # DEFINE AS PART OF BONUS 
        self.level = 1  # this level can be between 1 to 5
        self.max_health = 100 + 40*self.level
        self.health = 100 + 40*self.level
        self.explode = 0
        self.explosion_demage = 200
        self.explosion_radius = 2
    
    
    def scan_for_targets(self,King):     
       
        i = self.position[0] - 2
        j = self.position[1] - 2
        troops = barbarians + archers + stealth_archers +healers
        if(King.alive == True):
            troops.append(King)

        for row in range(i, i+5):
            for col in range(j, j+5):
                if(row < 0 or col < 0):
                    continue
                for troop in troops:
                    if(troop.position[0] == row and troop.position[1] == col):
                        troop.deal_damage(self.explosion_demage)
                
class TownHall(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (4, 3)
        self.V = V
        self.destroyed = False
        self.health = 100                    # townhall health 100
        self.max_health = 100
        self.type = 'townhall'

# here add the that wizard can target stealth archers as well basically check if the time is less than 10 then troops be only
# barbarian and archers else include stealth archers as well

class WizardTower(Building):
    def __init__(self, position, V):
        self.position = position
        self.dimensions = (1, 1)
        self.V = V
        self.destroyed = False                    # health 60
        self.type = 'wizardtower'
        self.isShooting = False
# DONE AS BONUS
        self.level = 2  # this level can be between 1 to 5
        self.health = 60 + 30*self.level    
        self.attack = 4+self.level
        self.attack_radius = 5 + (self.level)/2
        self.max_health = 60 + 30*self.level

    def scan_for_targets(self, King):
        self.isShooting = False
        troops = healers+ barbarians + archers + dragons + balloons + [stealth_archer for stealth_archer in stealth_archers if stealth_archer.alive and (time.time() - stealth_archer.invisible_start_time) > 10]
        for troop in troops:
            if (troop.position[0] - self.position[0])**2 + (troop.position[1] - self.position[1])**2 <= self.attack_radius**2:
                self.isShooting = True
                self.attack_target(troop,0)
                return

        if King.alive == False:
            return

        if(King.position[0] - self.position[0])**2 + (King.position[1] - self.position[1])**2 <= self.attack_radius**2:
            self.isShooting = True
            self.attack_target(King,1)

    def attack_target(self, target, isKing):
        if(self.destroyed == True):
            return

        if isKing == 1:
            target.deal_damage(self.attack)
        i = target.position[0] - 1
        j = target.position[1] - 1
        troops = barbarians + archers  + dragons + balloons + stealth_archers +healers
        for row in range(i, i+3):
            for col in range(j, j+3):
                if(row < 0 or col < 0):
                    continue
                for troop in troops:
                    if(troop.position[0] == row and troop.position[1] == col):
                        troop.deal_damage(self.attack)


def shoot_cannons(King, V):
    for cannon in V.cannon_objs:
        V.cannon_objs[cannon].scan_for_targets(King)


def shoot_wizard_towers(King, V):
    for tower in V.wizard_tower_objs:
        V.wizard_tower_objs[tower].scan_for_targets(King)
