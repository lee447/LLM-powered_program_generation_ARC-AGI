def solve(grid):
    h = len(grid)
    if h==0: 
        return grid
    w = len(grid[0])
    # flood‐fill to get connected red regions (red==2)
    # We'll use DFS (4‐neighbors)
    seen = [[False]*w for _ in range(h)]
    comps = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                while stack:
                    r,c = stack.pop()
                    if r<0 or r>=h or c<0 or c>=w: 
                        continue
                    if seen[r][c]:
                        continue
                    if grid[r][c] != 2:
                        continue
                    seen[r][c] = True
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==2:
                            stack.append((nr,nc))
                comps.append(comp)
    # Decide for each connected red component whether to recolor it (to light blue = 8).
    # Our heuristic uses the component's average row and average col.
    # Let diff = avg_col - avg_row.
    # We'll recolor the entire component (all its red cells) if our decision function returns True.
    def flip_decision(comp):
        n = len(comp)
        sr = sum(r for r,c in comp)
        sc = sum(c for r,c in comp)
        avg_row = sr / n
        avg_col = sc / n
        diff = avg_col - avg_row
        # Our heuristic:
        # (1) If diff < 2 then normally do not flip; except if (avg_row > 3 and diff < 0) then flip.
        if diff < 2:
            if avg_row > 3 and diff < 0:
                return True
            return False
        # (2) If avg_row < 2 then flip.
        if avg_row < 2:
            return True
        # (3) If avg_row > 5 then flip.
        if avg_row > 5:
            return True
        # (4) If 3 <= diff <= 5 then flip, except if avg_row < 2 (already handled).
        if 3 <= diff <= 5:
            return True
        # (5) If diff >= 10 then flip if (avg_row < 2 or avg_row > 5).
        if diff >= 10:
            if avg_row < 2 or avg_row > 5:
                return True
            return False
        # Otherwise do not flip.
        return False

    # Make a copy of grid (we assume we can update in place)
    out = [row[:] for row in grid]
    # For each connected red region, if decision returns True, set all its cells to 8.
    for comp in comps:
        if flip_decision(comp):
            for r,c in comp:
                out[r][c] = 8
    return out

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        result = solve(grid)
        sys.stdout.write(json.dumps(result))
    else:
        sys.stdout.write("[]")