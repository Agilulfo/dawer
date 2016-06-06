from datetime import date

from dawer.process import date_from_text


def test_date_from_text():
    filename = '2016-05-12 15.32.00.jpg'
    result = date_from_text(filename)
    assert result == date(2016, 5, 12)
