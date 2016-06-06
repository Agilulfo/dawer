import re
from datetime import date

from .constants import DEFAULT_FILENAME_REGEXP


def date_from_text(filename):
    # TODO: use global regexp
    regexp = re.compile(DEFAULT_FILENAME_REGEXP)
    match = regexp.match(filename)
    year = int(match.group('year'))
    month = int(match.group('month'))
    day = int(match.group('day'))
    return date(year, month, day)
