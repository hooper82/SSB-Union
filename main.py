import logging
import argparse

from StoryCatalog import StoryCatalog
from StoryNetwork import StoryNetwork

import gravis as gv


NODE_SCALE_FACTOR = 200

logging.basicConfig(
    format='%(asctime)s %(module)s.%(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='graph.html', type=str, help="Output graph HTML file name")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    story_catalog = StoryCatalog()
    story_network = StoryNetwork()

    story_catalog.load_all_stories()
    story_network.add_all_stories(story_catalog)

    G = story_network.get_graph()

    # Gravis
    fig = gv.d3(
        G,

        node_hover_neighborhood=True,
        node_label_data_source='name',

        graph_height=1200,

        node_size_factor=1,
        use_node_size_normalization=True,
        node_size_normalization_min=5,
        node_size_normalization_max=100,


        # edge_size_data_source='weight',
        edge_curvature=0.3,

        use_collision_force=True,
        collision_force_radius=50,
        collision_force_strength=0.7,
    )
    fig.export_html(args.file, overwrite=True)