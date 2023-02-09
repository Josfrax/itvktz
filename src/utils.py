"""
This module contain functions utils for App.
"""


from datetime import date


def Daysleft(date_close) -> int:
    """
    Calculate remaining days to completation.
    return:
        days:int
    """
    today = date.today()
    if date_close > today:
        delta = date_close - today
        return delta.days
    else:
        return 0