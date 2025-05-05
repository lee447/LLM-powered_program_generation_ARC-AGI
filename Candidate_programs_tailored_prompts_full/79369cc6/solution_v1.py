def solve(grid):
    h,len_row = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    row_counts = [sum(1 for v in row if v==8) for row in grid]
    col_counts = [sum(1 for r in range(h) if grid[r][c]==8) for c in range(len_row)]
    thr_r = sorted(row_counts)[len(row_counts)//2]
    thr_c = sorted(col_counts)[len(col_counts)//2]
    stripes_r = [r for r in range(h) if row_counts[r]>=thr_r]
    stripes_c = [c for c in range(len_row) if col_counts[c]>=thr_c]
    for r in stripes_r:
        for c in stripes_c:
            if 0<r<h-1 and 0<c<len_row-1:
                a=grid[r-1][c-1]; b=grid[r-1][c+1] if c+1<len_row else None
                d=grid[r+1][c+1] if (r+1<h and c+1<len_row) else None
                c0=grid[r+1][c-1] if r+1<h else None
                if a==6 and d==6 and b!=6 and c0!=6:
                    for dr in (0,1):
                        for dc in (0,1):
                            if r+dr<h and c+dc<len_row:
                                out[r+dr][c+dc]=4
                if b==6 and c0==6 and a!=6 and d!=6:
                    for dr in (0,1):
                        for dc in (0,1):
                            if r+dr<h and c+dc<len_row:
                                out[r+dr][c+dc]=4
    return out