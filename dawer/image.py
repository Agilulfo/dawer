from os.path import exists, join

from .exceptions import NotValidPath
from .filesystem import get_images_in_folder, move_files_to_dir
from .process import DateParser


class Image:
    date = None

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def extract_date_from_name(self, dateparser):
        self.date = dateparser.get_date(self.filename)

    def move_to(self, base_path):
        date_folder = '{year:04}/{month:02}/'.format(
            year=self.date.year, month=self.date.month
        )
        destination = join(base_path, date_folder)
        source = join(self.directory, self.filename)
        move_files_to_dir([source], destination)


class ImagesHandler:
    images = []

    def __init__(self, destination_path=None):
        if destination_path and not exists(destination_path):
            raise NotValidPath(destination_path)
        self.destination_path = destination_path
        self.dateparser = DateParser()

    def load_images_from_path(self, directory):
        if not exists(directory):
            raise NotValidPath(directory)
        filenames = get_images_in_folder(directory)
        for filename in filenames:
            image = Image(directory, filename)
            image.extract_date_from_name(self.dateparser)
            self.images.append(image)
