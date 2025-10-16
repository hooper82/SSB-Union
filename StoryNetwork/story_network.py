import networkx as nx
import logging

NODE_SCALE_FACTOR = 10

COLOR_HIATUS = "#808080"
COLOR_ONGOING = "#009600"
COLOR_COMPLETED = "#000096"
COLOR_UNKNOWN = "#0a0a0a"


def _parse_link(link):
    if link.startswith('http'):
        return f"\n<a href='{link}'>Read Me!</a>"
    return str()

def _parse_color(status):
    status = status.lower()
    if status == 'hiatus':
        return COLOR_HIATUS
    elif status == 'ongoing':
        return COLOR_ONGOING
    elif status == 'completed':
        return COLOR_COMPLETED
    else:
        return COLOR_UNKNOWN

def create_node_description(story):
    title = story.get('name', 'Unknown')
    author = story.get('author', 'Unknown')
    link = story.get('link', None)
    active = story.get('status', 'Unknown')

    description = f"Title: <strong>{title}</strong>"
    description += f"\nAuthor: <strong>{author}</strong>"
    description += f"\nActive: {active}"
    description += _parse_link(link)

    return description


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


    def add_node_attributes(self, all_attributes):
        nx.set_node_attributes(self.G, all_attributes)


    def _add_all_nodes(self, story_catalog):
        for story_id in story_catalog.get_all_story_ids():
            self.add_node(story_id)
        logging.info(f"Added {self.G.number_of_nodes()} nodes to the story graph.")


    def _add_all_edges(self, story_catalog):
        for source_id, target_id in story_catalog.get_all_story_connections():
            self.add_edge(source_id, target_id)
        logging.info(f"Added {self.G.number_of_edges()} edges to the story graph.")


    def _add_node_attributes(self, story_catalog):
        for node_id in self.G.nodes():
            node = self.G.nodes[node_id]
            story = story_catalog.get_story(node_id)
            if story:
                node['name'] = story.get('name', 'Unknown')
                node['author'] = story.get('author', 'Unknown')

                node['click'] = create_node_description(story)

                edge_count = len(list(self.G.in_edges(node_id))) + len(list(self.G.out_edges(node_id)))
                node['size'] = edge_count * NODE_SCALE_FACTOR

                node['border_size'] = 0
                node['color'] = _parse_color(story.get('status', 'Unknown'))

                logging.debug(f"Node {node_id}: {node['name']} by {node['author']} ({node.get('year', 'Unknown')}) with {edge_count} connections")
            else:
                logging.warning(f"No story found for node ID: {node_id}")


    def add_all_stories(self, story_catalog):
        self._add_all_nodes(story_catalog)
        self._add_all_edges(story_catalog)
        self._add_node_attributes(story_catalog)
        # self.remove_unconnected_nodes()