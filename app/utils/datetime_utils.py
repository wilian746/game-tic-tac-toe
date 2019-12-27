from datetime import datetime

import dateutil.parser
import pytz


class DatetimeFormat:
    BRAZILIAN_DATE = "%d/%m/%Y"
    BRAZILIAN_DATE_TIME = "%d/%m/%Y %H:%M:%S"
    ENGLISH_DATE = "%Y-%M-%D"
    ENGLISH_DATE_TIME = "%Y-%M-%D %H:%M:%S"
    ENGLISH_DATE_TIME_ISO = "%Y-%M-%DT%H:%M:%S"


def format_datetime(date, date_format_str=DatetimeFormat.BRAZILIAN_DATE_TIME):
    try:
        date_time = dateutil.parser.parse(date)
        date_time_str = date_time.strftime(date_format_str)
    except ValueError:
        date_time_str = date
    return date_time_str


def format_the_date_with_month_name(date_time: str):
    end_time = dateutil.parser.parse(date_time)
    months = [
        "Unknown",
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    return end_time.strftime(
        "%d de {0} de %Y - %H:%M:%S".format(months[end_time.month])
    )


def get_datetime(timezone: str = "America/Sao_Paulo") -> datetime:
    """
    Captures the datetime of a given timezone
    """
    return datetime.now(tz=pytz.timezone(timezone))


def convert_to_timezone(
    date, timezone: str = "UTC", timezone_date: str = "UTC"
) -> datetime:
    """
    Converts a date to a given timezone
    :param date: Date for conversion
    :param timezone: Timezone to be converted
    :param timezone_date: Timezone name of the entered date.
    :return: datetime
    """
    if not isinstance(date, datetime):
        date = dateutil.parser.parse(date)

    if date.tzinfo is None:
        date = pytz.timezone(timezone_date).localize(date, is_dst=False)

    timezone = pytz.timezone(timezone)
    date = date.astimezone(timezone)
    return date
