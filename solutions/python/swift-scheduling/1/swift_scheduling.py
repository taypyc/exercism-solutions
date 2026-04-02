from datetime import datetime, timedelta

def delivery_date(meeting_start_str, description):
    meeting_start = datetime.fromisoformat(meeting_start_str)
    
    year, month, day = meeting_start.year, meeting_start.month, meeting_start.day
    weekday = meeting_start.weekday()
    hour = meeting_start.hour

    result = None

    if description == "NOW":
        result = meeting_start + timedelta(hours=2)

    elif description == "ASAP":
        if hour < 13:
            result = datetime(year, month, day, 17, 0)
        else:
            tomorrow = meeting_start + timedelta(days=1)
            result = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 13, 0)

    elif description == "EOW":
        if weekday <= 2: 
            days_to_fri = 4 - weekday
            target = meeting_start + timedelta(days=days_to_fri)
            result = datetime(target.year, target.month, target.day, 17, 0)
        else:
            days_to_sun = 6 - weekday
            target = meeting_start + timedelta(days=days_to_sun)
            result = datetime(target.year, target.month, target.day, 20, 0)

    elif description.endswith("M"):
        n_month = int(description[:-1])
        target_year = year if month < n_month else year + 1
        result = get_first_workday(target_year, n_month)

    elif description.startswith("Q"):
        n_quarter = int(description[1:])
        last_month_of_q = n_quarter * 3
        current_q = (month - 1) // 3 + 1
        target_year = year if current_q <= n_quarter else year + 1
        result = get_last_workday(target_year, last_month_of_q)

    return result.isoformat() if result else None

def get_first_workday(year, month):
    date = datetime(year, month, 1, 8, 0)
    while date.weekday() > 4:
        date += timedelta(days=1)
    return date

def get_last_workday(year, month):
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    date = (next_month - timedelta(days=1)).replace(hour=8, minute=0, second=0)
    while date.weekday() > 4:
        date -= timedelta(days=1)
    return date