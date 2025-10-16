import logging
import yaml
import os

from StoryCatalog import StoryCatalog
from StoryNetwork import StoryNetwork

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



