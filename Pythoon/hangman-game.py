import os as os
import random

words = []
word = []


def clear(): return os.system("cls")


def words_ext():
    with open("./txt/words.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip())
            

def random_word():
    word = random.choice(words)
    print(word)


def run():
    clear()
    words_ext()
    random_word()


if __name__ == "__main__":
    run()
