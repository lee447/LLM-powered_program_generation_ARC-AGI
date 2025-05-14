def solve(grid):
    result = []
    for row in grid:
        new_row = []
        for i in range(len(row)):
            if row[i] == 5:
                break
            new_row.append(row[i])
        new_row.extend(row[i+1:])
        result.append(new_row)
    return result