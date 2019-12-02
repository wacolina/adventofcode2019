# Advent Code 2019
# Day 2, step 2
import re


def inputValues():
    valuesInput = []

    for x in open("2.2-input", "r"):
        valuesInput = list(map(int, re.split(',', x)))

    return valuesInput


def checkValues(valuesInput, x, y):
    counter = 0

    valuesInput[1] = x
    valuesInput[2] = y

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

    if (valuesInput[0] == 19690720):
        return [valuesInput[1], valuesInput[2]]
    else:
        return []


def main():
    correctValues = []

    for x in range(0, 100):
        for y in range(0, 100):
            valuesInput = inputValues()
            correctValues = checkValues(valuesInput, x, y)

            if len(correctValues) > 0:
                print('Noun: ' + str(correctValues[0]) + '. Verb: ' + str(correctValues[1]))
                break

        if len(correctValues) > 0:
            break


if __name__ == "__main__":
    main()