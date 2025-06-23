from datetime import datetime

def parse_date_safe(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

def dates_validator(date1, date2):
    if date1 == None or date2 == None or date1 == '' or date2 == '':
        return True
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return d1 <= d2
    except ValueError:
        return False
