import urllib2
import json
from datetime import datetime


class TelegramUser:
    def __init__(self, _id, first_name, last_name, username):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @staticmethod
    def fromJSON(j):
        user = TelegramUser(j['id'], j['first_name'])
        if 'last_name' in j:
            user.last_name = j['last_name']
        if 'username' in j:
            user.username = j['username']


class TelegramChat:
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
        return self.type == TelegramChat.T_PRIVATE

    def isGroup(self):
        return self.type == TelegramChat.T_GROUP

    def isSupergroup(self):
        return self.type == TelegramChat.T_SUPERGROUP

    def isChannel(self):
        return self.type == TelegramChat.T_CHANNEL

    @staticmethod
    def fromJSON(j):
        chat = TelegramChat(j['id'], j['type'])
        if 'title' in j:
            chat.title = j['title']
        if 'username' in j:
            chat.username = j['username']
        if 'first_name' in j:
            chat.first_name = j['first_name']
        if 'last_name' in j:
            chat.last_name = j['last_name']


class TelegramPhotoSize:
    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def fromJSON(j):
        ps = TelegramPhotoSize(j['file_id'], j['width'], j['height'])
        if 'file_size' in j:
            ps.file_size = j['file_size']


class TelegramAudio:
    def __init__(self, file_id, duration, performer=None, title=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def fromJSON(j):
        audio = TelegramAudio(j['file_id'], j['duration'])
        if 'performer' in j:
            audio.performer = j['performer']
        if 'title' in j:
            audio.title = j['title']
        if 'mime_type' in j:
            audio.mime_type = j['mime_type']
        if 'file_size' in j:
            audio.file_size = j['file_size']


class TelegramDocument:
    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def fromJSON(j):
        doc = TelegramDocument(j['file_id'])
        if 'thumb' in j:
            doc.thumb = j['thumb']
        if 'file_name' in j:
            doc.file_name = j['file_name']
        if 'mime_type' in j:
            doc.mime_type = j['mime_type']
        if 'file_size' in j:
            doc.file_size = j['file_size']

class TelegramMessage:
    def __init__(self, message_id, date, chat, from_=None, forward_from=None,
                 forward_date=None, reply_to_message=None, text=None,
                 audio=None, document=None, photo=None, sticker=None,
                 video=None, voice=None, caption=None, contact=None,
                 location=None, new_chat_partecipant=None,
                 left_chat_partecipant=None, new_chat_title=None,
                 new_chat_photo=None, delete_chat_photo=None,
                 group_chat_created=None, supergroup_chat_created=None,
                 channel_chat_created=None, migrate_to_chat_id=None,
                 migrate_from_chat_id=None):

        self.message_id = message_id
        self.date = date
        self.chat = chat
        self.from_ = from_
        self.forward_from = forward_from
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.text = text
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.caption = caption
        self.contact = contact
        self.location = location
        self.new_chat_partecipant = new_chat_partecipant
        self.left_chat_partecipant = left_chat_partecipant
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id

        @staticmethod
        def fromJSON(j):
            chat = TelegramChat.fromJSON(j['chat'])
            date = datetime.fromtimestamp(j['date'])
            msg = TelegramMessage(j['message_id'], date, chat)
            if 'from' in j:
                msg.from_ = TelegramUser.fromJSON(j['from'])
            if 'forward_from' in j:
                msg.forward_from = TelegramUser.fromJSON(j['forward_from'])
            if 'forward_date' in j:
                msg.forward_date = datetime.fromtimestamp(j['forward_date'])
            if 'reply_to_message' in j:
                msg.reply_to_message = TelegramMessage.fromJSON(j['reply_to_message'])
            if 'text' in j:
                msg.text = j['text']
            if 'audio' in j:
                msg.audio = TelegramAudio.fromJSON(j['audio'])
            if 'document' in j:
                msg.document = TelegramDocument.fromJSON(j['document'])
            if 'photo' in j:
                msg.photo = []
                for el in j['photo']:
                    msg.photo.append(TelegramPhotoSize.fromJSON(el))
            if 'sticker' in j:
                msg.sticker = TelegramSticker.fromJSON(j['sticker'])
            if 'video' in j:
                msg.video = TelegramVideo.fromJSON(j['video'])
            if 'voice' in j:
                msg.voice = TelgramVoice.fromJSON(j['voice'])
            if 'caption' in j:
                msg.caption = j['caption']
            if 'contact' in j:
                msg.contact = TelegramContact.fromJSON(j['contact'])
            if 'location' in j:
                msg.location = TelegramLocation.fromJSON(j['location'])
            if 'new_chat_partecipant' in j:
                msg.new_chat_partecipant = TelegramUser.fromJSON(j['new_chat_partecipant'])
            if 'left_chat_partecipant' in j:
                msg.left_chat_partecipant = TelegramUser.fromJSON(j['left_chat_partecipant'])
            if 'new_chat_title' in j:
                msg.new_chat_title = j['new_chat_title']
            if 'new_chat_photo' in j:
                msg.new_chat_photo = []
                for el in j['new_chat_photo']:
                    msg.new_chat_photo.append(TelegramPhotoSize.fromJSON(el))
            if 'delete_chat_photo' in j:
                msg.delete_chat_photo = j['delete_chat_photo']
            if 'group_chat_created' in j:
                msg.group_chat_created = j['group_chat_created']
            if 'supergroup_chat_created' in j:
                msg.supergroup_chat_created = j['supergroup_chat_created']
            if 'channel_chat_created' in j:
                msg.channel_chat_created = j['channel_chat_created']
            if 'migrate_to_chat_id' in j:
                msg.migrate_to_chat_id = j['migrate_to_chat_id']
            if 'migrate_from_chat_id' in j:
                msg.migrate_from_chat_id = j['migrate_from_chat_id']



class TelegramException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return repr(self.info)


class TelegramAPI:
    TELEGRAM_URL = "https://api.telegram.org/"

    def __init__(self, token):
        self._token = token

    def getMe(self):
        json = TelegramAPI._sendRequest(self._getUrl('getMe'))
        return TelegramUser.fromJSON(json)

    def sendMessage(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        return TelegramAPI._sendRequest(self._getUrl('sendMessage', params))

    def _getUrl(self, method, params={}):
        url = "%sbot%s/%s?" % (TelegramAPI.TELEGRAM_URL, self._token, method)
        for key, value in params.iteritems():
            url += "%s=%s&" % (key, value)
        return url[:-1]

    @staticmethod
    def _sendRequest(url):
        req = urllib2.urlopen(url)
        j = json.loads(req.read())

        if 'ok' not in j or not j['ok']:
            raise TelegramException(j)
