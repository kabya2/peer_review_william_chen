# peer_review_william_chen
William Chen's code review
### Updates and Fixes to `dice_game_pairProgram.py`

#### 1. **Added Comments and Docstrings**
   - Added clear and descriptive docstrings to all functions for better understanding.
   - Included inline comments to explain key logic in the code, such as:
     - `tuple out` condition where all dice match.
     - Input validation for reroll positions.
     - AI decision-making process for rerolling dice.

#### 2. **Input Validation Improvements**
   - **Reroll Input**: Added checks to validate that input positions for rerolling dice are integers and within the valid range (1-3).
     - Example Code:
       ```python
       try:
           reroll_positions = [int(pos) - 1 for pos in reroll_input.split()]
           for pos in reroll_positions:
               if 0 <= pos < 3:
                   dice[pos] = random.randint(1, 6)
               else:
                   print("Invalid position. Please choose between 1 and 3.")
       except ValueError:
           print("Invalid input. Enter numbers corresponding to dice positions (e.g., 1 2).")
       ```

   - **Game Mode Input**: Ensures the user selects a valid mode (`1v1` or `1vAI`) before starting the game.
     - If an invalid mode is entered, the program terminates gracefully with an error message.

#### 3. **Improved AI Logic Comments**
   - Clarified the AI's decision-making process when rerolling dice:
     - AI keeps all dice if they are unique.
     - AI rerolls otherwise and handles `tuple out` condition like a player.
   - Example Comment:
     ```python
     # AI Logic: If all dice are unique, AI keeps the dice; otherwise, AI rerolls for better results.
     ```

#### 4. **Error Handling Enhancements**
   - Added handling for invalid inputs during gameplay to prevent crashes.
   - Ensures the program provides clear error messages for incorrect user input.

#### 5. **Code Readability Improvements**
   - Improved function naming consistency.
   - Added helper functions, like `display_scores()` to clean up redundant print statements.

---

### Areas for Future Improvement
1. **Dynamic AI Strategy**:
   - Make the AI smarter by implementing a scoring strategy based on the current score standings.
2. **Edge Case Handling**:
   - Consider edge cases such as extremely long or invalid inputs for better robustness.
3. **Code Refactoring**:
   - Break AI logic into a separate function for better modularity and readability.
