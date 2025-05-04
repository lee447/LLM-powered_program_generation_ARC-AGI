def solve(grid):
    h,len_row = len(grid), len(grid[0])
    bars_by_color = {}
    for c in range(len_row):
        r = 0
        while r < h:
            color = grid[r][c]
            if color != 0 and color != 2:
                run = 1
                while r + run < h and grid[r+run][c] == color:
                    run += 1
                if run >= 3:
                    start = r
                    end = r + run - 1
                    if (start == 0 or grid[start-1][c] != color) and (end == h-1 or grid[end+1][c] != color):
                        bars_by_color.setdefault(color, []).append((start + run//2, c))
                r += run
            else:
                r += 1
    start = None
    for i in range(h):
        for j in range(len_row):
            if grid[i][j] == 2:
                start = (i, j)
                break
        if start is not None:
            break
    if start is None:
        return grid
    order_colors = sorted(bars_by_color.keys(), key=lambda col: min(r for r,c in bars_by_color[col]))
    cur_r, cur_c = start
    for col in order_colors:
        bars = sorted(bars_by_color[col], key=lambda x: (x[0], x[1]))
        for tar_r, tar_c in bars:
            dc = 1 if tar_c > cur_c else -1
            for c in range(cur_c, tar_c + dc, dc):
                if grid[cur_r][c] == 0:
                    grid[cur_r][c] = 2
            dr = 1 if tar_r > cur_r else -1
            for r in range(cur_r, tar_r + dr, dr):
                if grid[r][tar_c] == 0:
                    grid[r][tar_c] = 2
            cur_r, cur_c = tar_r, tar_c
    return grid