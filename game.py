import sys
import os

sys.path.append('./src')

import get_input
import village
import king
from map import printMap, showKingHealth, update_map
# here import stealth archers as well
from characters import spawnBarbarian, move_barbarians, spawnArcher, move_archers, spawnDragon, move_dragons, spawnBalloon, move_balloons, clearTroops , spawnStealthArcher,move_stealtharchers, move_healers,spawnHealer
from buildings import shoot_cannons, shoot_wizard_towers
from spells import rage_spell, heal_spell
import points as pt

getch = get_input.Get()

cnt = 0


level = 1

V = village.createVillage(level)



def Phealth(health_bar):
    if(King.health > 0):
        print()
        character = ""
        if(pt.hero == 0):
            character = "King's"
        elif(pt.hero == 1):
            character = "Queen's"
        print(character+ ' Health: ', end='')
        for i in range(len(health_bar)):
            print(health_bar[i], end='')
        print('')




os.system('clear')
print("Choose your Movement:\n1. Break walls\n2. Don't break walls if possible")
ch = int(input("Enter Choice: "))
if ch == 1:
    pt.movement = 2
elif ch == 2:
    pt.movement = 1
os.system('clear')
print("Choose your Hero:\n1. Barbarian King\n2. Archer Queen")
ch = int(input("Enter Choice: "))
if ch == 1:
    pt.hero = 0
elif ch == 2:
    pt.hero = 1
King = king.getHero(pt.hero)
os.system('clear')
printMap(V)
Phealth(showKingHealth(King.health))


def init_level(level):
    
    global V,King,cnt
    cnt = 0
    V = village.createVillage(level)
    os.system('clear')
    print("Choose your Hero:\n1. Barbarian King\n2. Archer Queen")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        pt.hero = 0
    elif ch == 2:
        pt.hero = 1
    King = king.getHero(pt.hero)
    os.system('clear')
    clearTroops()
    printMap(V)
    Phealth(showKingHealth(King.health))

# clear terminal

# #reposition cursor to top left
# print("\033[%d;%dH" % (0, 0), end='')

# while True:
#     pass




while(True):
    cnt += 1
    ch = get_input.input_to(getch)
    if ch == 'w':
        King.move('up', V)
    elif ch == 's':
        King.move('down', V)
    elif ch == 'a':
        King.move('left', V)
    elif ch == 'd':
        King.move('right', V)
    elif ch == '1':
        King.specialAttack(V,King)
    elif ch == ' ':
        King.normalAttack(V,King)
    elif ch == 'r':
        rage_spell(King)
    elif ch == 'h':
        heal_spell(King)
    elif ch == 'z':
        spawnBarbarian(V.spawn_points[0])
    elif ch == 'x':
        spawnBarbarian(V.spawn_points[1])
    elif ch == 'c':
        spawnBarbarian(V.spawn_points[2])
    elif ch == 'v':
        spawnDragon(V.spawn_points[0])
    elif ch == 'b':
        spawnDragon(V.spawn_points[1])
    elif ch == 'n':
        spawnDragon(V.spawn_points[2])
    elif ch == 'j':
        spawnBalloon(V.spawn_points[0])
    elif ch == 'k':
        spawnBalloon(V.spawn_points[1])
    elif ch == 'l':
        spawnBalloon(V.spawn_points[2])
    elif ch == 'i':
        spawnArcher(V.spawn_points[0])
    elif ch == 'o':
        spawnArcher(V.spawn_points[1])
    elif ch == 'p':
        spawnArcher(V.spawn_points[2])
    elif ch == 't':
        spawnStealthArcher(V.spawn_points[0])
    elif ch == 'y':
        spawnStealthArcher(V.spawn_points[1])
    elif ch == 'u':
        spawnStealthArcher(V.spawn_points[2])
    elif ch == '7':
        spawnHealer(V.spawn_points[0])
    elif ch == '8':
        spawnHealer(V.spawn_points[1])
    elif ch == '9':
        spawnHealer(V.spawn_points[2])
    elif ch == 'q':
        print('quit')
        break
    
    move_barbarians(V,pt.movement,King)
    move_archers(V,pt.movement,King)
    move_stealtharchers(V,pt.movement,King)
    move_healers(V,King)
    move_dragons(V,King)
    move_balloons(V,King)
    shoot_cannons(King, V)
    shoot_wizard_towers(King, V)


    if(cnt % 20 == 0):
        os.system('clear')
    print("\033[%d;%dH" % (0, 0), end='')
    printMap(V)
    Phealth(showKingHealth(King.health))
    if(V.check_if_game_over(King) == 1):  # next level
        level += 1
        init_level(level)
    elif(V.check_if_game_over(King) == 2):  # Victory
        os.system('clear')
        print('Victory')
        break
    elif(V.check_if_game_over(King) == 3):
        os.system('clear')
        print('Defeat')
        break

