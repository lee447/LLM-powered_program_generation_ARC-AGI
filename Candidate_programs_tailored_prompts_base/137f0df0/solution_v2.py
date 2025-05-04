from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    grey_rows, grey_cols = set(), set()
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 5:
                grey_rows.add(i)
                grey_cols.add(j)
    def group(sorted_indices):
        intervals = []
        if not sorted_indices:
            return intervals
        it = iter(sorted_indices)
        start = prev = next(it)
        for x in it:
            if x == prev + 1:
                prev = x
            else:
                intervals.append((start, prev))
                start = prev = x
        intervals.append((start, prev))
        return intervals
    row_intervals = group(sorted(grey_rows))
    col_intervals = group(sorted(grey_cols))
    gap_rows, gap_cols = [], []
    for k in range(len(row_intervals) - 1):
        e1 = row_intervals[k][1]
        s2 = row_intervals[k+1][0]
        for r in range(e1 + 1, s2):
            gap_rows.append(r)
    for k in range(len(col_intervals) - 1):
        e1 = col_intervals[k][1]
        s2 = col_intervals[k+1][0]
        for c in range(e1 + 1, s2):
            gap_cols.append(c)
    min_row = min(r for r,_ in row_intervals)
    max_row = max(r for _,r in row_intervals)
    min_col = min(c for c,_ in col_intervals)
    max_col = max(c for _,c in col_intervals)
    res = [row[:] for row in grid]
    for j in gap_cols:
        for i in range(min_row, max_row + 1):
            if res[i][j] == 0:
                res[i][j] = 2
    for i in gap_rows:
        for j in range(min_col, max_col + 1):
            if res[i][j] == 0:
                res[i][j] = 2
    for j in gap_cols:
        for i in range(0, min_row):
            if res[i][j] == 0:
                res[i][j] = 1
        for i in range(max_row + 1, H):
            if res[i][j] == 0:
                res[i][j] = 1
    for i in gap_rows:
        for j in range(0, min_col):
            if res[i][j] == 0:
                res[i][j] = 1
        for j in range(max_col + 1, W):
            if res[i][j] == 0:
                res[i][j] = 1
    return res