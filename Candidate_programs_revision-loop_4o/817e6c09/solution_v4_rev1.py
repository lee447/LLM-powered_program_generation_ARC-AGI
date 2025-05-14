def solve(grid):
    def replace_first_pair(row):
        first_pair_start = -1
        for i in range(len(row) - 1):
            if row[i] == 8 and row[i + 1] == 8:
                first_pair_start = i
                break
        if first_pair_start != -1:
            row[first_pair_start] = 2
            row[first_pair_start + 1] = 2
        return row

    return [replace_first_pair(row) for row in grid]