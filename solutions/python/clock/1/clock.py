class Clock:
    def __init__(self, hour, minute):
        self.total_minutes = (hour * 60 + minute) % 1440

    def __repr__(self):
        h, m = divmod(self.total_minutes, 60)
        return f"Clock({h}, {m})"

    def __str__(self):
        h, m = divmod(self.total_minutes, 60)
        return f"{h:02d}:{m:02d}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)