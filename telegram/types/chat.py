from telegram.exception import ObjectDecodingException


class Chat:
    T_PRIVATE = 'private'
    T_GROUP = 'group'
    T_SUPERGROUP = 'supergroup'
    T_CHANNEL = 'channel'

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
            obj = Chat(j['id'], j['type'])
            if 'title' in j:
                obj.title = j['title']
            if 'username' in j:
                obj.username = j['username']
            if 'first_name' in j:
                obj.first_name = j['first_name']
            if 'last_name' in j:
                obj.last_name = j['last_name']
        except KeyError:
            raise ObjectDecodingException("Chat", j)

        return obj
