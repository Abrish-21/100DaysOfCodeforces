from collections import defaultdict

def baboons():
    t = int(input())
    relative = list(map(int, input().split()))
    if len(relative) == 1:return 1
    graph = defaultdict(list)
    for i in range(t):
        graph[relative[i]].append(i + 1)
        graph[i+1].append(relative[i])
    visited = set()
    count = 0
    def dfs(node, visited):
        if not node: return
        visited.add(node)
        for neighbors in graph[node]:
            if neighbors not in visited:
                dfs(neighbors, visited)
    

    for node in range(1,t+1):
        if node not in visited :
            dfs(node, visited)
            count += 1
    return count
print(baboons())



