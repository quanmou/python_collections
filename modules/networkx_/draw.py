import networkx as nx
import matplotlib.pyplot as plt

# 创建空的网格
G = nx.Graph()
# 添加节点
G.add_node('JFK')
G.add_nodes_from(['SFO', 'LAX', 'ATL', 'FLO', 'DFW', 'HNL'])
# 将节点分类
nodelist1 = ['SFO', 'LAX', 'ATL', 'FLO']
nodelist2 = ['DFW', 'HNL', 'JFK']

# 添加连线
G.add_edges_from(
    [('JFK', 'SFO'), ('JFK', 'LAX'), ('LAX', 'ATL'), ('FLO', 'ATL'), ('ATL', 'JFK'), ('FLO', 'JFK'), ('DFW', 'HNL')])

# 绘制网络图
nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=nodelist1, alpha=0.6, node_color='blue', node_shape='p',
                       node_size=200, linewidths=2, label='1')
nx.draw_networkx_nodes(G, pos=nx.circular_layout(G), nodelist=nodelist2, alpha=0.6, node_color='red', node_shape='v',
                       node_size=220)
nx.draw_networkx_labels(G, pos=nx.circular_layout(G), font_sizet=15, font_color='k', font_family='SimHei', alpha=0.8)
plt.show()
