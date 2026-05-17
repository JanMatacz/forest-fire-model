import random
import matplotlib.pyplot as plt
import matplotlib.colors

FOREST_PROBABILITY = 0.1


def create_forest(width, height, forestCoverage):
    forestMap = [[2] * width for _ in range(height)]

    while True:
        forest_strike(forestMap, 0.5)
        spread_forest(forestMap)
        coveredArea = sum(cell == 0 for row in forestMap for cell in row)
        if forestCoverage <= coveredArea / (width * height):
            break

    return forestMap

def forest_strike(forest_map, probability):
    if random.random() < probability:
        row = random.randint(0, len(forest_map) - 1)
        col = random.randint(0, len(forest_map[0]) - 1)
        if forest_map[row][col] == 2:
            forest_map[row][col] = 0

def spread_forest(forest_map):
    for x in range(len(forest_map)):
        for y in range(len(forest_map[0])):
            if forest_map[x][y] == 0:
                if y != 0:
                    if forest_map[x][y - 1] == 2:
                        if random.random() < FOREST_PROBABILITY:
                            forest_map[x][y - 1] = 0
                if y != len(forest_map[0]) - 1:
                    if forest_map[x][y + 1] == 2:
                        if random.random() < FOREST_PROBABILITY:
                            forest_map[x][y + 1] = 0
                if x != 0:
                    if forest_map[x - 1][y] == 2:
                        if random.random() < FOREST_PROBABILITY:
                            forest_map[x - 1][y] = 0
                if x != len(forest_map) - 1:
                    if forest_map[x + 1][y] == 2:
                        if random.random() < FOREST_PROBABILITY:
                            forest_map[x + 1][y] = 0


if __name__ == "__main__":
    startingForest = create_forest(100, 100, 0.8)
    forest_cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "", ["green", "red", "saddlebrown"]
    )
    fig, ax = plt.subplots()
    img = ax.imshow(startingForest, cmap=forest_cmap, vmin=0, vmax=2)
    plt.colorbar(img, ax=ax)
    plt.show()
    
