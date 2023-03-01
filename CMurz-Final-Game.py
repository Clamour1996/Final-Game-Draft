### Game ###

# To Do
## Too Done

## Create enemy index 
## Add randomized enemies 
## Add faith stat 
## Add ways to increase faith
## Punish continuous dodging 
## Fix Values and Index References for 3rd Floor
## Add multiple floors 
## Add final boss
## Add ending
## Add hint system
# Adjust timings
## Add Witch
## Add interactable room events
# Playtest (Cracked wand especially)
# Balance


## Modules

import random
import time
import os


## Introduction

while True:
    startscreen = "\nStart Game? \n[Y] or [N]"
    print(startscreen.center(12, "~"))
    ynresponse = input()
    ynresponse = ynresponse.lower()
    if ynresponse == "y":
        break
    if ynresponse == "n":
        print("An odd choice, then!")
        quit()
    else:
        print("And what is that supposed to mean?")
        time.sleep(2)
        print("This game is all about paying attention!")
        time.sleep(3)
        continue
time.sleep(2)
print("Welcome to the Python's Lair!\nA dungeon-crawling adventure into the den of the mystical serpent,\n\"Com-pyu Tar\"")
time.sleep(6)
print("Will you execute the beast? Or be terminated in the depths of its dungeon?")
time.sleep(6)

## Player Statistics

playerhealth = 500
faith = 1

while True:
    print("Choose a weapon! Iron Spear [1], Crystal Shield [2], or Cracked Wand [3]")
    weaponchoice = int(input())
    if weaponchoice == 1:
        weaponattack = 6
        print("You grabbed the spear! A mighty weapon with a hardened point.")
        break
    if weaponchoice == 2:
        weaponattack = 4
        playerhealth = playerhealth * 3
        print("You grabbed the shield! A defensive tool for a cautious warrior.")
        break
    if weaponchoice == 3:
        weaponattack = 1
        playerhealth = playerhealth / 5
        print("You grabbed the wand? An odd tool for a adventurer, but to each their own.")
        break
    else:
        continue
time.sleep(5)


## Functions

def multiplier():
    if weaponchoice == 1:
        return random.randint(5, 20) * faith
    if weaponchoice == 2:
        return random.randint(5, 20) * faith
    if weaponchoice == 3:
        return random.randint(0, 100) * faith
    
def floor1rooms():
    roomstate = random.randint(1, 5)
    return roomstate

def floor2rooms():
    roomstate = random.randint(1, 10)
    return roomstate

def floor3rooms():
    roomstate = random.randint(1, 15)
    return roomstate

def enemydecision():
    if floorcounter == 1:
        return random.randint(1,4)
    if floorcounter == 2:
        return random.randint(1,7)
    if floorcounter == 3:
        return random.randint(1,9)
    if floorcounter == "boss":
        return random.randint(1,6)


## Indecies ##

# Advice Index

travelerresponsedictionary = {
    1 : "Hm, it's important to read the room, wouldn't you say?",
    2 : "I would only act if I was sure of myself.",
    3 : "What happens once will surely happen again."
}

adventurerhintdictionary = {
    1 : "\"This first floor isn't too bad, huh?\nYou can tell how much danger you're in\njust by how intense the monsters move.\"",
    2 : "\"I hear their a witch somewhere in Com-Pyu Tar.\nI've wonder if there's a way to get on their good side?\nWhat would a witch like?\"",
    3 : "\"You gotta be careful when you counter\nMiss-time it, and you're in for some pain!\"",
    4 : "\"They might be monsters, but they get tired too!\nThat's when I attack!\"",
    5 : "\"Shit...I got hit hard...\nI thought I could just dodge all day...\nUgh...But...they eventually catch on...\"",
    6 : "\"Who built Com-Pyu Tar?\nI heard it was one of the gods.\nI'm a believer in the Goddess Dell, myself.\"",
    7 : "\"Some of these rooms...I feel like they're hinting at something.\nI'd better pay attention.\"",
    8 : "\"I'm a spellcaster.\nHeal you? Buddy, I'm not made of MP.\n...You want a favor from a magician? Compliment their INT\"",
    9 : "\"AHHHH MY HAND A MIMIC BIT MY HAND\nIT BIT MY HAND OFF WITH ITS TEETH\nITS TEETH BIG SILVER TEETH\nOH GOD LENOVO WHY IS THIS HAPPENING\""
    }

# Chest Index

