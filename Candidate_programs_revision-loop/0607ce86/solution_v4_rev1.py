from collections import Counter
def solve(grid):
    H, W = len(grid), len(grid[0])
    def find_vp():
        best_p, best_score = 1, -1.0
        maxp = H//2+1 if H//2+1>2 else H
        for p in range(2, maxp):
            reps = [[0]*W for _ in range(p)]
            for r in range(p):
                for c in range(W):
                    cnt=Counter(grid[i][c] for i in range(r, H, p))
                    reps[r][c]=cnt.most_common(1)[0][0]
            match=0
            total=H*W
            for i in range(H):
                for j in range(W):
                    if grid[i][j]==reps[i%p][j]:
                        match+=1
            score=match/total
            if score>best_score:
                best_score, best_p = score, p
        return best_p
    def find_hp():
        best_p, best_score = 1, -1.0
        maxp = W//2+1 if W//2+1>2 else W
        for p in range(2, maxp):
            reps = [[0]*p for _ in range(H)]
            for c in range(p):
                for r in range(H):
                    cnt=Counter(grid[r][j] for j in range(c, W, p))
                    reps[r][c]=cnt.most_common(1)[0][0]
            match=0
            total=H*W
            for i in range(H):
                for j in range(W):
                    if grid[i][j]==reps[i][j%p]:
                        match+=1
            score=match/total
            if score>best_score:
                best_score, best_p = score, p
        return best_p
    vp=find_vp()
    hp=find_hp()
    pattern=[[0]*hp for _ in range(vp)]
    for i in range(vp):
        for j in range(hp):
            cnt=Counter(grid[x][y] for x in range(i, H, vp) for y in range(j, W, hp))
            pattern[i][j]=cnt.most_common(1)[0][0]
    res=[[pattern[i%vp][j%hp] for j in range(W)] for i in range(H)]
    return res