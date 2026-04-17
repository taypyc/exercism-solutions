def annotate(minefield):
    if not minefield:
        return []
    
    rows = len(minefield)
    cols = len(minefield[0])
    
    if any(len(row) != cols for row in minefield):
        raise ValueError("The board is invalid with current input.")

    board = [list(row) for row in minefield]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")
            
            if board[r][c] == '*':
                continue

            count = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == '*':
                            count += 1
            
            if count > 0:
                board[r][c] = str(count)

    return ["".join(row) for row in board]