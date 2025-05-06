def solve(grid):
    cool = {1,6,8}
    stats = {}
    for i,row in enumerate(grid):
        for j,v in enumerate(row):
            if v in cool:
                if v not in stats:
                    stats[v] = {"count":0,"minc":j,"minr":i,"maxr":i,"maxc":j}
                s = stats[v]
                s["count"] += 1
                if j < s["minc"]: s["minc"] = j
                if i < s["minr"]: s["minr"] = i
                if i > s["maxr"]: s["maxr"] = i
                if j > s["maxc"]: s["maxc"] = j
    sel = max(stats.items(), key=lambda x:(x[1]["count"], -x[1]["minc"]))[0]
    s = stats[sel]
    return [[grid[i][j] if grid[i][j]==sel else 0 for j in range(s["minc"],s["maxc"]+1)] for i in range(s["minr"],s["maxr"]+1)]