chestindex = {
    1 : {"desc" : "You find a small chest with rusted hinges.",
    "prize" : "There's nothing inside.",
    "heal" : "10",
    "after" : "Disappointing, but at least you can take a break."
    },
    2 : {"desc" : "You find a small chest with rusted hinges.",
    "prize" : "There's a medical herb.",
    "heal" : "40",
    "after" : "Chewing on the herb, you resume your adventure."
    },
    3 : {"desc" : "You find a chest with silver hinges.",
    "prize" : "Before you can touch it, the chest swings open!\nRows of silvery teeth rip into your hand!",
    "heal" : "-200",
    "after" : "You manage to escape the mimic, clutching your wound."
    },
    4 : {"desc" : "You find a chest with an iron lock.",
    "prize" : "You faintly hear peals of laughter, chimes of bells, and a soothing light fills the room.",
    "heal" : "230",
    "after" : "Vigor renewed, you stride onwards."
    },
    5 : {"desc" : "You find a massive chest with a golden trim.",
    "prize" : "There's a smaller chest inside.", # This printed 5 times for some reason; I'm not sure why
    "heal" : "-5",
    "after" : "You give up."
    },
    6 : {"desc" : "You find a chest with a stone lid.",
    "prize" : "There's a small fox statue. It's warm to the touch, like it's filled with fire.",
    "heal" : "98",
    "after" : "Tucking the statue into your pocket, you continue on your way."
    },
}


# Enemy Index & Stats

enemytype = {
    1 : {"name" : "slimeball",
        "hp" : 600,
        "atk" : 20,
        "int" : 20,
        1 : "Enemy bounces into the air!",
        2 : "Enemy hops forward",
        3 : "Enemy rolls forward",
        4 : "Enemy slime jiggles ominously",
        "ctr" : "The slime bounces angrily"},
    2 : {"name" : "Pyre Bat",
        "hp" : 230,
        "atk" : 40,
        "int" : 12,
        1 : "Enemy begins a dive!",
        2 : "Enemy bares its fangs",
        3 : "Enemy screeches angrily",
        4 : "Enemy flutters around",
        "ctr" : "countermove"
        },
    3 : { "name" : "Rattled Snake",
        "hp" : 400,
        "atk" : 65,
        "int" : 7,
        1 : "Enemy begins to rattle its tail!",
        2 : "Enemy panicks and shows its fangs",
        3 : "Enemy flinches and slithers forward",
        4 : "Enemy begins to back up",
        "ctr" : "countermove"
        },
    4 : { "name" : "Living Armor",
        "hp" : 1620,
        "atk" : 100,
        "int" : 25,
        1 : "Enemy raises their sword",
        2 : "Enemy's sword glows with power",
        3 : "Enemy clanks defiantly",
        4 : "Enemy assumes a thrusting stance",
        5 : "Enemy assumes a cutting stance",
        6 : "Enemy punches with their offhand",
        7 : "Enemy begins to stretch",
        "hint" : "A wall-drawing of a person in armor?\nTheir hands are raised above their head, holding a glowing weapon\nCreatures shy away from the sword's power."
        },
    5 : { "name" : "Psychic Eyes",
        "hp" : 1320,
        "atk" : 110,
        "int" : 6,
        1 : "Enemy's eyes turn blue",
        2 : "Enemy's eyes turn red",
        3 : "Enemy's pupils dilate",
        4 : "Enemy begins to glare",
        5 : "Enemy blinks angrily",
        6 : "Enemy bobs side-to-side",
        7 : "Enemy winks at you",
        "hint" : "An engraving of eyes seems to follow your every move.\nFaint pigments color the iris: Red in one eye, blue in the other.\nIt's unsettling."
        },
    6 : { "name" : "Crazed Adventurer",
        "hp" : 300,
        "atk" : 700,
        "int" : 2,
        1 : "Enemy screams with rage",
        2 : "Enemy charges angrily",
        3 : "Enemy begins to sob",
        4 : "Enemy begins to cough up blood",
        5 : "Enemy pleads for mercy",
        6 : "Enemy calls for their dead friends",
        7 : "Enemy blankly stares into the distance",
        "hint" : "You find a journal discarded on the ground.\n\"I don't know how long I've been in here.\nThose bastards took my food.\nIf I ever find them...\nYOU NEED TO KILL TO EAT\nKILL K LL  I L    K   \"\nThe rest of the journal is torn."
        },
    7 : { "name" : "Flu Wyrm",
        "hp" : 2000,
        "atk" : 130,
        "int" : 19,
        1 : "Enemy hacks up a glob of lava",
        2 : "Enemy coughs up a fireball",
        3 : "Enemy's fever boils the air around them",
        4 : "Enemy stumbles and swipes at you",
        5 : "Enemy sneezes, swinging its head at you",
        6 : "Enemy flies into the air, but blacks out and crashes down",
        7 : "Enemy lazily crawls forward",
        8 : "Enemy nauseously gnashes its teeth",
        9 : "Enemy coughs up smoke",
        "hint" : "A etching on the wall depicts a great dragon, terrorizing a village.\nA plague doctor offers it a livestock to eat.\nIn the final etching, the dragon sits in a burning village.\nIt looks like its nose is running?"
        },
    8 : { "name" : "Dance Golem",
        "hp" : 2400,
        "atk" : 120,
        "int" : 10,
        1 : "Enemy does the robot, and tries to pass it to you",
        2 : "Enemy starts a wave, and passes it to you",
        3 : "Enemy starts breakdancing",
        4 : "Enemy starts throwing it back",
        5 : "Enemy starts to waltz",
        6 : "Enemy is feeling the groove",
        7 : "Enemy is ferociously doing the macarena",
        8 : "Enemy starts to cha cha",
        9 : "Enemy takes a quick breather",
        "hint" : "A group of statues litter the room, in various poses.\nThey seem to show the sequence of a dance.\nYou attempt to copy one of the poses, but nearly throw your back out.\nLet's not do that again."
        },
    9 : { "name" : "Hell Hound",
        "hp" : 1300,
        "atk" : 220,
        "int" : 10,
        1 : "\"I know you, " + os.getlogin() + "\"",
        2 : "\"Try to know me, " + os.getlogin() + ", and ask: Why are you here?\"",
        3 : "Enemy approaches",
        4 : "Enemy stalks closer",
        5 : "\"Does the fool even know why they're here?\"",
        6 : "\"What's wrong? Feeling nervous?\"",
        7 : "Enemy grins",
        8 : "Enemy snarls",
        9 : "Enemy gives you time to reconsider",
        "hint" : "A polished silver mirror stands in the center of the room.\nIt's frame is decorated with ornate carvings of hunting dogs.\nYou lean in closer, but it's just your reflection."
        },
}

