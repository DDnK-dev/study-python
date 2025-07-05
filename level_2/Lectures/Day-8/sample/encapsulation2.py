class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if -90 <= lat_value <= 90:
            self._latitude = lat_value
        else:
            raise ValueError(f"유효하지 않는 위도 값: {lat_value}")

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if -180 <= long_value <= 180:
            self._longitude = long_value
        else:
            raise ValueError(f"유효하지 않은 경도 값: {long_value}")
    def __str__(self):
        return f"위도: {self._latitude}, 경도: {self._longitude}"


coord = Coordinate(37.5024625930912, 127.02862987558395)
print(coord)

cord2 = Coordinate(50.5024625930912, 230.02862987558395)
print(cord2)
