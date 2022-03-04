import datetime
from typing import Iterable

def _convert_json_timestamp(
    timestamp_str: str,
    format: str = '%Y-%m-%dT%H:%M:%S%z',
    ) -> datetime.datetime:
    """Converts json timestamp to Pythons datetime object.

    Parameters
    ----------
    timestamp_str : str
        The timestamp string of json type
        
    format : str
         (Default value = '%Y-%m-%dT%H:%M:%S%z')
         The format to match the `timestamp_str` in order to create Python
         datetime object. 

    Returns
    -------
    datetime.datetime

    """
    if timestamp_str is not None:
        return datetime.datetime.strptime(
            timestamp_str,
            format,
        )
    else:
        return None

def convert_json_timestamp(
    timestamp_str: str,
    formats: Iterable[str] = None,
    ) -> datetime.datetime:
    """Creates Python datetime object form json timestamp.

    The function will try each format in `formats` in order to match the
    given `timestamp_str`. If a fomrat matches the datetime object wil be
    returned. If no format matches with the given `timestamp_str`, then
    ValueError will be raised.

    Parameters
    ----------
    timestamp_str : str
        The timestamp string of json type
        
    formats : Iterable[str]
         (Default value = None)
         An iterable of string which are the formats that will be tried.

    Returns
    -------
    datetime.datetime

    Raises
    -------
    ValueError
        When no format was matches this error will be raised.

    """
    if timestamp_str is None:
        return None
    if formats is None:
        formats = [
            '%Y-%m-%dT%H:%M:%S%z',
            '%Y-%m-%dT%H:%M:%S.%f%z',
            '%Y-%m-%dT%H:%M:%S%f%z',
        ]
    for format in formats:
        try:
            return _convert_json_timestamp(
                timestamp_str,
                format,
            )
        except ValueError:
            continue
    raise ValueError(
        f"time data '{timestamp_str}' does not "
        f"match fomrat {formats}"
    )


def convert_to_date(date_str: str, formats: list = None):
    if date_str is None:
        return None
    if formats is None:
        formats = [
            '%Y-%m-%d',
            ]
    for format in formats:
        try:
            return _convert_json_timestamp(
                date_str,
                format,
                ).date()
        except ValueError:
            continue
    raise ValueError(
        f"date data '{date_str}' does not "
        f"match fomrat in {formats}"
    )


def convert_to_bool(variable: str = None):
    """converts variable to boolean.

    It retruns None if the variable is not True or False or true or false.

    Parameters
    ----------
    variable : str

    Returns
    -------
    bool

    """
    if bool(variable) is not None:
        return bool(variable)
    else:
        return None