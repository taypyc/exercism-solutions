class SpaceAge:
    MERCURY_PERIOD = 0.2408467
    VENUS_PERIOD = 0.61519726
    EARTH_PERIOD = 1.0
    MARS_PERIOD = 1.8808158
    JUPITER_PERIOD = 11.862615
    SATURN_PERIOD = 29.447498
    URANUS_PERIOD = 84.016846
    NEPTUNE_PERIOD = 164.79132
    EARTH_YEAR_SECONDS = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def _calculate_age(self, orbital_period):
        return round(self.seconds / (self.EARTH_YEAR_SECONDS * orbital_period), 2)

    def on_mercury(self):
        return self._calculate_age(self.MERCURY_PERIOD)

    def on_venus(self):
        return self._calculate_age(self.VENUS_PERIOD)

    def on_earth(self):
        return self._calculate_age(self.EARTH_PERIOD)

    def on_mars(self):
        return self._calculate_age(self.MARS_PERIOD)

    def on_jupiter(self):
        return self._calculate_age(self.JUPITER_PERIOD)

    def on_saturn(self):
        return self._calculate_age(self.SATURN_PERIOD)

    def on_uranus(self):
        return self._calculate_age(self.URANUS_PERIOD)

    def on_neptune(self):
        return self._calculate_age(self.NEPTUNE_PERIOD)