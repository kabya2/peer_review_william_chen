import random
import matplotlib.pyplot as plt

# Function to roll three dice
def roll_dice():
    """Roll three dice and return the result as a list."""
    return [random.randint(1, 6) for _ in range(3)]

# Function to display the game history as a graph
def graph_history(player1_scores, player2_scores):
    """
    Plot the scores of Player 1 and Player 2 over time.
    """
    plt.plot(player1_scores, label="Player 1")
    plt.plot(player2_scores, label="Player 2")
    plt.xlabel("Rounds")
    plt.ylabel("Score")
    plt.title("Game Score History")
    plt.legend()
    plt.show()

# Function to play a single round for a player
def play_turn(player_name):
    """
    Handles a player's turn:
    - Rolls dice
    - Allows rerolling under specific rules
    - Returns the points scored in the round
    """
    print(f"\n{player_name}'s turn:")
    dice = roll_dice()
    print(f"Initial roll: {dice}")

    # Reroll Logic: Check for duplicates and decide which dice can be rerolled
    while True:
        reroll_input = input("Enter positions to reroll (e.g., 1 3) or 'done' to finish: ").lower()
        if reroll_input == 'done':
            break
        try:
            # Validate input for reroll positions
            reroll_positions = [int(pos) - 1 for pos in reroll_input.split()]
            for pos in reroll_positions:
                if 0 <= pos < 3:  # Validating positions between 0 and 2
                    dice[pos] = random.randint(1, 6)
                else:
                    print("Invalid position. Please choose between 1 and 3.")
            print(f"Rerolled dice: {dice}")
        except ValueError:
            print("Invalid input. Enter numbers corresponding to dice positions (e.g., 1 2).")

    # Check for 'tuple out' condition where all dice match
    if dice[0] == dice[1] == dice[2]:
        print("Tuple out! No points this round.")
        return 0  # No points scored this round
    
    # Sum of the dice as the points scored
    points = sum(dice)
    print(f"Points scored this round: {points}")
    return points

# Main Game Function
def main():
    """
    Main function to run the dice game:
    - Supports Player vs Player or Player vs AI
    - Tracks scores and game history
    - Declares a winner
    """
    print("Welcome to the Dice Game! First to 100 points wins.")
    mode = input("Choose mode: '1v1' or '1vAI': ").lower()

    # Validate game mode input
    if mode not in ['1v1', '1vai']:
        print("Invalid mode. Please restart and choose '1v1' or '1vAI'.")
        return

    # Initialize scores and history
    player1_score, player2_score = 0, 0
    player1_history, player2_history = [], []

    while player1_score < 100 and player2_score < 100:
        # Player 1's turn
        player1_score += play_turn("Player 1")
        player1_history.append(player1_score)

        # Player 2's turn
        if mode == '1v1':
            player2_score += play_turn("Player 2")
        else:
            # AI Logic: Randomly decide to reroll or keep dice
            print("\nAI's turn:")
            dice = roll_dice()
            print(f"AI rolls: {dice}")
            if len(set(dice)) == 3:  # AI keeps all unique rolls
                print("AI keeps the dice.")
            else:
                print("AI rerolls the dice for better results.")
                dice = [random.randint(1, 6) for _ in range(3)]
            if dice[0] == dice[1] == dice[2]:
                print("AI tuple out! No points this round.")
                points = 0
            else:
                points = sum(dice)
                print(f"AI scores {points} points.")
            player2_score += points
        player2_history.append(player2_score)

        # Display current scores
        print(f"\nCurrent Scores:\nPlayer 1: {player1_score} | Player 2: {player2_score}")

    # Determine winner
    if player1_score >= 100 and player2_score >= 100:
        print("\nBoth players reached 100 points. Determining winner by highest score...")
    winner = "Player 1" if player1_score > player2_score else "Player 2"
    print(f"\n{winner} wins!")

    # Display game history graph
    graph_history(player1_history, player2_history)

if __name__ == "__main__":
    main()
