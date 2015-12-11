from ..exception import ObjectDecodingException


class Chat:
    T_PRIVATE = 'private'
    T_GROUP = 'group'
    T_SUPERGROUP = 'supergroup'
    T_CHANNEL = 'channel'

    FIELD_ID = 'id'
    FIELD_TYPE = 'type'
    FIELD_TITLE = 'title'
    FIELD_USERNAME = 'username'
    FIELD_FIRSTNAME = 'first_name'
    FIELD_LASTNAME = 'last_name'

    def __init__(self, _id, _type, title=None, username=None,
                 first_name=None, last_name=None):
        self.id = _id
        self.type = _type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def isPrivate(self):
        return self.type == Chat.T_PRIVATE

    def isGroup(self):
        return self.type == Chat.T_GROUP

    def isSupergroup(self):
        return self.type == Chat.T_SUPERGROUP

    def isChannel(self):
        return self.type == Chat.T_CHANNEL

    @staticmethod
    def decode(j):
        try:
            obj = Chat(j[Chat.FIELD_ID], j[Chat.FIELD_TYPE])
            if Chat.FIELD_TITLE in j:
                obj.title = j[Chat.FIELD_TITLE]
            if Chat.FIELD_USERNAME in j:
                obj.username = j[Chat.FIELD_USERNAME]
            if Chat.FIELD_FIRSTNAME in j:
                obj.first_name = j[Chat.FIELD_FIRSTNAME]
            if Chat.FIELD_LASTNAME in j:
                obj.last_name = j[Chat.FIELD_LASTNAME]
        except KeyError:
            raise ObjectDecodingException("Chat", j)

        return obj
