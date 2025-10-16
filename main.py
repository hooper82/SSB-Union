import logging
import yaml
import os

import networkx as nx
import matplotlib.pyplot as plt

from StoryCatalog import StoryCatalog
from StoryNetwork import StoryNetwork

import plotly.graph_objects as go
import gravis as gv


NODE_SCALE_FACTOR = 200

logging.basicConfig(
    format='%(asctime)s %(module)s.%(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    story_catalog = StoryCatalog()
    story_network = StoryNetwork()

    story_catalog.load_all_stories()

    for story_id in story_catalog.get_all_story_ids():
        story_network.add_node(story_id)

    for source_id, target_id in story_catalog.get_all_story_connections():
        story_network.add_edge(source_id, target_id)

    # story_network.add_node_attributes(story_catalog.stories)


    story_network.remove_unconnected_nodes()
    G = story_network.get_graph()
    print("NODE COUNT: ", G.number_of_nodes())

    for node_id in G.nodes():
        node = G.nodes[node_id]
        node['name'] = story_catalog.get_story(node_id)['name']
        node['author'] = story_catalog.get_story(node_id).get('author', 'Unknown')
        node['year'] = story_catalog.get_story(node_id).get('year', 'Unknown')

        edge_count = len(list(G.in_edges(node_id))) + len(list(G.out_edges(node_id)))
        node['size'] = edge_count * NODE_SCALE_FACTOR

    
    # Directed Graph
    # plt.figure(1, figsize=(16, 16))
    # nx.draw(G, pos=nx.spring_layout(G, gravity=0.1), labels=story_catalog.get_story_name_mapping(G.nodes()), with_labels=True, font_size=12)
    # plt.show()


    # Shell Layout
    # plt.figure(2, figsize=(16, 16))    # plt.figure(3, figsize=(16, 16))
    # nx.draw(G, pos=nx.shell_layout(G), labels=story_catalog.get_story_name_mapping(G.nodes()), with_labels=True, font_size=12)
    # plt.show()

    # Gravis
    fig = gv.d3(
        G,

        node_hover_neighborhood=True,
        node_label_data_source='name',

        graph_height=1200,

        use_node_size_normalization=True,
        node_size_normalization_max=30,
        edge_size_data_source='weight',
        edge_curvature=0.3,

        use_collision_force=True,
        collision_force_radius=50,
        collision_force_strength=0.7,
    )
    fig.export_html('graph.html', overwrite=True)