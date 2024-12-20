word = "ayam babi kambing harimau kelinci kucing kuda monyet sapi tikus ular sapi naga"
import random

word_list = word.split()
word = random.choice(word_list)
word = word.lower()
word = word.replace(" ", "")
word = list(word)
correct_guesses = ["_"] * len(word)
while "_" in correct_guesses:
    print(" ".join(correct_guesses))
    guess = input("Tebak nama hewan perhuruf: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                correct_guesses[i] = guess
    else:
        print("Salah, coba lagi")

if "_" not in correct_guesses:
    print("Kamu menang!")
else:
    print("Kamu kalah!")


