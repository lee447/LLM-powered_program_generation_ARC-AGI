def solve(grid):
    m, n = len(grid), len(grid[0])
    def find_stripes_h():
        stripes = []
        for i in range(m):
            row = grid[i]
            if 2 not in row and len(set(row)) == 1:
                if not stripes or stripes[-1] != i - 1:
                    stripes.append(i)
        return stripes
    def find_stripes_v():
        stripes = []
        for j in range(n):
            col = [grid[i][j] for i in range(m)]
            if 2 not in col and len(set(col)) == 1:
                if not stripes or stripes[-1] != j - 1:
                    stripes.append(j)
        return stripes
    def process_horizontal():
        stripes = find_stripes_h()
        if len(stripes) < 2:
            return False
        stripes.append(m)
        for k in range(len(stripes) - 1):
            a, b = stripes[k], stripes[k + 1]
            band = list(range(a + 1, b))
            if len(band) != 2:
                continue
            if not any(grid[r][c] == 2 for r in band for c in range(n)):
                continue
            ca = grid[a][0]
            cb = grid[b][0] if b < m else ca
            bg = ca
            blocks = []
            for r in band:
                for c in range(n - 1):
                    if grid[r][c] == grid[r][c + 1] == grid[r + 1][c] == grid[r + 1][c + 1] == 2:
                        blocks.append((r, c))
            for r, c in blocks:
                for dr in (0, 1):
                    for dc in (0, 1):
                        grid[r + dr][c + dc] = bg
            direction = 'left' if ca > cb else ('right' if ca < cb else 'left')
            for r, c in blocks:
                newc = 0 if direction == 'left' else n - 2
                for dr in (0, 1):
                    for dc in (0, 1):
                        grid[r + dr][newc + dc] = 2
        return True
    def process_vertical():
        stripes = find_stripes_v()
        if len(stripes) < 2:
            return False
        stripes.append(n)
        for k in range(len(stripes) - 1):
            a, b = stripes[k], stripes[k + 1]
            band = list(range(a + 1, b))
            if len(band) != 2:
                continue
            if not any(grid[r][c] == 2 for r in range(m) for c in band):
                continue
            ca = grid[0][a]
            cb = grid[0][b] if b < n else ca
            bg = ca
            blocks = []
            for r in range(m - 1):
                for c in band:
                    if grid[r][c] == grid[r][c + 1] == grid[r + 1][c] == grid[r + 1][c + 1] == 2:
                        blocks.append((r, c))
            for r, c in blocks:
                for dr in (0, 1):
                    for dc in (0, 1):
                        grid[r + dr][c + dc] = bg
            direction = 'up' if ca > cb else ('down' if ca < cb else 'up')
            for r, c in blocks:
                newr = 0 if direction == 'up' else m - 2
                for dr in (0, 1):
                    for dc in (0, 1):
                        grid[newr + dr][c + dc] = 2
        return True
    if not process_horizontal():
        process_vertical()
    return grid