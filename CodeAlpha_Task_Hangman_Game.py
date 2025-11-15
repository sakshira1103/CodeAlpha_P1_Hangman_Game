import random
words=["orange", "apple", "grapes", "banana" ,"pineapple"]

word=random.choice(words)
space=["_"]*len(word)
chances=5

print("Welcome to Hangman game!")
print(f"You  have {chances} chances")
print(" ".join(space))

while "_" in space and chances>0:
    guess=input("Guess a letter:").lower()
    if guess in space:
        print("Already entered letter.")
        continue
    if guess in word:
        for letter in range(len(word)):
            if word[letter]==guess:
                space[letter]=guess
        print("correct guess")
    else:
        chances-=1
        print("Wrong guess,you lost one chance.")
    print(" ".join(space))
    print(f"chances left:{chances}")

if "_" not in space:
    print("Congratulation!,you guess correct word.")
else:
    print(f"Game over!,The word is {word}.")
    

   