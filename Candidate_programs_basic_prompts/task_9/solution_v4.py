def solve(grid):
    n = len(grid)
    m = len(grid[0])
    bw = m // 3
    color_map = {0:6,1:4,2:1}
    band_colors = []
    for b in range(3):
        counts = [0]*n
        for i in range(n):
            for j in range(b*bw, (b+1)*bw):
                if grid[i][j] == 5:
                    counts[i] += 1
        mx = max(counts)
        tops = [i for i,c in enumerate(counts) if c==mx]
        if len(tops)==1:
            band_colors.append(color_map[tops[0]])
        else:
            band_colors.append(9 if len(tops)==3 else 3)
    return [[band_colors[c//bw] for c in range(m)] for _ in range(n)]