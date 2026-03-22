def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    row_maxima = [max(row) for row in matrix]
    col_minima = [min(col) for col in zip(*matrix)]

    results = []
    for r, row in enumerate(matrix):
        for c, tree_height in enumerate(row):
            if tree_height == row_maxima[r] and tree_height == col_minima[c]:
                results.append({"row": r + 1, "column": c + 1})

    return results