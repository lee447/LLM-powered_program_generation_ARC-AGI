def solve(grid):
    result = []
    for row in grid:
        left_part = row[:4]
        right_part = row[5:]
        right_part = [x for x in right_part if x != 0]
        result.append(left_part[:1] + right_part + left_part[1:4-len(right_part)])
    return result