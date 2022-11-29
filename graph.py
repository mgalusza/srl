import networkx as nx

G = nx.Graph()

for i in range(0,10):
    G.add_node(i)

global paths

paths = []

def find_path(G,curr_node,e_node,visited, path,n,steps):
    global paths
    if curr_node == e_node:
        paths = paths + [path]
        return 
    if n == steps:
        return 
    visited.add(curr_node)
    for neigh in G.neighbors(curr_node):
        if neigh not in visited:
            find_path(G,neigh,e_node,visited,path + [neigh],n+1,steps)

def start_path(G,s_node, e_node,steps):
    paths = []
    find_path(G,s_node,e_node,set(),[s_node],0,steps)

G.add_edge((1),(2))
G.add_edge((2),(3))
G.add_edge((1),(5))
G.add_edge((1),(4))
G.add_edge((4),(3))
start_path(G,(1),(3),5)
print(paths)