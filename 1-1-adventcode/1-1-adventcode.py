# Advent Code 2019
# Day 1, step 1
import math


def main():
    valuesInput = []
    valuesFuel = []
    totalFuel = 0
    f = open("1.1-input", "r")
    for x in f:
        x = x.rstrip('\n')
        valuesInput.append(x)

    f.close()

    valuesInput = list(map(int, valuesInput))

    for x in valuesInput:
        valuesFuel.append((math.floor(x / 3)) - 2)

    for x in valuesFuel:
        totalFuel = totalFuel + x

    print('Total fuel: ' + str(totalFuel))


if __name__ == "__main__":
    main()
