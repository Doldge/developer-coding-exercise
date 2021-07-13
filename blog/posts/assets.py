import os
import os.path
from typing import List, Dict


def get_template_directory() -> str:
    """Returns the template directory.

    FIXME: there must be a way to fetch this from the django.settings module?
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(directory, 'templates')


def get_asset_directory() -> str:
    directory = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
    return os.path.join(directory, 'assets/posts/')


def list_files(directory: str) -> List[str]:
    return os.listdir(directory)


def list_assets() -> List[str]:
    return list_files(get_asset_directory())


def read_post_from_file(filename: str) -> Dict[str, str]:
    post = dict()
    with open(filename, newline='\n') as f:
        header = False
        for line in f:
            if line.strip() == '===':
                # It's a marker for the header. Flip the header switch and continue
                header = not header
                continue
            if header is True:
                # We're inside the header.
                # structure is key: value
                key, _, value = line.partition(': ')
                post[key.lower()] = value.strip()
            else:
                if 'content' not in post.keys():
                    post['content'] = line
                else:
                    post['content'] += line
    return post


def get_all_posts() -> Dict[str, Dict[str, str]]:
    result_set = dict()
    asset_dir = get_asset_directory()
    post_list = list_files(asset_dir)
    for post in post_list:
        filename, _, ext = post.partition('.')
        result_set[filename] = read_post_from_file(asset_dir + post)
    return result_set
