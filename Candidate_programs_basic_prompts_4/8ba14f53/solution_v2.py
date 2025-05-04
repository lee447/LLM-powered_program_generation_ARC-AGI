def solve(grid):
    h, w = len(grid), len(grid[0])
    bw = w // 3
    blocks = [ [row[i*bw:(i+1)*bw] for row in grid] for i in range(3) ]
    def maj(b):
        cnt = {}
        for r in b:
            for x in r:
                if x:
                    cnt[x] = cnt.get(x,0) + 1
        return max(cnt.items(), key=lambda y:(y[1],-y[0]))[0] if cnt else 0
    bc = [maj(b) for b in blocks]
    ans = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i >= j:
                if i == 0:
                    ans[i][j] = bc[0]
                else:
                    ans[i][j] = bc[1]
            else:
                ans[i][j] = 0
    return ans