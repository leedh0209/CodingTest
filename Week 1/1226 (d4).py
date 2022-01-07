def find_maze(curr, last, maze, visited):
    global answer
    if maze[curr[0]][curr[1] + 1] != 1 and curr[1] + 1 != last[1] and visited[curr[0]][curr[1] + 1] != 1:
        if maze[curr[0]][curr[1] + 1] == 3:
            answer = 1
        new_curr = [curr[0], curr[1] + 1]
        new_visited = visited[:]
        new_visited[curr[0]][curr[1]] = 1
        find_maze(new_curr, curr, maze, new_visited)
    if maze[curr[0]][curr[1] - 1] != 1 and curr[1] - 1 != last[1] and visited[curr[0]][curr[1] - 1] != 1:
        if maze[curr[0]][curr[1] - 1] == 3:
            answer = 1
        new_curr = [curr[0], curr[1] - 1]
        new_visited = visited[:]
        new_visited[curr[0]][curr[1]] = 1
        find_maze(new_curr, curr, maze, new_visited)
    if maze[curr[0] + 1][curr[1]] != 1 and curr[0] + 1 != last[0] and visited[curr[0] + 1][curr[1]] != 1:
        if maze[curr[0] + 1][curr[1]] == 3:
            answer = 1
        new_curr = [curr[0] + 1, curr[1]]
        new_visited = visited[:]
        new_visited[curr[0]][curr[1]] = 1
        find_maze(new_curr, curr, maze, new_visited)
    if maze[curr[0] - 1][curr[1]] != 1 and curr[0] - 1 != last[0] and visited[curr[0] - 1][curr[1]] != 1:
        if maze[curr[0] - 1][curr[1]] == 3:
            answer = 1
        new_curr = [curr[0] - 1, curr[1]]
        new_visited = visited[:]
        new_visited[curr[0]][curr[1]] = 1
        find_maze(new_curr, curr, maze, new_visited)


for test_case in range(10):
    T = int(input())
    array = [list(map(int, str(input()))) for _ in range(16)]
    visited = array[:]
    visited[1][1] = 1
    answer = 0
    start = [1, 1]
    find_maze(start, start, array, visited)

    print(f'#{T} {answer}')

