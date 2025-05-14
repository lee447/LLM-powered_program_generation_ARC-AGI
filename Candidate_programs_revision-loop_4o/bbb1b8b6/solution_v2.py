def solve(grid):
    result = []
    for row in grid:
        left_part = row[:4]
        right_part = row[5:]
        if 0 in right_part:
            right_part = [x for x in right_part if x != 0]
        result.append(left_part + right_part)
    return result