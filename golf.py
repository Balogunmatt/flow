names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]
def golfScore(par, strokes):
    if (strokes == 1):
        return names[0]
    elif (strokes <= par - 2):
        return names[1]
    elif (strokes == par - 1):
        return names[2]
    elif (strokes == par):
        return names[3]
    elif (strokes == par + 1):
        return names[4]
    elif (strokes == par + 2):
        return names[5]
    else:
        return names[6]

wood = golfScore(5, 1)
print(wood)
