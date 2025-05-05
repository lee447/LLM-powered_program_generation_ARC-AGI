def solve(grid):
    h=len(grid); w=len(grid[0])
    centers=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    (r1,c1),(r2,c2)=centers
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0:
                if r2>r1 and c2>c1 and r>r1 and r<=r2 and c>=c1 and c<c2:
                    grid[r][c]=4
                elif r2<r1 and c2<c1 and r<r1 and r>=r2 and c<=c1 and c>c2:
                    grid[r][c]=4
                elif r2>r1 and c2<c1 and r>r1 and r<=r2 and c>c2 and c<=c1:
                    grid[r][c]=4
                elif r2<r1 and c2>c1 and r<r1 and r>=r2 and c>=c1 and c<c2:
                    grid[r][c]=4
    return grid