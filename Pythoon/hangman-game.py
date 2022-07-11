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
        for line in f:
            if (string_check.search(line) == None):
                words.append(line.strip())
            else:
                continue

def random_word():
    word = random.choice(words)
    print(word)


def run():
    clear()
    try:
        start = int(input("Bienvenido a el Ahorcado\nEscribe 1 para iniciar \n"))
        if start ==1 :
            words_ext()
            random_word()
        else:
            raise ValueError
    except ValueError:
        print("Solo puedes poner el numero de la opción")
    


if __name__ == "__main__":
    run()
