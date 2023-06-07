# Dass Assignment - 3

### PRISHA , 2021101075

# Assignment 3.1

- Everything mentioned in the assignment has been implemented.
- **Bonus** :
    - King’s Leviathan Axe has also been implemented.
    - Dragon Character has been added, it can fly over walls.
    - Queen's Eagle Arrow has been added.
    - Movement avoiding walls has also been implemented.

- To run the game : `python3 game.py`
- To view replays : `python3 replay.py`  and select the replay you want to watch according to mentioned date and time.
- For Victory : All buildings apart from walls get destroyed from the map in all three levels.
- For Defeat : If all troops and King die before destroying all buildings apart from walls.

## Controls :

### Hero :

- w : move up
- a : move left
- d : move right
- s : move down
- 1 : Special Attack
- space : Normal Attack

### Barbarian :

- z : spawn at point 1
- x : spawn at point 2
- c : spawn at point 3

### Dragon :

- v : spawn at point 1
- b : spawn at point 2
- n : spawn at point 3

### Archer :

- i : spawn at point 1
- o : spawn at point 2
- p : spawn at point 3


### Balloon :

- j : spawn at point 1
- k : spawn at point 2
- l : spawn at point 3

### Extending the given codebase

### Stealth Archer :

- t : spawn at point 1
- y : spawn at point 2
- u : spawn at point 3


### Healer :

- 7 : spawn at point 1
- 8 : spawn at point 2
- 9 : spawn at point 3

q : Quit Game

## Assumptions :

- Rage and Heal Spell can be applied multiple times.
- The limit for troops in each level is as follows :
    - Barbarians : 10
    - Archers : 7
    - Balloon : 5
    - Dragon : 3
- You have to choose the type of troop movement at start of the game.
- You have to choose the hero after each level.

### Extending the given codebase

## 1. Stealth Archer

- Cannot be targetted if current time is less than 10sec when compared to time of creation .
- Rest after 10 sec it works as normal archer (used concept of inheritance) can be targetted by cannon and wizard tower. Spawn limit of stealth archer is kept same as archer which is 7. 
- Stealth archer can be attacked it comes in grid of wizard and healradius of healer tho its invisible ( not direct target)
- Stealth archer when invisible can attack but can't be targetted

## 2. Healer

- Healer is an aerial troop like balloon , it moves to the closest wounded troop and heals it 
- Not only this, it has head radius then any target which comes inside that radius will be healed and also the troops which are in range 1 of that target will get healed.
- Spawn limit of the healer is kept 10. It can be attacked by Wizard Tower.


## Bonus

- Randomly levels are assigned to all the buildings between 1 and 5 (both inclusive).
- They can be manually changed in the classes and assign the level as desired . All the building's health are assigned the same as their max health.


If a wall of level >= 3 is destroyed then it explodes and damages all the ground troops(including King/Queen) if they come in the grid of radius 2 of the wall being exploded.

