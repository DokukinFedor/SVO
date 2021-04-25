n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
grph = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            grph[i].append(j)
print(grph)