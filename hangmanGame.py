import hangman_words
import hangman_art
import random
chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
word_length = len(chosen_word)
display = []
for k in range(word_length):
    display += "_"
result_disp = ' '.join(display)        
print(result_disp)
lives = 6
blanks = display.count('_')
while blanks != 0 and lives != 0:
    guess = input("\nGuess a letter: ").lower()
    if guess in display:
        print(f"\nYou've already chosen '{guess}'")
    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter
            blanks = display.count('_')
        elif guess not in chosen_word:
            print(f"\nYou guessed the letter '{guess}' that is not in the word. You lose a life.")
            lives -= 1
            print(f"You have {lives} lives left!")
            print(hangman_art.stages[lives])
            break
    result_disp = ' '.join(display)
    print("\n")
    print(result_disp)
if lives == 0:
    print(f"\nGame Over.\nYou lose! The right word is: {chosen_word}")
elif blanks == 0:
    print("\nGame Over.\nCongrats! You win.")


