paths = []
edges = {}

def search(a, b, path):
    global paths
    global edges
    for idx in range(len(edges[a])):
        if edges[a][idx] == b:
            path.append(edges[a][idx])
            paths.append(path)
        elif edges[a][idx].isupper() or (edges[a][idx].islower() and edges[a][idx] not in path):
            newPath = path.copy()
            newPath.append(edges[a][idx])
            search(edges[a][idx],b,newPath)

lines = []
with open('inputs/day12.txt') as f:
    lines = f.readlines()

for line in lines:
    edge = line.strip().split('-')
    if edge[0] == 'start':
        if 'start' not in edges:
            edges['start'] = []
        if edge[1] not in edges['start']:
            edges['start'].append(edge[1])
    elif edge[1] == 'start':
        if 'start' not in edges:
            edges['start'] = []
        if edge[0] not in edges['start']:
            edges['start'].append(edge[0])
    elif edge[0] == 'end':
        if edge[1] not in edges:
            edges[edge[1]] = []
        if 'end' not in edges[edge[1]]:
            edges[edge[1]].append('end')
    elif edge[1] == 'end':
        if edge[0] not in edges:
            edges[edge[0]] = []
        if 'end' not in edges[edge[0]]:
            edges[edge[0]].append('end')
    else:
        if edge[0] not in edges:
            edges[edge[0]] = []
        if edge[1] not in edges[edge[0]]:
            edges[edge[0]].append(edge[1])
        if edge[1] not in edges:
            edges[edge[1]] = []
        if edge[0] not in edges[edge[1]]:
            edges[edge[1]].append(edge[0])

search('start','end', ['start'])

print(len(paths))
