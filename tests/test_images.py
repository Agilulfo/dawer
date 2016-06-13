from datetime import date
from os.path import join

import pytest
from mock import MagicMock, patch

from dawer.exceptions import UnknownImageDate
from dawer.image import Image, ImagesHandler
from dawer.process import DateParser


def test_init_image():
    filename = '2016-05-12 15.32.00.jpg'
    directory = './images/'
    image = Image(directory, filename)
    assert image.filename == filename
    assert image.directory == directory


def test_extract_date_from_image_filename():
    filename = '2016-05-12 15.32.00.jpg'
    directory = './images/'
    image = Image(directory, filename)
    image.extract_date_from_name(DateParser())
    assert image.date == date(2016, 5, 12)


def test_extract_date_from_unformatted_filename():
    filename = 'myDog.jpg'
    directory = './images/'
    image = Image(directory, filename)
    image.extract_date_from_name(DateParser())
    assert image.date is None


def test_get_collection_sub_directory():
    source_base_path = './a'
    image_name = '2016-05-12.jpg'

    image = Image(source_base_path, image_name)
    sub_directory = image.get_collection_sub_directory()

    assert sub_directory is None

    image.date = date(2016, 5, 12)
    sub_directory = image.get_collection_sub_directory()

    assert sub_directory == '2016/05/'


@patch('dawer.image.move_files_to_dir')
def test_move_image(move):
    source_base_path = './a'
    collection_path = './b'
    image_name = '2016-05-12 15.32.00.jpg'

    image = Image(source_base_path, image_name)
    image.date = date(2016, 5, 12)
    image.move_to_collection(collection_path)

    source = join(source_base_path, image_name)
    destination = join(collection_path, '2016/05/')

    move.assert_called_with([source], destination)
    assert image.directory == destination


def test_move_image_with_unknown_date():
    source_base_path = './a'
    collection_path = './b'
    image_name = 'unknown.jpg'

    image = Image(source_base_path, image_name)
    with pytest.raises(UnknownImageDate):
        image.move_to_collection(collection_path)


@patch('dawer.image.get_images_in_folder')
def test_image_handler_load_images(img_list):
    fake_dir = './'
    files = {
        '2016-05-12 15.32.00.jpg': date(2016, 05, 12),
        '2016-05-12 15.32.02.png': date(2016, 05, 12),
        '2016-05-13.jpg': date(2016, 05, 13),
        'portrait.jpg': None,
    }
    img_list.return_value = files.keys()
    image_handler = ImagesHandler(fake_dir)
    image_handler.load_images_from_path(fake_dir)
    for image in image_handler.images:
        assert image.date == files[image.filename]


def test_move_images_to_collection():
    fake_dir = './'
    image_handler = ImagesHandler(fake_dir)

    image = Image(fake_dir, 'img.jpg')
    move_to_collection = MagicMock()
    image.move_to_collection = move_to_collection

    # image has no date
    image_handler.images = [image]
    image_handler.move_images_to_collection()

    move_to_collection.assert_not_called()

    # image has a date associated
    image.date = date.today()
    image_handler.move_images_to_collection()

    move_to_collection.assert_called_with(fake_dir)
