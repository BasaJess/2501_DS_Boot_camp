

1. Initialize the game board:
   - Create a 3x3 grid initialized with empty spaces or some placeholder like '-'.

2. Define the player symbols:
   - Player 1 uses 'X'
   - Player 2 uses 'O'

3. Function to display the board:
   - Loop through each row of the grid and print the values with column separators.

4. Function to check if the game board is full:
   - Check every cell in the grid; if any cell is still the placeholder, return False, else return True.

5. Function to check for a win:
   - Check all horizontal, vertical, and diagonal lines:
     - If any line contains the same player symbol across all its cells, return that player has won.
   
6. Function to take a player's move:
   - Input player's move as row and column numbers.
   - Check if the chosen cell is empty:
     - If empty, place the player's symbol in that cell.
     - If not empty, prompt the player to choose another cell.

7. Game loop:
   - Start the game with Player 1.
   - Display the game board.
   - Prompt the current player to enter their move.
   - Update the board based on the player's move.
   - Check for a win or draw:
     - If a player wins, display the winner and end the game.
     - If the board is full and no winner, declare a draw and end the game.
   - Switch turns between Player 1 and Player 2.

8. Repeat the game loop until there is a winner or the board is full (draw).

9. End the game:
   - Print the final state of the game board.
   - Congratulate the winner or declare a draw.
