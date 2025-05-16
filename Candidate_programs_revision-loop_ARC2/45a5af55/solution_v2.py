def solve(grid):
    stripes = []
    prev_color = None
    count = 0
    for row in grid:
        c = row[0]
        if c == prev_color:
            count += 1
        else:
            if prev_color is not None:
                stripes.append((prev_color, count))
            prev_color = c
            count = 1
    stripes.append((prev_color, count))
    if not stripes:
        return []
    total_before = sum(t for _, t in stripes[:-1])
    center_color, center_thickness = stripes[-1]
    S = 2 * total_before + center_thickness
    out = [[center_color] * S for _ in range(S)]
    offset = 0
    for color, thickness in stripes[:-1]:
        for dt in range(thickness):
            top = offset + dt
            bot = S - 1 - (offset + dt)
            for j in range(offset, S - offset):
                out[top][j] = color
                out[bot][j] = color
            for i in range(offset, S - offset):
                out[i][offset + dt] = color
                out[i][S - 1 - (offset + dt)] = color
        offset += thickness
    return out