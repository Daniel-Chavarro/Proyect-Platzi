from operator import truediv
import os as os
import random
import re
import time

string_check = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
validate = []


def clear(): return os.system("cls")


def dataImport(filepath="./txt/words.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if (string_check.search(line) == None):
                words.append(line.strip().upper())
    return words


def run():
    liveCounter = 3

    clear()
    data: list = dataImport(filepath="./txt/words.txt")
    print("Importacion Exitosa")
    time.sleep(1)
    clear()
    chosenWord = random.choice(data)
    chosenWordList = [letter for letter in chosenWord]
    wordScreen = ["_"] * len(chosenWordList)
    chosenWordDict = {}

    for idx, letterword in enumerate(chosenWord):
        if not chosenWordDict.get(letterword):
            chosenWordDict[letterword] = []

        chosenWordDict[letterword].append(idx)

    # Ciclo true
    while True:
        clear()
        print("Adivina la palabra!")
        for element in wordScreen:
            print(element + " ", end="")

        print("\n")
        userInput = str(input("Ingresa la letra \n")).strip().upper()
        assert userInput.isalpha(), "Solo puedes poner letras"

        if userInput in chosenWordList:
            for idx in chosenWordDict[userInput]:
                wordScreen[idx] = userInput
        else:
            liveCounter = liveCounter - 1
            print("No hay letra en la palabra")
            time.sleep(1.5)

        if "_" not in wordScreen:
            print("Ganaste, la palabra era: " + chosenWord)
            break

        if liveCounter == 0:
            print("Perdiste, la palabra era: " + chosenWord)
            time.sleep(3)
            break


if __name__ == "__main__":
    run()
