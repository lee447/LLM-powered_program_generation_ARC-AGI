def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    result = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 5:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append(comp)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 5:
                result[r][c] = 5
    for comp in comps:
        rows = [r for r, _ in comp]
        cols = [c for _, c in comp]
        minr, maxr, minc, maxc = min(rows), max(rows), min(cols), max(cols)
        present_top = set(c for r, c in comp if r == minr)
        gap = next(c for c in range(minc, maxc + 1) if c not in present_top)
        for r in range(minr + 1, maxr):
            for c in range(minc + 1, maxc):
                if result[r][c] == 0:
                    result[r][c] = 2
        rowbar = minr - 1
        if 0 <= rowbar < h:
            left_size = gap - minc
            right_size = maxc - gap
            direction = -1 if left_size >= right_size else 1
            result[rowbar][gap] = 2
            c = gap + direction
            while 0 <= c < w and result[rowbar][c] == 0:
                result[rowbar][c] = 2
                c += direction
    return result