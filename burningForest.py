import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import random
from forestGeneration import create_forest

THUNDER_STRIKE_PROBABILITY = 0.01
TIME_TO_BURN = 0
PROBABILITY_OF_IGNITE = 0.1

def map_visualisation(forest_map):
    forest_cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", ["green", "red", "saddlebrown"]
    )
    img = plt.imshow(forest_map, cmap=forest_cmap, vmin=0, vmax=2)
    return img

def thunder_strike(forest_map, probability):
    if random.random() < probability: #THUNDER_STRIKE_PROBABILITY:
        row = random.randint(0, len(forest_map) - 1)
        col = random.randint(0, len(forest_map[0]) - 1)
        if forest_map[row][col] == 0:
            forest_map[row][col] = 1

def spread_fire(forest_map):
    for x in range(0, len(forest_map)):
        for y in range(0, len(forest_map[0])):
            if forest_map[x][y] == 1:
                if y != 0:
                    if forest_map[x][y - 1] == 0:
                        if random.random() < PROBABILITY_OF_IGNITE:
                            forest_map[x][y - 1] = 1
                if y != len(forest_map) - 1:
                    if forest_map[x][y + 1] == 0:
                        if random.random() < PROBABILITY_OF_IGNITE:
                            forest_map[x][y + 1] = 1
                if x != 0:
                    if forest_map[x - 1][y] == 0:
                        if random.random() < PROBABILITY_OF_IGNITE:
                            forest_map[x - 1][y] = 1
                if x != len(forest_map[0]) - 1:
                    if forest_map[x + 1][y] == 0:
                        if random.random() < PROBABILITY_OF_IGNITE:
                            forest_map[x + 1][y] = 1

def create_timer_map(forest_map):
    timeMap = []
    for x in range(len(forest_map)):
        row = []
        for y in range(len(forest_map[0])):
            if forest_map[x][y] == 0:
                row.append(41)
            elif forest_map[x][y] == 1:
                row.append(40)
            elif forest_map[x][y] == 2:
                row.append(0)
        timeMap.append(row)
    return timeMap
    



def time_change(timeMap, forest_map):
    for x in range(len(forest_map)):
        for y in range(len(forest_map[0])):
            if forest_map[x][y] == 1 and timeMap[x][y] == 41:
                timeMap[x][y] = 40
            if timeMap[x][y] < 41:
                timeMap[x][y] -= 1
                if timeMap[x][y] == 0:
                    forest_map[x][y] = 2




def simulate(width, height, forestCoverage):
    forest = create_forest(width, height, forestCoverage)
    time_events = create_timer_map(forest)
    plt.ion()
    fig, ax = plt.subplots()
    img = map_visualisation(forest)
    thunder_strike(forest, 1)
    while True:
        thunder_strike(forest, THUNDER_STRIKE_PROBABILITY)
        spread_fire(forest)
        img.set_data(forest)
        time_change(time_events, forest)
        plt.pause(0.000001)

if __name__ == "__main__":
    simulate(100, 100, 0.8)
    