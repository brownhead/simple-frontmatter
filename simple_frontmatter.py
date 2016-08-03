import shutil

import yaml

DEFAULT_FRONT_MATTER_END = u"\n...\n"


def loads(file_contents, front_matter_end=DEFAULT_FRONT_MATTER_END):
    end = file_contents.find(front_matter_end)
    if end == -1:
        return (None, file_contents)

    return (yaml.load(file_contents[:end]),
            file_contents[end + len(front_matter_end):])


def load(file_obj, front_matter_end=DEFAULT_FRONT_MATTER_END):
	return loads(file_obj.read())
