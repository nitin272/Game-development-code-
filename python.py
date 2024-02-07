def initialize_board():
  return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
  for row in board:
      print('|'.join(row))
      print('-'*5)

def check_win(board):

  for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != ' ':
          return True
      if board[0][i] == board[1][i] == board[2][i] != ' ':
          return True
  if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
      return True
  return False

def check_draw(board):
  for row in board:
      if ' ' in row:
          return False
  return True

def switch_player(currentPlayer):
  return 'O' if currentPlayer == 'X' else 'X'

def play_game():
  board = initialize_board()
  currentPlayer = 'X'
  while True:
      display_board(board)
      try:
          row = int(input(f"{currentPlayer}'s turn. Choose row (0-2): "))
          col = int(input(f"{currentPlayer}'s turn. Choose column (0-2): "))
      except ValueError:
          print("Please enter a valid number.")
          continue

      if row not in range(3) or col not in range(3):
          print("Invalid input. Please try again.")
          continue

      if board[row][col] == ' ':
          board[row][col] = currentPlayer
          if check_win(board):
              display_board(board)
              print(f"Player {currentPlayer} wins!")
              break
          elif check_draw(board):
              display_board(board)
              print("It's a draw!")
              break
          currentPlayer = switch_player(currentPlayer)
      else:
          print("This cell is already taken. Please try again.")

if __name__ == "__main__":
  play_game()
