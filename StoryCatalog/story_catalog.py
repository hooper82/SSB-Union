import yaml
import os
import logging


class StoryCatalog:
    def __init__(self, story_directory='data'):
        self._story_directory = story_directory
        self.stories = {}

    def _load_story_file(self, filename: str) -> dict:
        with open(filename, 'r') as file:
            story_data = yaml.safe_load(file)
            logging.debug(f"Loaded story: {story_data.get('name', 'Unknown')} from {filename}")
            return story_data

    def _find_story_files(self):
        print(os.path.exists(self._story_directory))
        for file in os.listdir(self._story_directory):
            if not file.endswith('.yaml'):
                continue

            yield os.path.join(self._story_directory, file)

    def load_all_stories(self):
        for story_file in self._find_story_files():
            story = self._load_story_file(story_file)
            self.add_story(story)

        logging.info(f"Total stories loaded: {len(self.stories)}")

    def add_story(self, story):
        self.stories[story['id']] = story

    def get_story(self, story_id):
        return self.stories.get(story_id)

    def list_stories(self):
        return list(self.stories.values())
    
    def get_all_story_ids(self):
        return list(self.stories.keys())
    
    def get_all_story_connections(self):
        for story in self.stories.values():
            for connection in story.get('connections', []):
                yield (story['id'], connection)