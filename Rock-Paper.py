import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the choices and the result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    """Main function to play the game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.\n")

    while True:
        # Get user input
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower().strip()
        if user_choice == 'exit':
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine winner
        winner = determine_winner(user_choice, computer_choice)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display the result
        display_result(user_choice, computer_choice, winner)

        # Show current scores
        print(f"\nCurrent Scores:\nYou: {user_score} | Computer: {computer_score}\n")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again != 'yes':
            break

    # Final scores
    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()

        
        
