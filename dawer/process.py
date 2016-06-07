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
    results = []
    for filename in filenames:
        date = date_from_text(filename)
        if date:
            results.append((filename, date))
    return results


def group_by_year(dated_files):
    result = {}
    for filename, date in dated_files:
        year = date.year
        list_of_dates = result.get(year, [])
        list_of_dates.append((filename, date))
        result[year] = list_of_dates
    return result


def group_by_month(dated_files):
    result = group_by_year(dated_files)
    years = result.keys()
    for year in years:
        files = result[year]
        months = {}
        for filename, date in files:
            month = date.month
            list_of_dates = months.get(month, [])
            list_of_dates.append((filename, date))
            months[month] = list_of_dates
        result[year] = months
    return result
