from datetime import datetime

def dates_validator(date1, date2):
    try:
        date_1 = datetime.strptime(str(date1), "%Y-%m-%d").date() if date1 else None
        date_2 = datetime.strptime(str(date2), "%Y-%m-%d").date() if date2 else None
    except (ValueError, TypeError):
        return False

    if date_1 is None or date_2 is None:
        return True

    return date_1 <= date_2