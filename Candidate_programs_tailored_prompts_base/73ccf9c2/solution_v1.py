def solve(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r,c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] != 0:
                                visited[nr][nc] = True
                                stack.append((nr,nc))
                comps.append(comp)
    def score(comp):
        return sum(r+c for r,c in comp)/len(comp)
    target = max(comps, key=score)
    rs = [r for r,c in target]; cs = [c for r,c in target]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    return [row[c0:c1+1] for row in grid[r0:r1+1]]