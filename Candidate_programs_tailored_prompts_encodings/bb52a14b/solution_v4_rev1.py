def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seeds = []
    patterns = [([1,4,1],'A'),([4,8,4],'B')]
    for i in range(h):
        for j in range(w):
            for pat,_ in patterns:
                if j+2<w and grid[i][j]==pat[0] and grid[i][j+1]==pat[1] and grid[i][j+2]==pat[2]:
                    seeds.append((i,j,pat,'h'))
                if i+2<h and grid[i][j]==pat[0] and grid[i+1][j]==pat[1] and grid[i+2][j]==pat[2]:
                    seeds.append((i,j,pat,'v'))
    for r,c,pat,dir in seeds:
        if dir=='h':
            for x in range(c-1,-1,-1):
                if grid[r][x]==8: break
                if out[r][x]==0: out[r][x]=pat[(x-c)%3]
            for x in range(c+3,w):
                if grid[r][x]==8: break
                if out[r][x]==0: out[r][x]=pat[(x-c)%3]
        else:
            for y in range(r-1,-1,-1):
                if grid[y][c]==8: break
                if out[y][c]==0: out[y][c]=pat[(y-r)%3]
            for y in range(r+3,h):
                if grid[y][c]==8: break
                if out[y][c]==0: out[y][c]=pat[(y-r)%3]
    return out