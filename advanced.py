'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see `advanced_sample_data.py` for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    try:
        if to_member in social_graph[from_member]['following'] and from_member not in social_graph[to_member]['following']:
            print('follower')
        elif to_member not in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
            print('followed by')
        elif to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
            print('friends')
        elif to_member not in social_graph[from_member]['following'] and from_member not in social_graph[to_member]['following']:
            print('no relationship')
    except:
        if to_member in social_graph[from_member]['following']:
            print('follower')
        elif to_member not in social_graph[from_member]['following']:
            print('followed by')



def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see `advanced_sample_data.py` for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner, or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)
    winner = 'No Winner'
    w_count = 0
    #check rows
    row_win = 0
    for a in board:
        for b in a:
            if b == a[0]:
                row_win += 1
        if row_win == size: 
            winner = f'Winner: {a[0]}'
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
            winner = f'Winner: {x[0]}'
            break
        col_win = 0

    #check diag up
        
    diag_up=[board[i][i] for i,v in enumerate(board)]
    du_win = 0
    for y in diag_up:
        if y == diag_up[0]:
            du_win += 1

    if du_win == size: 
        winner = f'Winner: {diag_up[0]}'
    du_win=0

    #check diag down

    diag_down = [board[(size-1)-i][i] for i,v in enumerate(board)]
    dd_win = 0
    for y in diag_down:
        if y == diag_down[0]:
            dd_win += 1
    if dd_win == size: 
        winner = f'Winner: {diag_down[0]}'

    print(winner)

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see `advanced_sample_data.py` for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    check = []
    total = 0
    routes = list(route_map.items())

    
    while routes[0][0][0] != first_stop:
        routes.remove(routes[0])
    
    if routes[0][0][0] == first_stop:
        while routes[0][0][1] != second_stop:
            check.append(routes[0])
            routes.remove(routes[0])

    if routes[0][0][1] == second_stop:
        check.append(routes[0])
        routes.remove(routes[0])

    route_times = {x:y for x,y in check}

    for x in route_times:
        total+=route_times[x]['travel_time_mins']
    
    print(f'Estimated Time of Arrival: {total} mins')