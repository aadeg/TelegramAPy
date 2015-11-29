import urllib2
import requests
import json
from datetime import datetime

from exception import TelegramException, ObjectDecodingException


class TelegramUser:
    def __init__(self, _id, first_name, last_name=None, username=None):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @staticmethod
    def decode(j):
        try:
            obj = TelegramUser(j['id'], j['first_name'])
            if 'last_name' in j:
                obj.last_name = j['last_name']
            if 'username' in j:
                obj.username = j['username']
        except KeyError:
            raise ObjectDecodingException("TelegramUser", j)

        return obj


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
    def decode(j):
        try:
            obj = TelegramChat(j['id'], j['type'])
            if 'title' in j:
                obj.title = j['title']
            if 'username' in j:
                obj.username = j['username']
            if 'first_name' in j:
                obj.first_name = j['first_name']
            if 'last_name' in j:
                obj.last_name = j['last_name']
        except KeyError:
            raise ObjectDecodingException("TelegramChat", j)

        return obj


class TelegramPhotoSize:
    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = TelegramPhotoSize(j['file_id'], j['width'], j['height'])
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramPhotoSize", j)

        return obj


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
    def decode(j):
        try:
            obj = TelegramAudio(j['file_id'], j['duration'])
            if 'performer' in j:
                obj.performer = j['performer']
            if 'title' in j:
                obj.title = j['title']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramAudio", j)

        return obj


class TelegramDocument:
    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = TelegramDocument(j['file_id'])
            if 'thumb' in j:
                obj.thumb = TelegramPhotoSize.deconde(j['thumb'])
            if 'file_name' in j:
                obj.file_name = j['file_name']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramDocument", j)

        return obj


