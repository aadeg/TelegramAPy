from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class UserProfilePhotos:
    FIELD_PHOTOS = 'photos'
    FIELD_TOTALCOUNT = 'total_count'

    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def decode(j):
        try:
            photos = []
            for i in j[UserProfilePhotos.FIELD_PHOTOS]:
                for k in i:
                    photos.append(PhotoSize.deconde(k))

            obj = UserProfilePhotos(j[UserProfilePhotos.FIELD_TOTALCOUNT],
                                    photos)
        except KeyError:
            raise ObjectDecodingException("UserProfilePhotos", j)

        return obj
