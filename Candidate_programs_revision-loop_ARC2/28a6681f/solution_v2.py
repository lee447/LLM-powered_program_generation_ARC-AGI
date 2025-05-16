from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h>0 else 0
    colors = set(grid[r][c] for r in range(h) for c in range(w) if grid[r][c]!=0)
    H_colors=[]
    for c in colors:
        col_counts={}
        row_counts={}
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    col_counts[j]=col_counts.get(j,0)+1
                    row_counts[i]=row_counts.get(i,0)+1
        cols2=[j for j,cnt in col_counts.items() if cnt>=2]
        if len(cols2)==2 and any(cnt>=2 for cnt in row_counts.values()):
            H_colors.append(c)
    fill_color = min(c for c in colors if c not in H_colors)
    for c in H_colors:
        col_counts={}
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    col_counts[j]=col_counts.get(j,0)+1
        cols2=[j for j,cnt in col_counts.items() if cnt>=2]
        c_low, c_high = min(cols2), max(cols2)
        for r in range(h):
            if grid[r][c_low]==c:
                rcpos=[j for j in range(c_high+1,w) if grid[r][j]==fill_color]
                if rcpos:
                    minRC=min(rcpos)
                    if minRC - c_high - 1 <= 0:
                        for j in range(c_low+1, minRC):
                            if grid[r][j]==0:
                                grid[r][j]=fill_color
                elif grid[r][c_high]==c:
                    for j in range(c_low+1, c_high):
                        if grid[r][j]==0:
                            grid[r][j]=fill_color
    return grid