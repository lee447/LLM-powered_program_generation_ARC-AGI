from collections import defaultdict
def solve(grid):
    h, w = len(grid), len(grid[0])
    windows = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8:
                windows.append((r,c))
    groups = defaultdict(list)
    for r,c in windows:
        groups[r].append(c)
    out = []
    for r in sorted(groups):
        cols = sorted(groups[r])
        for i in range(0, len(cols), 2):
            c1, c2 = cols[i], cols[i+1]
            start, end = c1+2, c2-1
            out.append([grid[r][j] for j in range(start, end+1)])
            out.append([grid[r+1][j] for j in range(start, end+1)])
    return out