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
    trimmed_subgrid = trim_subgrid(subgrid)
    return trimmed_subgrid