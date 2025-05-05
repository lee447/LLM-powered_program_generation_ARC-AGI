def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = []
    for i in range(h):
        j = 0
        while j < w:
            if grid[i][j] == 8:
                k = j
                while k < w and grid[i][k] == 8:
                    k += 1
                if k - j == 3:
                    centers.append((i, j + 1))
                j = k
            else:
                j += 1
    for j in range(w):
        i = 0
        while i < h:
            if grid[i][j] == 8:
                k = i
                while k < h and grid[k][j] == 8:
                    k += 1
                if k - i == 3:
                    centers.append((i + 1, j))
                i = k
            else:
                i += 1
    res = [row[:] for row in grid]
    for r, c in centers:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = r + dr, c + dc
                if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] in (0, 8):
                    res[rr][cc] = 8
    return res