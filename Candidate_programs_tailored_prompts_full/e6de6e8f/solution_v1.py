def solve(grid):
    h, w = len(grid), len(grid[0])
    steps = []
    for c in range(w):
        cnt = sum(1 for r in range(h) if grid[r][c] == 2)
        if cnt > 0:
            steps.append(2 if cnt > 1 else 1)
    L = min(len(steps), 7)
    out = [[0]*7 for _ in range(L+1)]
    out[0][3] = 3
    col = 3
    for i in range(L):
        s = steps[i]
        r = i+1
        for j in range(s):
            if 0 <= col+j < 7:
                out[r][col+j] = 2
        col += 1
    return out