bossstats = {
    "name" : "Python",
    "hp" : 30000,
    "atk" : 300,
    "int" : 9,
    1 : "The Python raises the blade affixed to its tail",
    2 : "The Python flashes its multicolored teeth, preparing a breath attack",
    3 : "The Python sweeps its tail across the arena",
    4 : "The Python lunges at you",
    5 : "\"Oh, I'm having such fun!\"",
    6 : "\"Did you know the people I swallow never truly die?\"",
}


## Enter Dungeon ##

print("Weapon in hand, you set out to conquer Com-Pyu Tar.")
time.sleep(2)
print("On the road, a weary traveler stops you, offering advice.")
time.sleep(1)
print("Do you accept?\n[Y] or [N]")
ynresponse = input()
ynresponse = ynresponse.lower()
if ynresponse == "y":
    travelerresponse = random.randint(1, 3)
    print("\"" + travelerresponsedictionary[travelerresponse] + "\"")
    time.sleep(3)
    print("With that, they leave.")
    time.sleep(2)
print("You approach the looming dungeon, and enter its yawning maw.")
time.sleep(4)

## Floor 1

floorcounter = 1
roomcounter = 0
spurnnedcounter = 0

battlestate = False
enemyturn = False
playerturn = True

counterfail = 0
counterwin = 0
dodgecounter = 0


