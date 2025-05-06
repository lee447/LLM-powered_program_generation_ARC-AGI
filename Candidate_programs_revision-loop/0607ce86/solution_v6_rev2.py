from collections import Counter
def solve(grid):
    H,W=len(grid),len(grid[0])
    def find_period(axis):
        best_score=-1; best_p=1
        if axis=='h':
            for p in range(2,W//2+1):
                match=total=0
                for i in range(H):
                    for j in range(W-p):
                        total+=1
                        if grid[i][j]==grid[i][j+p]: match+=1
                score=match/total if total else 0
                if score>best_score:
                    best_score, best_p=score, p
        else:
            for p in range(2,H//2+1):
                match=total=0
                for i in range(H-p):
                    for j in range(W):
                        total+=1
                        if grid[i][j]==grid[i+p][j]: match+=1
                score=match/total if total else 0
                if score>best_score:
                    best_score, best_p=score, p
        return best_p
    hp=find_period('h')
    vp=find_period('v')
    tile=[[0]*hp for _ in range(vp)]
    for i in range(vp):
        for j in range(hp):
            cnt=Counter()
            for x in range(i,H,vp):
                for y in range(j,W,hp):
                    cnt[grid[x][y]]+=1
            tile[i][j]=cnt.most_common(1)[0][0]
    return [[tile[i%vp][j%hp] for j in range(W)] for i in range(H)]