class TelegramSticker:
    def __init__(self, file_id, width, height, thumb=None,
                 file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = TelegramDocument(j['file_id'])
            if 'thumb' in j:
                obj.thumb = TelegramPhotoSize.deconde(j['thumb'])
            if 'file_name' in j:
                obj.file_name = j['file_name']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramSticker", j)

        return obj


class TelegramVideo:
    def __init__(self, file_id, width, height, duration, thumb=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = TelegramVideo(j['file_id'], j['width'], j['height'],
                                j['duration'])
            if 'thumb' in j:
                obj.thumb = TelegramPhotoSize.deconde(j['thumb'])
            if 'file_name' in j:
                obj.file_name = j['file_name']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramVideo", j)

        return obj


class TelegramVoice:
    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = TelegramVoice(j['file_id'], j['duration'])
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("TelegramVoice", j)

        return obj


class TelegramContact:
    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    @staticmethod
    def decode(j):
        try:
            obj = TelegramContact(j['phone_number'], j['first_name'])
            if 'last_name' in j:
                obj.last_name = j['last_name']
            if 'user_id' in j:
                obj.user_id = j['user_id']
        except KeyError:
            raise ObjectDecodingException("TelegramContact", j)

        return obj


class TelegramLocation:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @staticmethod
    def decode(j):
        try:
            obj = TelegramLocation(j['longitude'], j['latitude'])
        except KeyError:
            raise ObjectDecodingException("TelegramLocation", j)

        return obj


class TelegramUserProfilePhotos:
    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def decode(j):
        try:
            photos = []
            for i in j['photos']:
                for k in i:
                    photos.append(TelegramPhotoSize.deconde(k))

            obj = TelegramUserProfilePhotos(j['total_count'], photos)
        except KeyError:
            raise ObjectDecodingException("TelegramUserProfilePhotos", j)

        return obj


class TelegramFile:
    def __init__(self, file_id, file_size=None, file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def decode(j):
        try:
            obj = TelegramFile(j['file_id'])
            if 'file_size' in j:
                obj.file_size = j['file_size']
            if 'file_path' in j:
                obj.file_path = j['file_path']
        except KeyError:
            raise ObjectDecodingException("TelegramFile", j)

        return obj


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
    def decode(j):
        try:
            chat = TelegramChat.decode(j['chat'])
            date = datetime.fromtimestamp(j['date'])
            obj = TelegramMessage(j['message_id'], date, chat)
            if 'from' in j:
                obj.from_ = TelegramUser.decode(j['from'])
            if 'forward_from' in j:
                obj.forward_from = TelegramUser.decode(j['forward_from'])
            if 'forward_date' in j:
                obj.forward_date = datetime.fromtimestamp(
                    j['forward_date'])
            if 'reply_to_message' in j:
                obj.reply_to_message = TelegramMessage.decode(
                    j['reply_to_message'])
            if 'text' in j:
                obj.text = j['text']
            if 'audio' in j:
                obj.audio = TelegramAudio.decode(j['audio'])
            if 'document' in j:
                obj.document = TelegramDocument.decode(j['document'])
            if 'photo' in j:
                obj.photo = []
                for el in j['photo']:
                    obj.photo.append(TelegramPhotoSize.decode(el))
            if 'sticker' in j:
                obj.sticker = TelegramSticker.decode(j['sticker'])
            if 'video' in j:
                obj.video = TelegramVideo.decode(j['video'])
            if 'voice' in j:
                obj.voice = TelegramVoice.decode(j['voice'])
            if 'caption' in j:
                obj.caption = j['caption']
            if 'contact' in j:
                obj.contact = TelegramContact.decode(j['contact'])
            if 'location' in j:
                obj.location = TelegramLocation.decode(j['location'])
            if 'new_chat_partecipant' in j:
                obj.new_chat_partecipant = TelegramUser.decode(
                    j['new_chat_partecipant'])
            if 'left_chat_partecipant' in j:
                obj.left_chat_partecipant = TelegramUser.decode(
                    j['left_chat_partecipant'])
            if 'new_chat_title' in j:
                obj.new_chat_title = j['new_chat_title']
            if 'new_chat_photo' in j:
                obj.new_chat_photo = []
                for el in j['new_chat_photo']:
                    obj.new_chat_photo.append(TelegramPhotoSize.decode(el))
            if 'delete_chat_photo' in j:
                obj.delete_chat_photo = j['delete_chat_photo']
            if 'group_chat_created' in j:
                obj.group_chat_created = j['group_chat_created']
            if 'supergroup_chat_created' in j:
                obj.supergroup_chat_created = j['supergroup_chat_created']
            if 'channel_chat_created' in j:
                obj.channel_chat_created = j['channel_chat_created']
            if 'migrate_to_chat_id' in j:
                obj.migrate_to_chat_id = j['migrate_to_chat_id']
            if 'migrate_from_chat_id' in j:
                obj.migrate_from_chat_id = j['migrate_from_chat_id']
        except KeyError:
            raise ObjectDecodingException("TelegramMessage", j)

        return obj


class TelegramUpdate:
    def __init__(self, update_id, message=None):
        self.update_id = update_id
        self.message = message

    @staticmethod
    def decode(j):
        try:
            obj = TelegramUpdate(j['update_id'])
            if 'message' in j:
                obj.message = TelegramMessage.decode(j['message'])
        except KeyError:
            raise ObjectDecodingException("TelegramUpdate", j)

        return obj


class TelegramAPI:
    TELEGRAM_URL = "https://api.telegram.org/"

    def __init__(self, token):
        self._token = token

    def getMe(self):
        j = TelegramAPI._sendRequest(self._getUrl('getMe'))
        return TelegramUser.decode(j)

    def sendMessage(self, chat_id, text):
        j = TelegramAPI._sendRequest(self._getUrl('sendMessage'),
                                     chat_id=chat_id, text=text)
        return TelegramMessage.decode(j)

    def forwardMessage(self, chat_id, from_chat_id, message_id):
        j = TelegramAPI._sendRequest(self._getUrl('forwardMessage'),
                                     chat_id=chat_id,
                                     from_chat_id=from_chat_id,
                                     message_id=message_id)
        return TelegramMessage.decode(j)

    def sendPhoto(self, chat_id, photo, is_path=True, caption=None,
                  reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'photo': open(photo, 'rb')}
        else:
            files = {'photo': photo}
        j = TelegramAPI._sendRequest(self._getUrl('sendPhoto'),
                                     chat_id=chat_id, files=files,
                                     is_file_path=is_path, caption=caption,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)

        return TelegramMessage.decode(j)

    def sendAudio(self, chat_id, audio, is_path=True, duration=None,
                  performer=None, title=None,
                  reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'audio': open(audio, 'rb')}
        else:
            files = {'audio': audio}
        j = TelegramAPI._sendRequest(self._getUrl('sendAudio'),
                                     chat_id=chat_id, files=files,
                                     is_file_path=is_path, duration=duration,
                                     performer=performer, title=title,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def sendDocument(self, chat_id, document, is_path=True,
                     reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'document': open(document, 'rb')}
        else:
            files = {'document': document}
        j = TelegramAPI._sendRequest(self._getUrl('sendDocument'),
                                     files=files, is_file_path=is_path,
                                     chat_id=chat_id,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def sendSticker(self, chat_id, sticker, is_path=True,
                    reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'sticker': open(sticker, 'rb')}
        else:
            files = {'sticker': sticker}
        j = TelegramAPI._sendRequest(self._getUrl('sendSticker'),
                                     files=files, is_file_path=is_path,
                                     chat_id=chat_id,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def sendVideo(self, chat_id, video, is_path=True, duration=None,
                  caption=None, reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'video': open(video, 'rb')}
        else:
            files = {'video': video}
        j = TelegramAPI._sendRequest(self._getUrl('sendVideo'),
                                     files=files, is_file_path=is_path,
                                     chat_id=chat_id, duration=duration,
                                     caption=caption,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def sendVoice(self, chat_id, voice, is_path=True, duration=None,
                  reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'voice': open(voice, 'rb')}
        else:
            files = {'voice': voice}
        j = TelegramAPI._sendRequest(self._getUrl('sendVoice'),
                                     files=files, is_file_path=is_path,
                                     chat_id=chat_id, duration=duration,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def sendLcation(self, chat_id, latitude, longitude,
                    reply_to_message_id=None, replay_markup=None):
        j = TelegramAPI._sendRequest(self._getUrl('sendLcation'),
                                     chat_id=chat_id, latitude=latitude,
                                     longitude=longitude,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return TelegramMessage.decode(j)

    def getUpdates(self, offset=None, limit=None, timeout=None):
        j = TelegramAPI._sendRequest(self._getUrl('getUpdates'),
                                     offset=offset, limit=limit,
                                     timeout=timeout)
        ris = []
        for el in j:
            ris.append(TelegramUpdate.decode(el))
        return ris

    def _getUrl(self, method):
        url = "%sbot%s/%s?" % (TelegramAPI.TELEGRAM_URL, self._token, method)
        return url

    @staticmethod
    def _sendRequest(url, files={}, is_file_path=True, **kwargs):
        if is_file_path:
            req = requests.post(url, files=files, data=kwargs)
        else:
            kwargs.update(files)
            req = requests.post(url, data=kwargs)
        j = req.json()

        if 'ok' not in j or not j['ok']:
            raise TelegramException(j)

        return j['result']
