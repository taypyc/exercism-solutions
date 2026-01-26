def rectangles(strings):
    if not strings:
        return 0
        
    rows = len(strings)
    cols = len(strings[0])
    count = 0
    
    corners = [(r, c) for r in range(rows) for c in range(cols) if strings[r][c] == '+']
    
    for i, (r1, c1) in enumerate(corners):
        for (r2, c2) in corners[i+1:]:
            if r2 > r1 and c2 > c1:
                if strings[r1][c2] == '+' and strings[r2][c1] == '+':
                    if is_rectangle(strings, r1, r2, c1, c2):
                        count += 1
    return count

def is_rectangle(grid, r1, r2, c1, c2):
    for c in range(c1 + 1, c2):
        if grid[r1][c] not in '+-' or grid[r2][c] not in '+-':
            return False
    for r in range(r1 + 1, r2):
        if grid[r][c1] not in '+|' or grid[r][c2] not in '+|':
            return False
    return True