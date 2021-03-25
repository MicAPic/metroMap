def Metro_Dijkstra(n, start, finish, matrix):
    check = [True] * n
    weight = [300] * n
    parent = [0] * n
    weight[start] = 0
    for _ in range(n):
        min_weight = 301
        mw_id = -1
        for station in range(n):
            if check[station] and weight[station] < min_weight:
                min_weight = weight[station]
                mw_id = station
        for adj_st in range(n):
            if weight[mw_id] + matrix[mw_id][adj_st] < weight[adj_st]:
                weight[adj_st] = weight[mw_id] + matrix[mw_id][adj_st]
                parent[adj_st] = mw_id
        check[mw_id] = False
    path = []
    prev_station = finish
    while prev_station != start:
        path.append(prev_station)
        prev_station = parent[prev_station]
    path.append(start)
    path.reverse()
    return f'Кратачайший путь из {start} в {finish}: {weight[finish]} мин, проходит через: {path}'
    # return weight[finish], path


# routes = [[0, 10, 300, 300, 300, 300, 300, 300, 300],
#           [10, 0, 8, 7, 3, 300, 300, 300, 300],
#           [300, 8, 0, 300, 300, 11, 300, 300, 300],
#           [300, 7, 300, 0, 300, 300, 300, 8, 300],
#           [300, 3, 300, 300, 0, 300, 300, 300, 11],
#           [300, 300, 11, 300, 300, 0, 5, 300, 300],
#           [300, 300, 300, 300, 300, 5, 0, 5, 300],
#           [300, 300, 300, 8, 300, 300, 5, 0, 300],
#           [300, 300, 300, 300, 11, 300, 300, 300, 0]]
