from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    rows = range(1, h-1)
    r1 = next(i for i in rows if any(grid[i][j]==0 for j in range(w)))
    r2 = next(i for i in rows if i>r1 and any(grid[i][j]==0 for j in range(w)))
    cols1 = [j for j in range(w) if grid[r1][j]==0]
    cols2 = [j for j in range(w) if grid[r2][j]==0]
    avg1 = sum(cols1)/len(cols1)
    avg2 = sum(cols2)/len(cols2)
    slope = 1 if avg2>=avg1 else -1
    initial = min(cols1) if slope>0 else max(cols1)
    for i in range(r1, h-1):
        zero_cols = [j for j in range(w) if grid[i][j]==0]
        if not zero_cols: continue
        mn, mx = min(zero_cols), max(zero_cols)
        ideal = initial + slope*(i - r1)
        if slope>0:
            if ideal>mx:
                out[i][mx] = 8
                break
            if ideal<mn:
                continue
            out[i][ideal] = 8
        else:
            if ideal<mn:
                break
            if ideal>mx:
                continue
            out[i][ideal] = 8
    return out