# Advent Code 2019
# Day 1, step 2
import math


def main():
    valuesInput = []
    totalFuel = 0
    for x in open("1.2-input", "r"):
        valuesInput.append(x.rstrip('\n'))

    valuesInput = list(map(int, valuesInput))

    for x in valuesInput:
        while x > 0:
            x = (math.floor(x / 3)) - 2
            if x > 0:
                totalFuel = totalFuel + x

    print('Total fuel requirements: ' + str(totalFuel))


if __name__ == "__main__":
    main()
