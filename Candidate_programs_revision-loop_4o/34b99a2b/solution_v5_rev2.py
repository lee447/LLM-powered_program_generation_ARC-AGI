def solve(grid):
    def extract_subgrid(grid):
        subgrid = []
        for row in grid:
            new_row = []
            for val in row:
                if val == 8:
                    new_row.append(2)
                elif val == 4:
                    break
                else:
                    new_row.append(0)
            subgrid.append(new_row)
        return subgrid

    def trim_subgrid(subgrid):
        max_length = max(len(row) for row in subgrid)
        trimmed_subgrid = []
        for row in subgrid:
            trimmed_row = row[:max_length]
            trimmed_subgrid.append(trimmed_row)
        return trimmed_subgrid

    subgrid = extract_subgrid(grid)
    max_length = max(len(row) for row in subgrid)
    trimmed_subgrid = [row[:max_length] for row in subgrid]
    
    # Adjust the length of each row to match the longest row
    for i in range(len(trimmed_subgrid)):
        trimmed_subgrid[i] = trimmed_subgrid[i] + [0] * (max_length - len(trimmed_subgrid[i]))
    
    return trimmed_subgrid