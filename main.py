import logging
import yaml
import os

import StoryCatalog




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    import pprint

    story_catalog = StoryCatalog.StoryCatalog()
    story_catalog.load_all_stories()

    for story in story_catalog.list_stories():
        pprint.pprint(story)
        print()

