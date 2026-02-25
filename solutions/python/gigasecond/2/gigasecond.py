from datetime import timedelta

def add(moment):
    GIGA_SECOND = 1_000_000_000
    return moment + timedelta(seconds=GIGA_SECOND)