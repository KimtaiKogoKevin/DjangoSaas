import datetime

def timestamp_As_date_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)