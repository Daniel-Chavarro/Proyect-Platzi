from operator import truediv
import os as os
import random
import re

string_check = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
words = []
word = []


def clear(): return os.system("cls")


def words_ext():
    with open("./txt/words.txt", "r", encoding="utf-8") as f:
        Validation_counter = 0
        for line in f:
            for i in line:
                validation = str.isalnum(i)
                if validation == True:
                    continue
                else:
                    Validation_counter + 1
                    break
            if Validation_counter == 0:
                words.append(line.strip())
            else:
                continue

def random_word():
    word = random.choice(words)
    print(word)


def run():
    clear()
    try:
        start = input(int("Bienvenido a "))
        words_ext()
        random_word()
    except ValueError:
        print("Solo puedes poner el numero de la opción")


if __name__ == "__main__":
    run()
