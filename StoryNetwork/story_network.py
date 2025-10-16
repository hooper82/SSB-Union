import networkx as nx
import logging


class StoryNetwork:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_node(self, node_id):
        self.G.add_node(node_id)

    def add_edge(self, source_node_id, target_node_id):
        self.G.add_edge(source_node_id, target_node_id)

    def remove_unconnected_nodes(self):
        pre_count = self.G.number_of_nodes()
        self.G.remove_nodes_from(list(nx.isolates(self.G)))
        post_count = self.G.number_of_nodes()
        logging.info(f"Removed {pre_count - post_count} unconnected nodes.")

    def get_graph(self):
        return self.G
