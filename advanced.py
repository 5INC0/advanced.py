def relationship_status(from_member, to_member, social_graph):
    try:
        if to_member in social_graph[from_member]['following'] and from_member not in social_graph[to_member]['following']:
            return('follower')
        elif to_member not in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
            return('followed by')
        elif to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
            return('friends')
        elif to_member not in social_graph[from_member]['following'] and from_member not in social_graph[to_member]['following']:
            return('no relationship')
    except:
        if to_member in social_graph[from_member]['following']:
            return('follower')
        elif to_member not in social_graph[from_member]['following']:
            return('followed by')

def tic_tac_toe(board):
    size = len(board)
    winner = "NO WINNER"
    #check rows
    row_win = 0
    for a in board:
        for b in a:
            if b == a[0]:
                row_win += 1
        if row_win == size: 
            winner = a[0]
            break
        row_win = 0

    #check col
        
    col = [x for x in zip(*board)]
    col_win = 0
    for x in col:
        for y in x:
            if y == x[0]:
                col_win += 1
        if col_win == size: 
            winner = x[0]
            break
        col_win = 0

    #check diag up
        
    diag_up=[board[i][i] for i,v in enumerate(board)]
    du_win = 0
    for y in diag_up:
        if y == diag_up[0]:
            du_win += 1

    if du_win == size: 
        winner = diag_up[0]
    du_win=0

    #check diag down

    diag_down = [board[(size-1)-i][i] for i,v in enumerate(board)]
    dd_win = 0
    for y in diag_down:
        if y == diag_down[0]:
            dd_win += 1
    if dd_win == size: 
        winner = diag_down[0]

    if winner == "":
        return("NO WINNER")
    else: 
        return(winner)

def eta(first_stop, second_stop, route_map):

    check = []
    total = 0
    routes = list(route_map.items())

    #skip over it not delete
    while routes and routes[0][0][0] != first_stop:
        routes.append(routes[0])
        routes.remove(routes[0])
    
    if routes and routes[0][0][0] == first_stop:
        while routes and routes[0][0][1] != second_stop:
            check.append(routes[0])
            routes.remove(routes[0])

    if routes and routes[0][0][1] == second_stop:
        check.append(routes[0])
        routes.remove(routes[0])

    route_times = {x:y for x,y in check}

    for x in route_times:
        total+=route_times[x]['travel_time_mins']

    return(total)