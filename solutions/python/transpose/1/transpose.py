def transpose(lines):
    if not lines:
        return ""
    
    rows = lines.split('\n') if isinstance(lines, str) else lines
    
    max_len = max(len(row) for row in rows)
    result = []
    
    for i in range(max_len):
        column = []
        for r, row in enumerate(rows):
            if i < len(row):
                column.append(row[i])
            else:
                if any(len(rows[next_r]) > i for next_r in range(r + 1, len(rows))):
                    column.append(" ")
        
        result.append("".join(column))
        
    return "\n".join(result)