def solution(wallpaper):
    # 가장 큰 r, c에 1씩 더하기
    # 가장 작은 r, c

    min_r, min_c = 1e9, 1e9
    max_r, max_c = -1, -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_r = min(min_r, i)
                min_c = min(min_c, j)
                max_r = max(max_r, i)
                max_c = max(max_c, j)

    return [min_r, min_c, max_r + 1, max_c + 1]
