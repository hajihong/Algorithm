from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    answer = []
    visited = [[False]*m for _ in range(n)]
    
    def bfs(x,y):
        cnt = int(maps[x][y])
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
    
        while queue:
            a, b = queue.popleft()
        
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
            
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    queue.append((nx, ny))
                
                
    
        return cnt
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                result = bfs(i,j)
                answer.append(result)
                
    answer.sort()
                
    if answer == []:
        return [-1]
    else:
        return answer