import re
from datetime import date

from .constants import DEFAULT_DATE_REGEXP


class DateParser:
    def __init__(self, regexp_string=DEFAULT_DATE_REGEXP):
        self.regexp = re.compile(regexp_string)

    def get_date(self, text):
        match = self.regexp.match(text)
        if match:
            year = int(match.group('year'))
            month = int(match.group('month'))
            day = int(match.group('day'))
            return date(year, month, day)
        return None


def extract_date_from_strings(strings, dateparser):
    results = []
    skipped = []
    for string in strings:
        date = dateparser.get_date(string)
        if date:
            results.append((string, date))
        else:
            skipped.append(string)
    return results, skipped


def group_by_year(dated_files):
    result = {}
    for filename, file_date in dated_files:
        year = file_date.year
        list_of_dates = result.get(year, [])
        list_of_dates.append((filename, file_date))
        result[year] = list_of_dates
    return result


def group_by_month(dated_files):
    result = group_by_year(dated_files)
    years = result.keys()
    for year in years:
        files = result[year]
        months = {}
        for filename, file_date in files:
            month = file_date.month
            list_of_dates = months.get(month, [])
            list_of_dates.append((filename, file_date))
            months[month] = list_of_dates
        result[year] = months
    return result
