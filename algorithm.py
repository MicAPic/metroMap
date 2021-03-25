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
