from pyvis.network import Network


net = Network()
net.add_node(1, label="Node 1")  # node id = 1 and label = Node 1
net.add_node(2)  # node id and label = 2

nodes = ["a", "b", "c", "d"]
net.add_nodes(nodes)  # node ids and labels = ["a", "b", "c", "d"]
net.add_nodes("hello")  # node ids and labels = ["h", "e", "l", "o"]

net.add_nodes(["a", "b", "c"])
print(net.get_node("c"))  # {'id': 'c', 'label': 'c', 'shape': 'dot'}

net.add_node(0, label='a')
net.add_node(1, label='b')
net.add_edge(0, 1)
net.add_edge(0, 1, weight=.87)

net.toggle_physics(True)
net.show_buttons(filter_=['physics'])
net.show('demo1.html')
