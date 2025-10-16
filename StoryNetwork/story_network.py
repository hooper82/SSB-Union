import networkx as nx


class StoryNetwork:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_node(self, node_id):
        self.G.add_node(node_id)

    def add_edge(self, source_node_id, target_node_id):
        self.G.add_edge(source_node_id, target_node_id)

    def get_graph(self):
        return self.G
