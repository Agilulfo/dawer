from datetime import date
from os.path import join

from mock import patch

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


@patch('dawer.image.move_files_to_dir')
def test_move_image(move):
    source_base_path = './a'
    destination_base_path = './b'
    image_name = '2016-05-12 15.32.00.jpg'

    image = Image(source_base_path, image_name)
    image.date = date(2016, 5, 12)
    image.move_to(destination_base_path)

    move.assert_called_with(
        [join(source_base_path, image_name)],
        join(destination_base_path, '2016/05/')
    )


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
    image_handler = ImagesHandler()
    image_handler.load_images_from_path(fake_dir)
    for image in image_handler.images:
        assert image.date == files[image.filename]
