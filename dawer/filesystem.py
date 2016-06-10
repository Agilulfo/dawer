import re
from os import listdir, makedirs
from os.path import exists
from shutil import move

from .constants import IMAGE_EXTENTIONS


def get_images_in_folder(path):
    regexp = re.compile('.+\.(?:' + '|'.join(IMAGE_EXTENTIONS) + ')$')
    files = listdir(path)
    image_files = [f for f in files if regexp.match(f)]
    return image_files


# TODO: add test?
def move_files_to_dir(files, directory):
    if not exists(directory):
        makedirs(directory)
    for f in files:
        move(f, directory)
