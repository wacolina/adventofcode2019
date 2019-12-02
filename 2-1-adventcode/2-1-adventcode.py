# Advent Code 2019
# Day 2, step 1
import re


def main():
    valuesInput = []
    counter = 0
    for x in open("2.1-input", "r"):
        valuesInput = list(map(int, re.split(',', x)))

    print(valuesInput)

    for key, value in enumerate(valuesInput):
        if counter != 3:
            counter += 1
            continue

        operation = valuesInput[key - counter]
        if operation == 1:
            valuesInput[value] = valuesInput[valuesInput[key - 1]] + valuesInput[valuesInput[key - 2]]
        elif operation == 2:
            valuesInput[value] = valuesInput[valuesInput[key - 1]] * valuesInput[valuesInput[key - 2]]
        elif operation == 99:
            break
        else:
            print('wrong')

        counter = 0

    print(valuesInput)


if __name__ == "__main__":
    main()