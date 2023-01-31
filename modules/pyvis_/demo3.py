"""
官方文档：https://pyvis.readthedocs.io/en/latest/
"""


from pyvis.network import Network
import networkx as nx

# g = Network(height=800, width=800, notebook=False)
g = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", filter_menu=True)
g.toggle_hide_edges_on_drag(True)
g.barnes_hut()  # use this particular physic solver
g.from_nx(nx.davis_southern_women_graph())  # just show a networkx graph
# g.show_buttons(filter_=['physics'])
g.show("demo3.html")
