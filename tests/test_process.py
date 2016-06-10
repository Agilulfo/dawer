from datetime import date

from dawer.process import (DateParser, extract_date_from_strings,
                           group_by_month, group_by_year)


def test_DateParser():
    filename = '2016-05-12 15.32.00.jpg'
    parser = DateParser()
    result = parser.get_date(filename)
    assert result == date(2016, 5, 12)


def test_DateParser_wrong():
    filename = "IMG-123.jpg"
    parser = DateParser()
    result = parser.get_date(filename)
    assert result is None


def test_assign_date_to_filenames():
    filenames = {
        '2016-05-12 15.32.00.jpg': date(2016, 05, 12),
        '2016-05-12 15.32.02.png': date(2016, 05, 12),
        '2016-05-13.jpg': date(2016, 05, 13),
        'portrait.jpg': None,
    }
    parser = DateParser()
    result, skipped = extract_date_from_strings(filenames.keys(), parser)
    for string, corresponding_date in result:
        assert filenames[string] == corresponding_date

    for filename in skipped:
        assert filenames[filename] is None


def test_group_by_year():
    dated_files = [
        ('0.jpg', date(2014, 05, 12)),
        ('1.png', date(2016, 05, 12)),
        ('2.jpeg', date(2015, 05, 13)),
        ('3.jpeg', date(2014, 05, 11)),
    ]
    result = group_by_year(dated_files)
    for file in dated_files:
        filename, time = file
        assert file in result[time.year]


def test_group_by_month():
    dated_files = [
        ('0.jpg', date(2014, 05, 12)),
        ('1.png', date(2015, 05, 12)),
        ('2.jpeg', date(2015, 05, 13)),
        ('3.jpeg', date(2014, 06, 11)),
    ]
    data_structure = group_by_month(dated_files)
    for file in dated_files:
        filename, time = file
        assert file in data_structure[time.year][time.month]
