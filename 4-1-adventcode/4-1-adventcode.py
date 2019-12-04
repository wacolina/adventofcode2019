# Advent Code 2019
# Day 4, step 1


def main():
    results = []
    startingPoint = 245182
    endPoint = 790572

    while startingPoint < endPoint:
        valuesInput = list(map(int, str(startingPoint)))

        i = 0
        while i < len(valuesInput):
            if valuesInput[i] > valuesInput[i+1]:
                break

            i += 1

            if i == 5:
                j = 0
                sameDigits = 0

                while j < len(valuesInput):
                    if valuesInput[j] == valuesInput[j + 1]:
                        sameDigits += 1

                    j += 1

                    if j == 5:
                        if sameDigits == 0:
                            break
                        results.append(''.join(map(str, valuesInput)))
                        break
                break

        startingPoint += 1
    print('Good numbers: ' + str(len(results)))


if __name__ == "__main__":
    main()
