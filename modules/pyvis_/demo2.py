from pyvis.network import Network
import networkx as nx


g = Network()
g.add_nodes([1, 2, 3], value=[10, 100, 400],
            title=['I am node 1', 'node 2 here', 'and im node 3'],
            x=[21.4, 54.2, 11.2],
            y=[100.2, 23.54, 32.1],
            label=['NODE 1', 'NODE 2', 'NODE 3'],
            color=['#00ff1e', '#162347', '#dd4b39'])

nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)

nt = Network('500px', '500px')  # populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('demo2.html')
