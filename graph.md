+ [Course Schedule](#course-schedule)
+ [Course Schedule II](#course-schedule-ii)
+ [Number of Islands](#number-of-islands)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
<!-----solution----->

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root: 'Node'):
    if not root:
        return 0

    depth = 1
    if root.children:
        depth += max(self.maxDepth(child) for child in root.children)
    return depth
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid):
    if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
    visited = set((0, 0))
    queue = collections.deque([(0, 0, 1)])
    
    while queue:
        x, y, level = queue.popleft()
        if (x, y) == (len(grid) - 1, len(grid[0]) - 1): return level
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0 and (x + dx, y + dy) not in visited:
                visited.add((x + dx, y + dy))
                queue.append((x + dx, y + dy, level + 1))
        
    return -1
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    price_table = [float('inf')]*n
    price_table[src] = 0

    for source, destination, ticket_price in flights:
        if source == src:
            price_table[destination] = ticket_price
    
    
    for trasfer in range(0, K):            
        current_price = [*price_table]
        
        for source, destination, ticket_price in flights:             
            current_price[destination] = min(current_price[destination], price_table[source] + ticket_price )
         
        price_table = current_price        
    
    if price_table[dst] == float('inf'):
        return -1
    else:
        return price_table[dst]
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def numIslands(self, grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.mark_connected_land(grid, i, j)
                count += 1
    return count

def mark_connected_land(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = ':)'
    self.mark_connected_land(grid, i+1, j)
    self.mark_connected_land(grid, i-1, j)
    self.mark_connected_land(grid, i, j+1)
    self.mark_connected_land(grid, i, j-1)
```

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def findOrder(self, numCourses, prerequisites):
    self.graph = collections.defaultdict(list) # a graph for all courses
    self.res = [] # start from empty
    for pair in prerequisites:
        self.graph[pair[0]].append(pair[1]) 
    self.visited = [0 for x in range(numCourses)] # DAG detection 
    for x in range(numCourses):
        if not self.DFS(x):
            return []
         # continue to search the whole graph
    return self.res

def DFS(self, node):
    if self.visited[node] == -1: # cycle detected
        return False
    if self.visited[node] == 1:
        return True # has been finished, and been added to self.res
    self.visited[node] = -1 # mark as visited
    for x in self.graph[node]:
        if not self.DFS(x):
            return False
    self.visited[node] = 1 # mark as finished
    self.res.append(node) # add to solution as the course depenedent on previous ones
    return True
```

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
```