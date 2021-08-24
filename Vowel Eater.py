# Prompt the user to enter a word
Vowels = ("A", "E", "I", "O", "U")
user_word = input("Write your word:")
user_word = user_word.upper()
# and assign it to the user_word variable.

for letter in user_word:
    if letter not in Vowels:
        print(letter)
    continue
    # Complete the body of the for loop.