import tkinter as tk
import random

# Predefined list of words
WORD_LIST = ['python', 'hangman', 'challenge', 'programming', 'developer','charan','ravinteja']

# Function to select a random word
def select_word():
    return random.choice(WORD_LIST)

# Hangman Game Class for GUI
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Challenge")

        # Initialize game variables
        self.word_to_guess = select_word()
        self.guessed_letters = []
        self.incorrect_guesses = []
        self.attempts_left = 6

        # Set up GUI components
        self.word_label = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 18))
        self.word_label.pack(pady=20)

        self.status_label = tk.Label(root, text=f"Remaining Attempts: {self.attempts_left}", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        self.input_entry = tk.Entry(root, font=("Helvetica", 14))
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Guess", command=self.process_guess)
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
        self.message_label.pack(pady=10)

    # Get the display word with blanks and guessed letters
    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess])

    # Process the guessed letter
    def process_guess(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Invalid input. Enter a single letter.")
            return

        if guess in self.guessed_letters or guess in self.incorrect_guesses:
            self.message_label.config(text="You've already guessed that letter.")
            return

        # Check if the guess is correct
        if guess in self.word_to_guess:
            self.guessed_letters.append(guess)
            if all(letter in self.guessed_letters for letter in self.word_to_guess):
                self.word_label.config(text=self.get_display_word())
                self.message_label.config(text=f"Congratulations! You've guessed the word: {self.word_to_guess}")
                self.end_game()
        else:
            self.incorrect_guesses.append(guess)
            self.attempts_left -= 1
            self.message_label.config(text=f"Incorrect guess. {self.attempts_left} attempts left.")
            if self.attempts_left == 0:
                self.message_label.config(text=f"Game Over! The word was: {self.word_to_guess}")
                self.end_game()

        self.update_display()

    # Update the word and status display
    def update_display(self):
        self.word_label.config(text=self.get_display_word())
        self.status_label.config(text=f"Remaining Attempts: {self.attempts_left}")

    # Disable input after the game ends
    def end_game(self):
        self.input_entry.config(state='disabled')
        self.submit_button.config(state='disabled')

# Run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
