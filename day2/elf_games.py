# Must count max of each color shown in each game, then compare to actual amounts
# Must collect IDs of possible games
# Format:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

import re

with open('day2/input.txt') as input:
    lines = input.read().splitlines()
    possible_games = []
    powers = []
    for line in lines:
        redMax = 0
        greenMax = 0
        blueMax = 0

        currentLine = line.replace('Game ', '')
        # print(currentLine)
        splitLine = currentLine.split(': ')
        # print(splitLine)
        id = int(splitLine[0])
        # print(id)
        currentLine = splitLine[1]
        # print(currentLine)
        redAmounts = re.findall(r'(\d+) red', currentLine)
        for amount in redAmounts:
            if int(amount) > redMax:
                redMax = int(amount)
        greenAmounts = re.findall(r'(\d+) green', currentLine)
        for amount in greenAmounts:
            if int(amount) > greenMax:
                greenMax = int(amount)            
        blueAmounts = re.findall(r'(\d+) blue', currentLine)
        for amount in blueAmounts:
            if int(amount) > blueMax:
                blueMax = int(amount)
        
        if (redMax <= 12 and greenMax <= 13 and blueMax <= 14):
            possible_games.append(id)

        powers.append(redMax*greenMax*blueMax)

    total = 0
    for id in possible_games:
        total += id

    power_total = 0
    for power in powers:
        power_total += power

    print(total)
    print(power_total)
    
    

