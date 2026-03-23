DIGITS = {
    " _ \n| |\n|_|\n   ": "0",
    "   \n  |\n  |\n   ": "1",
    " _ \n _|\n|_ \n   ": "2",
    " _ \n _|\n _|\n   ": "3",
    "   \n|_|\n  |\n   ": "4",
    " _ \n|_ \n _|\n   ": "5",
    " _ \n|_ \n|_|\n   ": "6",
    " _ \n  |\n  |\n   ": "7",
    " _ \n|_|\n|_|\n   ": "8",
    " _ \n|_|\n _|\n   ": "9",
}

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(line) % 3 != 0 for line in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    output_rows = []
    
    for row_start in range(0, len(input_grid), 4):
        current_row_lines = input_grid[row_start : row_start + 4]
        row_digits = ""
        
        number_of_cells = len(current_row_lines[0]) // 3
        for i in range(number_of_cells):
            cell_lines = [line[i*3 : (i+1)*3] for line in current_row_lines]
            cell_string = "\n".join(cell_lines)
            
            row_digits += DIGITS.get(cell_string, "?")
            
        output_rows.append(row_digits)

    return ",".join(output_rows)