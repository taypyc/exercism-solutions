def gamestate(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    def check_win(player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    x_wins = check_win('X')
    o_wins = check_win('O')

    if x_wins and o_wins:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    if x_wins and x_count == o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")
        
    if o_wins and x_count > o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_wins or o_wins:
        return "win"
    
    if x_count + o_count == 9:
        return "draw"
        
    return "ongoing"