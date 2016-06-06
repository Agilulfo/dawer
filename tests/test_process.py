from datetime import date

from dawer.process import date_from_text, dates_from_filenames


def test_date_from_text():
    filename = '2016-05-12 15.32.00.jpg'
    result = date_from_text(filename)
    assert result == date(2016, 5, 12)


def test_date_from_text_wrong():
    filename = "IMG-123.jpg"
    result = date_from_text(filename)
    assert result is None


def test_assign_date_to_filenames():
    filenames = {
        '2016-05-12 15.32.00.jpg': date(2016, 05, 12),
        '2016-05-12 15.32.02.png': date(2016, 05, 12),
        '2016-05-13.jpg': date(2016, 05, 13),
        'portrait.jpg': None,
    }
    result = dates_from_filenames(filenames.keys())
    for k, v in result.items():
        if v:
            assert result[k] == v
