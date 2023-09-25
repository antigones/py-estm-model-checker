def get_neighbours(i,j,height,width):
    return [(x,y) for x, y in [
            (i-1, j),   # n
            (i, j-1),   # w
            (i+1, j),   # s
            (i, j+1),   # e
        ]
        if 0 <= x < height and 0 <= y < width]

def emoji_print(matrix,emoji_map):
    out = list()
    for elm in matrix:
        content = [emoji_map[x] for x in elm]
        out.append("".join(content))
    print('\n'.join(out))