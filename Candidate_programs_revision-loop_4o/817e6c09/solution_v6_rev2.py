def solve(grid):
    def replace_last_pair(row):
        last_pair_start = -1
        for i in range(len(row) - 1, 0, -1):
            if row[i] == 2 and row[i - 1] == 2:
                last_pair_start = i - 1
                break
        if last_pair_start != -1:
            row[last_pair_start] = 8
            row[last_pair_start + 1] = 8
        return row

    return [replace_last_pair(row) for row in grid]