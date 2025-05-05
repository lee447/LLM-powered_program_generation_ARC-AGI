def solve(grid):
    n=len(grid)
    for s in (5,4):
        for r in range(n-s+1):
            for c in range(n-s+1):
                ok=True
                for i in range(s):
                    for j in range(s):
                        if grid[r+i][c+j]!=8:
                            ok=False
                            break
                    if not ok:
                        break
                if ok:
                    pr=r-s
                    pc=c-s
                    if pr>=0 and pc>=0:
                        return [grid[pr+i][pc:pc+s] for i in range(s)]
    return []