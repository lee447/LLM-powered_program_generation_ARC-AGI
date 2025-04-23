def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    frames = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 5 and not visited[i][j]:
                stack = [(i,j)]
                pts = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<H and 0<=cc<W and not visited[rr][cc] and grid[rr][cc]==5:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                rs = [r for r,c in pts]; cs = [c for r,c in pts]
                frames.append((min(rs), max(rs), min(cs), max(cs)))
    out = [row[:] for row in grid]
    for top,bot,left,right in frames:
        # fill interior
        for r in range(top+1, bot):
            for c in range(left+1, right):
                if out[r][c] == 0:
                    out[r][c] = 2
        # stripe
        stripe_row = top-1
        if stripe_row >= 0:
            height = (bot - top + 1)
            stripe_len = height + 1
            interior_w = (right - left - 1)
            diff = stripe_len - interior_w
            shift = diff // 2
            start = left+1 - shift
            end = start + stripe_len - 1
            if start < 0:
                start = 0
                end = start + stripe_len - 1
            if end >= W:
                end = W-1
                start = end - stripe_len + 1
            for c in range(start, end+1):
                if out[stripe_row][c] == 0:
                    out[stripe_row][c] = 2
    return out