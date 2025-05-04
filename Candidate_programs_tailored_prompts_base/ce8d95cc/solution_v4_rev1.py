def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bar_cols = [c for c in range(w) if all(grid[r][c] != 0 for r in range(h))]
    non_bar_cols = [c for c in range(w) if c not in bar_cols]
    band_rows = []
    for r in range(h):
        vals = [grid[r][c] for c in non_bar_cols]
        if vals and all(v == vals[0] != 0 for v in vals):
            band_rows.append(r)
    bar_colors = []
    for c in bar_cols:
        for r in range(h):
            if r not in band_rows and grid[r][c] != 0:
                bar_colors.append(grid[r][c])
                break
    band_colors = [grid[r][non_bar_cols[0]] for r in band_rows]
    thick = [[grid[band_rows[i]][bar_cols[j]] == band_colors[i] for j in range(len(bar_cols))] for i in range(len(band_rows))]
    out_h = 2 * len(band_rows) + 1
    out_w = 2 * len(bar_cols) + 1
    out = [[0] * out_w for _ in range(out_h)]
    for r in range(out_h):
        for c in range(out_w):
            if r % 2 == 0 and c % 2 == 1:
                out[r][c] = bar_colors[c // 2]
            elif r % 2 == 1 and c % 2 == 0:
                out[r][c] = band_colors[r // 2]
            elif r % 2 == 1 and c % 2 == 1:
                j = c // 2
                if thick[r // 2][j]:
                    out[r][c] = band_colors[r // 2]
                else:
                    out[r][c] = bar_colors[j]
    return out