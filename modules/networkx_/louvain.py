"""
https://github.com/shobrook/communities
"""
from communities.algorithms import louvain_method
from communities.visualization import draw_communities, louvain_animation

import networkx as nx
import numpy as np

G = nx.Graph()
# Zachary's karate club，空手道俱乐部的数据
edges = [
    (2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1), (6, 1), (7, 1), (7, 5), (7, 6), (8, 1), (8, 2), (8, 3),
    (8, 4), (9, 1), (9, 3), (10, 3), (11, 1), (11, 5), (11, 6), (12, 1), (13, 1), (13, 4), (14, 1), (14, 2),
    (14, 3), (14, 4), (17, 6), (17, 7), (18, 1), (18, 2), (20, 1), (20, 2), (22, 1), (22, 2), (26, 24), (26, 25),
    (28, 3), (28, 24), (28, 25), (29, 3), (30, 24), (30, 27), (31, 2), (31, 9), (32, 1), (32, 25), (32, 26),
    (32, 29), (33, 3), (33, 9), (33, 15), (33, 16), (33, 19), (33, 21), (33, 23), (33, 24), (33, 30), (33, 31),
    (33, 32), (34, 9), (34, 10), (34, 14), (34, 15), (34, 16), (34, 19), (34, 20), (34, 21), (34, 23), (34, 24),
    (34, 27), (34, 28), (34, 29), (34, 30), (34, 31), (34, 32), (34, 33)
]
G.add_edges_from(edges)
# nx.draw(G, with_labels=True)

adj_matrix = np.array(nx.adjacency_matrix(G).todense())  # 从Networkx导出邻接矩阵
communities, frames = louvain_method(adj_matrix)

# draw_communities(adj_matrix, communities)
louvain_animation(adj_matrix, frames)
