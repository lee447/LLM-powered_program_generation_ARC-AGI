def solve(grid):
    result = []
    for row in grid:
        new_row = []
        for i in range(len(row)):
            if row[i] == 5:
                new_row.extend(reversed(row[i+1:]))
                break
            new_row.append(row[i])
        result.append(new_row)
    return result