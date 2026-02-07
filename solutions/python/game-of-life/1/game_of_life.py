def tick(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue 
                    
                    nr, nc = r + i, c + j
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live_neighbors += matrix[nr][nc]

            if matrix[r][c] == 1:
                if live_neighbors in [2, 3]:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
            else:
                if live_neighbors == 3:
                    new_grid[r][c] = 1
                    
    return new_grid