from ..exception import ObjectDecodingException


class Location:
    FIELD_LONGITUDE = 'longitude'
    FIELD_LATITUDE = 'latitude'

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @staticmethod
    def decode(j):
        try:
            obj = Location(j[Location.FIELD_LONGITUDE],
                           j[Location.FIELD_LATITUDE])
        except KeyError:
            raise ObjectDecodingException("Location", j)

        return obj
