from collections import deque

def find_exit(matrix, start):
    n = len(matrix)
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    prev = {}
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while queue:
        x, y, z = queue.popleft()
        if x == n-1 or y == n-1 or z == n-1:
            path = []
            while (x, y, z) != start:
                path.append((x, y, z))
                x, y, z = prev[(x, y, z)]
            path.append(start)
            path.reverse()
            return path
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or nz < 0 or nz >= n:
                continue
            if matrix[nx][ny][nz] == 0 and (nx, ny, nz) not in visited:
                queue.append((nx, ny, nz))
                visited.add((nx, ny, nz))
                prev[(nx, ny, nz)] = (x, y, z)
    return "Выхода из лабиринта нет"

maze = [[[0 for _ in range(15)] for _ in range(15)] for _ in range(15)]
maze[1][1][1] = 1
maze[1][2][1] = 1
maze[1][3][1] = 1
maze[1][4][1] = 1
maze[1][5][1] = 1
maze[1][6][1] = 1
maze[1][7][1] = 1
maze[1][8][1] = 1
maze[1][9][1] = 1
maze[1][10][1] = 1
maze[1][11][1] = 1
maze[1][12][1] = 1
maze[1][13][1] = 1
maze[1][14][1] = 1
maze[3][3][3] = 1
maze[3][4][3] = 1
maze[3][5][3] = 1
maze[3][6][3] = 1
maze[3][7][3] = 1
maze[3][8][3] = 1
maze[3][9][3] = 1
maze[3][10][3] = 1
maze[3][11][3] = 1
maze[3][12][3] = 1
maze[3][13][3] = 1
maze[3][14][3] = 1
start = (0, 0, 0)
path = find_exit(maze, start)
print(path)