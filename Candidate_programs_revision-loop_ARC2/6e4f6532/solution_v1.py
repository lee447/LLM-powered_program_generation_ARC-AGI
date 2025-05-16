def solve(grid):
    h=len(grid); w=len(grid[0])
    # find wall columns (long vertical line)
    freq=[{} for _ in range(w)]
    for j in range(w):
        for i in range(h):
            freq[j][grid[i][j]]=freq[j].get(grid[i][j],0)+1
    wall_cols=[j for j in range(w) if max(freq[j].values())==h]
    if len(wall_cols)<2:
        return grid
    wl,wr=min(wall_cols),max(wall_cols)
    # background in left region
    bg_left=max({}.fromkeys([]),key=lambda x:0) if False else None
    counter={}
    for i in range(h):
        for j in range(wl):
            counter[grid[i][j]]=counter.get(grid[i][j],0)+1
    bg_left=max(counter,key=counter.get)
    out=[row[:] for row in grid]
    # erase left shapes and mirror them
    for i in range(h):
        for j in range(wl):
            v=grid[i][j]
            if v!=bg_left:
                out[i][j]=bg_left
                j2=wr+(wl-j)
                if 0<=j2<w and out[i][j2]==bg_left:
                    out[i][j2]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    freq=[{} for _ in range(w)]
    for x in range(w):
        for y in range(h):
            freq[x][grid[y][x]]=freq[x][grid[y][x]]+1 if grid[y][x] in freq[x] else 1
    wall=[i for i in range(w) if max(freq[i].values())==h]
    wl,wr=min(wall),max(wall)
    cnt={}
    for y in range(h):
        for x in range(wl):
            cnt[grid[y][x]]=cnt.get(grid[y][x],0)+1
    bg=max(cnt,key=cnt.get)
    out=[row[:] for row in grid]
    for y in range(h):
        for x in range(wl):
            v=grid[y][x]
            if v!=bg:
                out[y][x]=bg
                nx=wr+(wl-x)
                if 0<=nx<w and out[y][nx]==bg:
                    out[y][nx]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    colcount=[{} for _ in range(w)]
    for j in range(w):
        for i in range(h):
            colcount[j][grid[i][j]]=colcount[j].get(grid[i][j],0)+1
    walls=[j for j in range(w) if max(colcount[j].values())==h]
    wl,wr=min(walls),max(walls)
    freq={}
    for i in range(h):
        for j in range(wl):
            freq[grid[i][j]]=freq.get(grid[i][j],0)+1
    bg=max(freq,key=freq.get)
    out=[r[:] for r in grid]
    for i in range(h):
        for j in range(wl):
            v=grid[i][j]
            if v!=bg:
                out[i][j]=bg
                nj=wr+(wl-j)
                if 0<=nj<w and out[i][nj]==bg:
                    out[i][nj]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    # detect the two-wall columns (uniform color)
    freq=[{} for _ in range(w)]
    for x in range(w):
        for y in range(h):
            freq[x][grid[y][x]]=freq[x].get(grid[y][x],0)+1
    walls=[i for i in range(w) if max(freq[i].values())==h]
    if len(walls)<2:
        return grid
    wl,wr=min(walls),max(walls)
    # background on left side
    count={}
    for y in range(h):
        for x in range(wl):
            count[grid[y][x]]=count.get(grid[y][x],0)+1
    bg=max(count,key=count.get)
    out=[row[:] for row in grid]
    # mirror variants from left to right
    for y in range(h):
        for x in range(wl):
            v=grid[y][x]
            if v!=bg:
                out[y][x]=bg
                nx=wr + (wl - x)
                if 0<=nx<w and out[y][nx]==bg:
                    out[y][nx]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    # find wall columns
    colfreq=[{} for _ in range(w)]
    for j in range(w):
        for i in range(h):
            colfreq[j][grid[i][j]]=colfreq[j].get(grid[i][j],0)+1
    walls=[j for j in range(w) if max(colfreq[j].values())==h]
    if len(walls)<2: return grid
    wl,wr=min(walls),max(walls)
    # most common in left
    freq={}
    for i in range(h):
        for j in range(wl):
            freq[grid[i][j]]=freq.get(grid[i][j],0)+1
    bg=max(freq,key=freq.get)
    out=[row[:] for row in grid]
    for i in range(h):
        for j in range(wl):
            v=grid[i][j]
            if v!=bg:
                out[i][j]=bg
                j2=wr+(wl-j)
                if 0<=j2<w and out[i][j2]==bg:
                    out[i][j2]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    freq=[{} for _ in range(w)]
    for x in range(w):
        for y in range(h):
            freq[x][grid[y][x]]=freq[x].get(grid[y][x],0)+1
    walls=[i for i in range(w) if max(freq[i].values())==h]
    if len(walls)<2: return grid
    wl,wr=min(walls),max(walls)
    cnt={}
    for y in range(h):
        for x in range(wl):
            cnt[grid[y][x]]=cnt.get(grid[y][x],0)+1
    bg=max(cnt,key=cnt.get)
    out=[row[:] for row in grid]
    for y in range(h):
        for x in range(wl):
            v=grid[y][x]
            if v!=bg:
                out[y][x]=bg
                nx=wr+(wl-x)
                if 0<=nx<w and out[y][nx]==bg:
                    out[y][nx]=v
    return out
def solve(grid):
    h=len(grid); w=len(grid[0])
    freq=[{} for _ in range(w)]
    for x in range(w):
        for y in range(h):
            freq[x][grid[y][x]]=freq[x].get(grid[y][x],0)+1
    walls=[i for i in range(w) if max(freq[i].values())==h]
    if len(walls)<2: return grid
    wl,wr=min(walls),max(walls)
    cnt={}
    for y in range(h):
        for x in range(wl):
            cnt[grid[y][x]]=cnt.get(grid[y][x],0)+1
    bg=max(cnt,key=cnt.get)
    out=[row[:] for row in grid]
    for y in range(h):
        for x in range(wl):
            v=grid[y][x]
            if v!=bg:
                out[y][x]=bg
                j2=wr+(wl-x)
                if 0<=j2<w and out[y][j2]==bg:
                    out[y][j2]=v
    return out