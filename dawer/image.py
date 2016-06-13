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

    def move_to_collection(self, collection_path):
        date_folder = '{year:04}/{month:02}/'.format(
            year=self.date.year, month=self.date.month
        )
        destination = join(collection_path, date_folder)
        source = join(self.directory, self.filename)
        move_files_to_dir([source], destination)
        self.directory = destination


class ImagesHandler:
    images = []

    def __init__(self, collection_path=None):
        if collection_path and not exists(collection_path):
            raise NotValidPath(collection_path)
        self.collection_path = collection_path
        self.dateparser = DateParser()

    def load_images_from_path(self, directory):
        if not exists(directory):
            raise NotValidPath(directory)
        filenames = get_images_in_folder(directory)
        for filename in filenames:
            image = Image(directory, filename)
            image.extract_date_from_name(self.dateparser)
            self.images.append(image)

    # TODO: test!
    def move_images_to_collection(self):
        for image in self.images:
            if image.date:
                image.move_to(self.collection_path)
