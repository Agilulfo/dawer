import re
from os import listdir

from .constants import IMAGE_EXTENTIONS


def get_images_in_folder(path):
    regexp = re.compile('.+\.(?:' + '|'.join(IMAGE_EXTENTIONS) + ')$')
    files = listdir(path)
    image_files = [f for f in files if regexp.match(f)]
    return image_files
