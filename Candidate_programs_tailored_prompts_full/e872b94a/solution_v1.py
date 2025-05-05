def solve(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    def get_comp(r, c):
        stack = [(r, c)]
        comp = []
        while stack:
            i, j = stack.pop()
            if visited[i][j]: continue
            visited[i][j] = True
            comp.append((i, j))
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == 5:
                    stack.append((ni, nj))
        return comp
    def signature(comp):
        pts = [(c, r) for r,c in comp]
        variants = []
        for t in range(4):
            trans = []
            for x, y in pts:
                if t == 0:
                    x0, y0 = x, y
                elif t == 1:
                    x0, y0 = y, -x
                elif t == 2:
                    x0, y0 = -x, -y
                else:
                    x0, y0 = -y, x
                trans.append((x0, y0))
            minx = min(p[0] for p in trans)
            miny = min(p[1] for p in trans)
            norm = sorted((y - miny, x - minx) for x, y in trans)
            variants.append(tuple(norm))
        return min(variants)
    shapes = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 5 and not visited[i][j]:
                comp = get_comp(i, j)
                shapes.add(signature(comp))
    cnt = len(shapes)
    return [[0] for _ in range(cnt)]
# Example usage:
input1 = [[0,0,0,0,0,0,0,5,5,0,0,0],[5,5,0,0,0,0,0,0,5,0,0,0],[0,5,5,0,0,0,5,5,5,0,0,0],[0,0,5,0,0,0,5,0,0,0,0,0],[0,0,5,0,0,0,5,5,5,5,0,0],[0,5,5,0,0,0,0,0,0,5,0,0],[0,5,0,0,5,5,5,0,0,5,0,0],[0,5,5,5,5,0,5,0,0,5,0,0],[0,0,0,0,0,0,5,0,0,5,0,0],[5,5,0,0,5,5,5,0,0,5,0,0],[0,5,0,0,5,0,0,0,5,5,0,0],[0,5,0,0,5,0,0,0,5,0,0,0]]
print(solve(input1))  # [[0],[0],[0],[0]]
input2 = [[0,5,0],[0,5,5],[0,0,5]]
print(solve(input2))  # [[0],[0]]
input3 = [[0,5,0,0,0,0,0],[0,5,5,0,0,0,0],[0,0,5,0,0,5,5],[0,5,5,0,0,5,0],[0,5,0,0,5,5,0],[0,5,0,0,5,0,0],[0,5,0,0,5,0,0]]
print(solve(input3))  # [[0],[0],[0]]
input4 = [[0,5,0,0,0,5,0,0,5,0,0,0],[0,5,0,0,0,5,0,0,5,0,0,0],[0,5,5,0,5,5,0,5,5,0,0,0],[0,0,5,0,5,0,0,5,0,0,0,0],[0,0,5,0,5,0,5,5,0,0,0,0],[5,5,5,0,5,0,5,0,0,0,0,0],[0,0,0,0,5,0,5,0,0,5,5,5],[0,0,0,5,5,0,5,0,0,5,0,0],[0,5,5,5,0,0,5,0,0,5,0,0]]
print(solve(input4))  # [[0],[0],[0],[0],[0]]