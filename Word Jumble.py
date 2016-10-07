import random


# a function that rearranges the chosen word into a random list
def word_scramble(jumble):
    for current_index in range(len(jumble)):
        random_index = random.randrange(0, len(jumble))
        temp = jumble[current_index]
        jumble[current_index] = jumble[random_index]
        jumble[random_index] = temp
    return jumble

colors = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET", "PINK", "BLACK", "WHITE", "BROWN", "GRAY", "PURPLE", "GOLD", "SILVER"]
# selects one random string from the list and sets it as the answer
selection = random.choice(colors)
answer = selection

chosen = list(selection)
# scrambles the chosen word and prints out the results
for letter in word_scramble(chosen):
    print letter,

guess = " "
count = 0
# A while loop that will constantly ask the user to input a guess until the guess matches the answer
while guess != answer:
    guess = raw_input("\nGuess the word: ")
    guess = guess.upper()
    if guess == answer:
        print ("You got it!")
    else:
        print("Wrong, try again")
        count += 1
        if count == 5:
            print ("I'll give you a hint. " "It starts with " + answer[0])
