from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class UserProfilePhotos:
    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def decode(j):
        try:
            photos = []
            for i in j['photos']:
                for k in i:
                    photos.append(PhotoSize.deconde(k))

            obj = UserProfilePhotos(j['total_count'], photos)
        except KeyError:
            raise ObjectDecodingException("UserProfilePhotos", j)

        return obj
