from ..exception import ObjectDecodingException


class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @staticmethod
    def decode(j):
        try:
            obj = Location(j['longitude'], j['latitude'])
        except KeyError:
            raise ObjectDecodingException("Location", j)

        return obj
