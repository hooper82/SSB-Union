import logging
import yaml
import os

import networkx as nx
import matplotlib.pyplot as plt

from StoryCatalog import StoryCatalog
from StoryNetwork import StoryNetwork

import plotly.graph_objects as go

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

    story_network.remove_unconnected_nodes()
    G = story_network.get_graph()
    print("NODE COUNT: ", G.number_of_nodes())



    plt.figure(3, figsize=(14, 24))

    # Add labels and the color map
    nx.draw_shell(G, with_labels=True, font_size=10)
    plt.axis('off')
    axis = plt.gca()

    # A bit of spacing around the edge so labels won't overflow
    # Current settings give the current amount of stories a circular shape
    axis.set_xlim([1.2 * x for x in axis.get_xlim()])
    axis.set_ylim([1 * y for y in axis.get_ylim()])
    # plt.tight_layout() - commented out, just throws a warning
    plt.show()