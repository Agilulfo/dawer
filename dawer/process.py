import re
from datetime import date

from .constants import DEFAULT_DATE_REGEXP


def date_from_text(text):
    # TODO: use global regexp
    regexp = re.compile(DEFAULT_DATE_REGEXP)
    match = regexp.match(text)
    if match:
        year = int(match.group('year'))
        month = int(match.group('month'))
        day = int(match.group('day'))
        return date(year, month, day)
    return None


def dates_from_filenames(filenames):
    results = {}
    for filename in filenames:
        date = date_from_text(filename)
        if date:
            results[filename] = date
    return results