while roomcounter < 4:
    roomstate = floor1rooms()
    opponent = random.randint(1, 3)
    print("You begin to battle a " + enemytype[opponent]["name"])
    enemyhealth = enemytype[opponent]["hp"]
    enemyattack = enemytype[opponent]["atk"]
    time.sleep(2)
    battlestate = True
    while battlestate == True:
        while playerturn == True:
            print("\nPlayer turn")
            print("HP: " + str(playerhealth))
            print(enemytype[opponent]["name"] + ": " + str(enemyhealth))
            time.sleep(3)
            attackroll = (weaponattack * multiplier())
            enemychoice = enemydecision()
            print(enemytype[opponent][enemychoice])
            time.sleep(2)
            print("What will you do? \n[A]ttack, [C]ounter, [D]odge")
            try:
                battlechoice = input()
            except: # Not sure what this part is for
                continue
            battlechoice = battlechoice.lower()
            if battlechoice == "a":
                enemyhealth = enemyhealth - attackroll
                print("You do " + str(attackroll) + " damage!")
            if battlechoice == "c" and enemychoice == 1:
                enemyhealth = enemyhealth - (attackroll * 4)
                print("You counter the attack and do " + str(attackroll * 4) + " damage!")
                counterwin = 1
            if battlechoice == "c" and enemychoice > 1:
                enemyhealth = enemyhealth - attackroll
                print("You try to counter the attack and do " + str(attackroll) + " damage!")
                print("But you miss-timed the counterattack!")
            if battlechoice == "d":
                dodgecounter += random.randint(1,3)
                print("You wait for an attack...") # Maybe put something in for the event that the user types something other than a, c, or d
            enemyturn = True
            playerturn = False
            time.sleep(3)
        while enemyturn == True:
            print("\nEnemy turn")
            enemyturn = False
            playerturn = True
            if dodgecounter > enemytype[opponent]["int"] and battlechoice == "d" and random.randint(0,2) % 2 == 0:
                enemychoice = 0
                playerhealth = playerhealth - (enemyattack * 2)
                print("Enemy saw through your evasion! You lose " + str(enemyattack * 3) + " health.")
            if enemychoice == 1 and battlechoice == "a":
                playerhealth = playerhealth - (enemyattack * 4)
                print("The enemy strikes powerfully!")
                print("You lose " + str(enemyattack * 3) + " health.")
            if enemychoice == 1 and counterwin == 1:
                print("The enemy's strong attack is stopped in its tracks!")
            if enemychoice == 1 and battlechoice == "d":
                print("The enemy strikes powerfully!")
                print("But you roll out of the way!")
            if (enemychoice == 2 and battlechoice != "d") or (enemychoice == 3 and battlechoice != "d"):
                playerhealth = playerhealth - enemyattack
                print("You take " + str(enemyattack) + " damage.")
            if (enemychoice == 2 and battlechoice == "d") or (enemychoice == 3 and battlechoice == "d"):
                print("You dodge out of the way and take no damage!")
            if enemychoice == 4:
                print("The enemy looks on, but does not act.")
            if weaponchoice == 3 and attackroll > 20 and attackroll < 221:
                playerhealth += (attackroll - 20)
                print("The Cracked Wand glows, absorbing some health from the opponent")
            if playerhealth <= 0:
                print("You're out of health!\nGAME OVER")
                time.sleep(3)
                quit()
            counterwin = 0
            counterfail = 0
            dodgecounter = dodgecounter - 1
            if enemyhealth <= 0: # This part should be under playerturn
                if playerhealth >= 450:
                    print("You won, with nary a scratch on you!\n")
                if playerhealth < 450 and playerhealth >= 200:
                    print("After a hard fight, you won!\n")
                if playerhealth < 200 and playerhealth > 50:
                    print("It was difficult, but you came out on top.\n")
                if playerhealth <= 50:
                    print("Your wounds are severe, but you survived.\n")
                battlestate = False
                roomcounter += 1
        time.sleep(3)
    print("\nNearby, something catches your attention:")
    if roomstate % 2 == 0:
        print("You come upon a fellow adventurer.")
        time.sleep(2)
        print("Swap Advice?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            adventurerhintroll = random.randint(1,9)
            print(adventurerhintdictionary[adventurerhintroll] + "\n")
        else:
            print("They shrug.")
            time.sleep(1)
            print("\"To each their own, pal.\"\n")
            spurnnedcounter += 1
        time.sleep(5)
    if roomstate % 2 == 1:
        chestchoice = random.randint(1,6)
        chesthealvalue = int(chestindex[chestchoice]["heal"])
        time.sleep(2)
        print(chestindex[chestchoice]["desc"])
        time.sleep(2)
        print("Will you open it?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            if chestchoice == 5:
                for i in range(6 + spurnnedcounter - faith):
                    print(chestindex[chestchoice]["prize"])
                    time.sleep(2)
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(3)
            else:
                print(chestindex[chestchoice]["prize"])
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(5)
                if playerhealth <= 0:
                    print("You're out of health!\nGAME OVER")
                    time.sleep(3)
                    quit()
        else:
            print("You decide to leave it alone.")
            time.sleep(3)
    if roomstate == 1 or roomstate == 2: # The way this is written, this never happens because one of the previous two "if" statements will have already applied.
        print("There's an old altar in the back of the room.")
        time.sleep(2)
        print("Rest?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            print("You rest for a while, and no monsters appear")
            time.sleep(3)
            if playerhealth < 50:
                faith += 3
                print("It's a welcome rest.\nYou know there's someone watching out for you.")
            if playerhealth < 300:
                faith += 2
                print("It's a welcome rest.\nYou feel as if there's someone watching out for you.")                
            else:
                faith += 1
                print("It's a nice rest.")
            time.sleep(4)
    print("You move to room " + str(roomcounter + 1))

time.sleep(2)
print("You cleared the 1st floor!\nYou venture deeper into Com-Pyu Tar...\n")
time.sleep(3)



## Floor Event 1

print("You encounter a hooded stranger.")
time.sleep(2)
print("\"Hey fella. Care to make a deal?\"")
print("Do you?")
print(r"[Y] or [N]")
ynresponse = str(input())
ynresponse = ynresponse.lower()
while True:
    if ynresponse == "y":
        print("\"Let's see... You got " + str(playerhealth) + " health left.")
        time.sleep(2)
        print("Offer me some, and I might just give you something good, ehehe.\"")
        time.sleep(1)
        print("Your Offer:")
        offer = int(input())
        if offer >= playerhealth:
            print("Hehehe- What? No- I'm not-")
            time.sleep(2)
            print("No. I'm not doing that.")
            break
        if offer < 100:
            print("\"Eheheh- Really? That's it?\"")
            time.sleep(2)
            print("You feel something small change within you.")
            weaponattack += 1
        if offer >= 100 and offer < 500:
            print("\"Not bad, not bad. \"")
            time.sleep(2)
            print("You feel something small change within you.")
            faith += random.randint(1,2)
        if offer >= 500:
            print("\"WHOA! Okay, now we're talking!\"")
            time.sleep(2)
            print("You feel something big change within you!")
            faith += 1
            weaponattack += 5
        playerhealth -= int(offer)
        break
    else:
        print("\"Damn.\"")
        time.sleep(3)
        break
print("They sprint away.\nWhat was that about?\n")
time.sleep(6)




## Floor 2

floorcounter = 2
roomcounter = 4

battlestate = False
enemyturn = False
playerturn = True

counterfail = 0
counterwin = 0
dodgecounter = 0

while roomcounter >= 4 and roomcounter <= 9:
    roomstate = floor2rooms()
    opponent = random.randint(4, 6)
    print("As you stalk the dungeon,\nyou notice something:\n")
    time.sleep(3)
    print(enemytype[opponent]["hint"])
    time.sleep(10)
    print("Suddenly, you're attacked!")
    time.sleep(3)
    print("\nYou begin to battle a " + enemytype[opponent]["name"])
    enemyhealth = enemytype[opponent]["hp"]
    enemyattack = enemytype[opponent]["atk"]
    time.sleep(3)
    battlestate = True
    while battlestate == True:
        while playerturn == True:
            print("\nPlayer turn")
            print("HP: " + str(playerhealth))
            print(enemytype[opponent]["name"] + ": " + str(enemyhealth))
            time.sleep(4)
            attackroll = (weaponattack * multiplier())
            enemychoice = enemydecision()
            print(enemytype[opponent][enemychoice])
            time.sleep(3)
            print("What will you do? \n[A]ttack, [C]ounter, [D]odge")
            try:
                battlechoice = input()
            except:
                continue
            battlechoice = battlechoice.lower()
            if battlechoice == "a":
                enemyhealth = enemyhealth - attackroll
                print("You do " + str(attackroll) + " damage!")
            if battlechoice == "c" and enemychoice >= 1 and enemychoice <= 2:
                enemyhealth = enemyhealth - (attackroll * 4)
                print("You counter the attack and do " + str(attackroll * 4) + " damage!")
                counterwin = 1
            if battlechoice == "c" and enemychoice > 2:
                enemyhealth = enemyhealth - (attackroll / 2)
                counterfail = 1
                print("You try to counter the attack and do " + str(attackroll) + " damage!")
                print("But you miss-timed the counterattack!")
            if battlechoice == "d":
                dodgecounter += random.randint(0,3)
                print("You wait for an attack...")
            enemyturn = True
            playerturn = False
            time.sleep(4)
        while enemyturn == True:
            print("\nEnemy turn")
            enemyturn = False
            playerturn = True
            if dodgecounter > enemytype[opponent]["int"] and battlechoice == "d" and random.randint(0,2) % 2 == 0:
                enemychoice = 0
                playerhealth = playerhealth - (enemyattack * 3)
                print("Enemy saw through your evasion! You lose " + str(enemyattack * 3) + " health.")
            if enemychoice >= 1 and enemychoice <= 2 and battlechoice == "a":
                playerhealth = playerhealth - (enemyattack * 3)
                print("The enemy strikes powerfully!")
                print("You lose " + str(enemyattack * 3) + " health.")
            if enemychoice >= 1 and enemychoice <= 2 and counterwin == 1:
                print("The enemy's strong attack is stopped in its tracks!")
            if enemychoice >= 1 and enemychoice <= 2 and battlechoice == "d":
                print("The enemy strikes powerfully!")
                print("But you roll out of the way!")
            if enemychoice >= 3 and enemychoice <= 6 and battlechoice != "d":
                playerhealth = playerhealth - enemyattack
                print("You take " + str(enemyattack) + " damage.")
            if (enemychoice >= 3 and enemychoice <= 6 and battlechoice == "d"):
                print("You dodge out of the way and take no damage!")
            if enemychoice == 7:
                print("The enemy looks on, but does not act.")
            if weaponchoice == 3 and attackroll > 20 and attackroll < 221:
                playerhealth = playerhealth + (attackroll - 20)
                print("The Cracked Wand glows, absorbing some health from the opponent")
            if playerhealth <= 0:
                print("You're out of health!\nGAME OVER")
                time.sleep(3)
                quit()
            counterwin = 0
            counterfail = 0
            dodgecounter = dodgecounter - 1
            if enemyhealth <= 0:
                if playerhealth >= 500:
                    print("You won, with nary a scratch on you!\n")
                if playerhealth < 500 and playerhealth >= 200:
                    print("After a hard fight, you won!\n")
                if playerhealth < 200 and playerhealth > 50:
                    print("It was difficult, but you came out on top.\n")
                if playerhealth <= 50:
                    print("Your wounds are severe, but you survived.\n")
                battlestate = False
                roomcounter += 1
        time.sleep(3)
    print("\nNearby, something catches your attention:")
    if roomstate % 2 == 0:
        print("You come upon a fellow adventurer.")
        time.sleep(2)
        print("Swap Advice?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            adventurerhintroll = random.randint(1,9)
            print(adventurerhintdictionary[adventurerhintroll])
        else:
            print("They shrug.")
            time.sleep(1)
            print("\"To each their own, pal.\"")
            spurnnedcounter += 1
    if roomstate % 2 == 1:
        chestchoice = random.randint(1,6)
        chesthealvalue = int(chestindex[chestchoice]["heal"])
        time.sleep(2)
        print(chestindex[chestchoice]["desc"])
        time.sleep(2)
        print("Will you open it?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            if chestchoice == 5:
                for i in range(6 + spurnnedcounter - faith):
                    print(chestindex[chestchoice]["prize"])
                    time.sleep(2)
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(3)
            else:
                print(chestindex[chestchoice]["prize"])
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(3)
                if playerhealth <= 0:
                    print("You're out of health!\nGAME OVER")
                    time.sleep(3)
                    quit()
        else:
            print("You decide to leave it alone.")
            time.sleep(2)
    if roomstate == 1 or roomstate == 2:
        print("There's an old altar in the back of the room.")
        time.sleep(2)
        print("Rest?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            print("You rest for a while, and no monsters appear")
            if playerhealth < 50:
                faith += 3
            if playerhealth < 300:
                faith += 2
            else:
                faith += 1
    print("You move to room " + str(roomcounter + 1))

time.sleep(2)
print("You cleared the 2nd floor!\nYou venture deeper into Com-Pyu Tar...\n")
time.sleep(3)


## Floor Event 2

print("You enter into a large room.")
time.sleep(2)
print("In the center is a witch, consulting a glowing rectangular object.")
time.sleep(4)
print("\"Oh, hey. sry, just a sec.\"")
time.sleep(8)
print("\"Cool, alright. I'm good now.\"")
time.sleep(2)
if weaponchoice == 1:
    print("\"WELCOME, WARRIOR")
if weaponchoice == 2:
    print("\"WELCOME, ADVENTURER")
if weaponchoice == 3:
    print("\"WELCOME, MAGICIAN")
time.sleep(3)
print("\"I AM THE WITCH, FOLLOWER OF THE GREAT ALGO RHYTHM -")
time.sleep(6)
print("THE VERY HEARTBEAT OF THIS ACCURSED LAND")
time.sleep(4)
print("...I see you seek to slay the Python of Com-Pyu Tar.")
time.sleep(4)
print("An honorable task;\nPerhaps one day you shall duel the Monsters of the Sea Sharp")
time.sleep(6)
print("Or face off against The Machine.")
time.sleep(5)
print("But I shall not delay you any longer.\nSpeak or BEGONE!\"\n")
time.sleep(4)
print("What do you say?")
witchresponse = input()
witchresponse = witchresponse.lower()
a = witchresponse.find("int") + witchresponse.find("smart") + witchresponse.find("intelligent") + witchresponse.find("clever")
if a > 0:
    print("\"Oh shit thank you")
    time.sleep(2)
    print("ive actually been working on my INT, ty for noticing")
    time.sleep(4)
    print("Damn, now I don't want you to die.")
    time.sleep(3)
    print("Here's a tip: The more faith you have, the more damage you can do.")
    time.sleep(4)
    print("But the Python is kinda overwhelming, especially its power attacks:")
    time.sleep(4)
    print("The Pylance and Rainbow Breath.\nDon't get hit by that.\"")
else:
    print("They ignore you, looking back at their phone.\n")
 
time.sleep(4)
print("You move on.")


## Floor 3

floorcounter = 3
roomcounter = 10

battlestate = False
enemyturn = False
playerturn = True
counterfail = 0
counterwin = 0
dodgecounter = 0

while roomcounter >= 10 and roomcounter <= 15:
    roomstate = floor3rooms()
    opponent = random.randint(7, 9)
    print("As you stalk the dungeon,\nyou notice something:\n")
    time.sleep(2)
    print(enemytype[opponent]["hint"])
    time.sleep(10)
    print("Suddenly, you're attacked!")
    time.sleep(3)
    print("You begin to battle a " + enemytype[opponent]["name"])
    enemyhealth = enemytype[opponent]["hp"]
    enemyattack = enemytype[opponent]["atk"]
    time.sleep(1)
    battlestate = True
    while battlestate == True:
        while playerturn == True:
            print("\nPlayer turn")
            print("HP: " + str(playerhealth))
            print(enemytype[opponent]["name"] + ": " + str(enemyhealth))
            time.sleep(3)
            attackroll = (weaponattack * multiplier())
            enemychoice = enemydecision()
            print(enemytype[opponent][enemychoice])
            time.sleep(2)
            print("What will you do? \n[A]ttack, [C]ounter, [D]odge")
            try:
                battlechoice = input()
            except:
                continue
            battlechoice = battlechoice.lower()
            if battlechoice == "a":
                enemyhealth = enemyhealth - attackroll
                print("You do " + str(attackroll) + " damage!")
            if battlechoice == "c" and enemychoice >= 1 and enemychoice <= 2:
                enemyhealth = enemyhealth - (attackroll * 4)
                print("You counter the attack and do " + str(attackroll * 4) + " damage!")
                counterwin = 1
            if battlechoice == "c" and enemychoice > 2:
                enemyhealth = enemyhealth - (attackroll / 2)
                counterfail = 1
                print("You try to counter the attack and do " + str(attackroll) + " damage!")
                print("But you miss-timed the counterattack!")
            if battlechoice == "d":
                dodgecounter += random.randint(0,3)
                print("You wait for an attack...")
            enemyturn = True
            playerturn = False
            time.sleep(3)
        while enemyturn == True:
            print("\nEnemy turn")
            enemyturn = False
            playerturn = True
            if dodgecounter > enemytype[opponent]["int"] and battlechoice == "d" and random.randint(0,2) % 2 == 0:
                enemychoice = 0
                playerhealth = playerhealth - (enemyattack * 3)
                print("Enemy saw through your evasion! You lose " + str(enemyattack * 3) + " health.")
            if enemychoice >= 1 and enemychoice <= 2 and battlechoice == "a":
                playerhealth = playerhealth - (enemyattack * 3)
                print("The enemy strikes powerfully!")
                print("You lose " + str(enemyattack * 3) + " health.")
            if enemychoice >= 1 and enemychoice <= 2 and counterwin == 1:
                print("The enemy's strong attack is stopped in its tracks!")
            if enemychoice >= 1 and enemychoice <= 2 and battlechoice == "d":
                print("The enemy strikes powerfully!")
                print("But you roll out of the way!")
            if enemychoice >= 3 and enemychoice <= 8 and battlechoice != "d":
                playerhealth = playerhealth - enemyattack
                print("You take " + str(enemyattack) + " damage.")
            if (enemychoice >= 3 and enemychoice <= 8 and battlechoice == "d"):
                print("You dodge out of the way and take no damage!")
            if enemychoice == 9:
                print("The enemy looks on, but does not act.")
            if weaponchoice == 3 and attackroll > 20 and attackroll < 221:
                playerhealth = playerhealth + (attackroll - 20)
                print("The Cracked Wand glows, absorbing some health from the opponent")
            if playerhealth <= 0:
                print("You're out of health!\nGAME OVER")
                time.sleep(3)
                quit()
            counterwin = 0
            counterfail = 0
            dodgecounter = dodgecounter - 1
            if enemyhealth <= 0:
                if playerhealth >= 500:
                    print("You won, with nary a scratch on you!")
                if playerhealth < 500 and playerhealth >= 200:
                    print("After a hard fight, you won!")
                if playerhealth < 200 and playerhealth > 50:
                    print("It was difficult, but you came out on top.")
                if playerhealth <= 50:
                    print("Your wounds are severe, but you survived.")
                battlestate = False
                roomcounter += 1
        time.sleep(4)
    print("\nNearby, something catches your attention:")
    if roomstate % 2 == 0:
        print("You come upon a fellow adventurer.")
        time.sleep(3)
        print("Swap Advice?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            adventurerhintroll = random.randint(1,9)
            print(adventurerhintdictionary[adventurerhintroll])
        else:
            print("They shrug.")
            time.sleep(1)
            print("\"To each their own, pal.\"")
            spurnnedcounter += 1
    if roomstate % 2 == 1:
        chestchoice = random.randint(1,6)
        chesthealvalue = int(chestindex[chestchoice]["heal"])
        time.sleep(2)
        print(chestindex[chestchoice]["desc"])
        time.sleep(2)
        print("Will you open it?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            if chestchoice == 5:
                for i in range(6 + spurnnedcounter - faith):
                    print(chestindex[chestchoice]["prize"])
                    time.sleep(2)
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(3)
            else:
                print(chestindex[chestchoice]["prize"])
                playerhealth = playerhealth + chesthealvalue
                print(chestindex[chestchoice]["after"])
                time.sleep(3)
                if playerhealth <= 0:
                    print("You're out of health!\nGAME OVER")
                    time.sleep(3)
                    quit()
        else:
            print("You decide to leave it alone.")
            time.sleep(2)
    if roomstate == 1 or roomstate == 2:
        print("There's an old altar in the back of the room.")
        time.sleep(2)
        print("Rest?\n[Y] or [N]")
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            print("You rest for a while, and no monsters appear")
            if playerhealth < 50:
                faith += 3
            if playerhealth < 300:
                faith += 2
            else:
                faith += 1
    print("You move to room " + str(roomcounter + 1))
    if roomcounter > 15: ## Floor Event 3
        print("In the final room, standing in front of the staircase down, is the Witch.")
        time.sleep(3)
        print("\"You made it. Well done.")
        time.sleep(2)
        print("Let's see... You have " + str(playerhealth) + " health.")
        time.sleep(2)
        if faith > 10:
            print("And you must be well loved by the gods, to have such strength!")
        if playerhealth > 1000:
            print("And a wit, sharper than steel")
        else:
            print("And you must have a will of iron, to make it this far.")
        time.sleep(3)
        print("Tell me, do you feel ready? Answer boldly now.\"\n")
        time.sleep(3)
        print("How do you respond?\n[Y] or [N]")
        time.sleep(1)
        ynresponse = input()
        ynresponse = ynresponse.lower()
        if ynresponse == "y":
            print("\"Good. And good luck.\"")
            time.sleep(1)
            print("The Witch steps aside.")
            if a > 0:
                print("\"Kick its ass!\"")
        elif ynresponse != "y":
            print("\"There's no shame in that.")
            time.sleep(1)
            print("Bolster your strength a while yet, warrior.\"")
            time.sleep(2)
            print("With a wave of their wand, everything goes dark.")
            time.sleep(2)
            print("You awaken in Room 10.")
            time.sleep(3)
            roomcounter = 10
        

time.sleep(2)
print("You cleared the 3rd floor!\nYou venture into the unknown depths of Com-Pyu Tar...\n")
time.sleep(4)
print("In the deepest part of the dungeon is an enormous arena.")
time.sleep(3)
print("Lit by a thousand magical flames, the Python of Com-Pyu Tar looms.")
time.sleep(3)
print("\"Prepare, invader! For a duel, and your demise!\"")
time.sleep(2)
print("You begin to battle The Python!\n")

## Final Boss

floorcounter = "boss"
enemyturn = False
playerturn = True
battlestate = True
bossbattle = True

counterfail = 0
counterwin = 0
dodgecounter = 0

while bossbattle == True:
    enemyhealth = bossstats["hp"]
    enemyattack = bossstats["atk"]
    time.sleep(2)
    battlestate = True
    while battlestate == True:
        while playerturn == True:
            print("\nPlayer turn")
            print("HP: " + str(playerhealth))
            print(bossstats["name"] + ": " + str(enemyhealth))
            time.sleep(3)
            attackroll = (weaponattack * multiplier())
            enemychoice = enemydecision()
            print(bossstats[enemychoice])
            time.sleep(2)
            print("What will you do? \n[A]ttack, [C]ounter, [D]odge")
            try:
                battlechoice = input()
            except:
                continue
            battlechoice = battlechoice.lower()
            if battlechoice == "a":
                enemyhealth = enemyhealth - attackroll
                print("You do " + str(attackroll) + " damage!")
            if battlechoice == "c" and enemychoice >= 1 and enemychoice <= 2:
                enemyhealth = enemyhealth - (attackroll * 4)
                print("You counter the attack and do " + str(attackroll * 4) + " damage!")
                counterwin = 1
            if battlechoice == "c" and enemychoice > 2:
                enemyhealth = enemyhealth - attackroll
                print("You try to counter the attack and do " + str(attackroll) + " damage!")
                print("But you miss-timed the counterattack!")
            if battlechoice == "d":
                dodgecounter += random.randint(1,3)
                print("You wait for an attack...")
            enemyturn = True
            playerturn = False
            time.sleep(3)
        while enemyturn == True:
            print("\nEnemy turn")
            enemyturn = False
            playerturn = True
            if dodgecounter > bossstats["int"] and battlechoice == "d" and random.randint(0,2) % 2 == 0:
                enemychoice = 0
                enemyhealth = enemyhealth - (enemyattack * 2)
                print("Enemy is upset they can't hit you! Enemy begins to thrash wildly!")
                print("Enemy loses " + str(enemyattack * 2) + " health.")
                print("Seeing their power, you begin doubt yourself!\nFaith reduced!")
                if faith > 1:
                    faith -= 1
                if faith == 1:
                    print("But you have no faith left!\nThe gods punish you!")
                    playerhealth -= 100
                    print("You lose 100 HP")
            if enemychoice >= 1 and enemychoice<= 2 and battlechoice == "a":
                playerhealth = playerhealth - (enemyattack * 3)
                print("The Enemy's strike is devastating!")
                print("You lose " + str(enemyattack * 3) + " health.")
                time.sleep(1)
                print("You lose faith in yourself!")
                if faith > 1:
                    faith -= 1
                if faith == 1:
                    print("But you have no faith left!\nThe gods punish you!")
                    playerhealth -= 100
                    print("You lose 100 HP")
            if enemychoice >= 1 and enemychoice <= 2 and counterwin == 1:
                print("The enemy's devestating attack is stopped in its tracks!")
                time.sleep(1)
                print("Perhaps you stand a chance!")
                faith += 1
            if enemychoice >= 1 and enemychoice <= 2 and battlechoice == "d":
                print("The Enemy's attack shakes the earth!")
                print("But you leap out of the way!")
            if enemychoice >= 2 and enemychoice <= 3 and battlechoice != "d":
                playerhealth = playerhealth - enemyattack
                print("You take " + str(enemyattack) + " damage.")
            if enemychoice >= 2 and enemychoice <= 3 and battlechoice == "d":
                print("You dodge out of the way and take no damage!")
            if enemychoice == 5 or enemychoice == 6:
                print("The enemy looks on, but does not act.")
            if weaponchoice == 3 and attackroll > 20 and attackroll < 821:
                playerhealth += (attackroll - 20)
                print("The Cracked Wand glows, absorbing some health from the Python")
            if playerhealth <= 0:
                print("You're out of health!\nGAME OVER")
                time.sleep(3)
                quit()
            counterwin = 0
            counterfail = 0
            dodgecounter = dodgecounter - 1
            if enemyhealth <= 0:
                battlestate = False
                bossbattle = False
        time.sleep(3)

print("\n\"NO! I HAVE BEEN BESTED-")
time.sleep(4)
print("BY A FOOL SUCH AS YOU!\"")
time.sleep(7)
print("With that final word,\nThe Python collapses, defeated.")
if playerhealth <= 500:
    print("And you remain,\nbruised, battered, yet not beaten.")
if playerhealth >= 500 and playerhealth <=999:
    print("And you remain,\nstronger from your ordeal.")
if playerhealth > 999:
    print("And you stand above, the paragon of a warrior.")
if faith > 5:
    print("Fortune smiles upon you.")
if spurnnedcounter > 5:
    print("Though, you aren't very popular\nwith your fellow adventurers.")
print("As you emerge from Com-Pyu Tar,\na new adventure seems ready to unfold.")
time.sleep(20)
print("THE END")
time.sleep(5)
quit()