from mock import patch

from dawer.filesystem import get_images_in_folder


def test_get_images_in_folder_return_list():
    result = get_images_in_folder('./')
    assert isinstance(result, list)


def test_get_images_in_folder_return_strings():
    results = get_images_in_folder('./')
    for result in results:
        assert isinstance(result, str)


@patch('dawer.filesystem.listdir')
def test_get_images_in_folder_return_only_images(listdir):
    listdir.return_value = [
        'image.jpg', 'audio.mp3', 'text.txt', 'directory'
    ]
    results = get_images_in_folder('./')
    assert results == ['image.jpg']
