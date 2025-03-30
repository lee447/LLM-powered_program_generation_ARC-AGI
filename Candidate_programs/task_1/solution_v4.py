def solve(grid):
    h = len(grid)
    if h == 0:
        return grid
    w = len(grid[0])
    def segments(row):
        segs = []
        i = 0
        while i < len(row):
            if row[i] != 0:
                start = i
                while i < len(row) and row[i] != 0:
                    i += 1
                segs.append((start, i, row[start:i]))
            else:
                i += 1
        return segs
    out = []
    for r in grid:
        segs = segments(r)
        newrow = [0]*w
        # we consider only segments of length>=2 as valid clusters
        valid = [s for s in segs if (s[1]-s[0])>=2]
        if len(valid) == 0:
            out.append(newrow)
            continue
        # if there are at least two segments, we use only the first two;
        # otherwise, if only one, we use that one.
        if len(valid) >= 2:
            s1 = valid[0]
            s2 = valid[1]
            # Let target length be the length of the first segment.
            t = s1[1]-s1[0]
            def trim(seg, target):
                s, e, lst = seg
                if len(lst) > target:
                    return lst[:target]
                return lst
            seg1 = trim(s1,t)
            seg2 = trim(s2,t)
            # choose the candidate with larger sum; in tie, choose the first.
            if sum(seg1) >= sum(seg2):
                chosen = seg1[:]
            else:
                chosen = seg2[:]
                # if chosen is from s2 and first seg exists, force last element to equal s1's last element if different
                if seg1 and chosen[-1] != seg1[-1]:
                    chosen[-1] = seg1[-1]
            # fill both segments with the chosen pattern
            start1 = s1[0]
            end1 = s1[0] + len(chosen)
            start2 = s2[0]
            end2 = s2[0] + len(chosen)
            for i, val in enumerate(chosen):
                if start1+i < w:
                    newrow[start1+i] = val
                if start2+i < w:
                    newrow[start2+i] = val
        else:
            s1 = valid[0]
            seg1 = s1[2]
            # use the segment as‐is (or trimmed if too long – here we leave it)
            start1 = s1[0]
            for i, val in enumerate(seg1):
                if start1+i < w:
                    newrow[start1+i] = val
        out.append(newrow)
    return out


if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read()
    if data:
        inpt = json.loads(data)
        res = solve(inpt)
        sys.stdout.write(json.dumps(res))
    else:
        pass