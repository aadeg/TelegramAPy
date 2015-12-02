import requests

from exception import TelegramException
from types import Message, User, UserProfilePhotos, File, Update


class TelegramAPI:
    TELEGRAM_URL = "https://api.telegram.org/"

    def __init__(self, token):
        self._token = token
        self._url = "%sbot%s/" % (TelegramAPI.TELEGRAM_URL, self._token)

    def getMe(self):
        j = TelegramAPI._sendRequest(self._getUrl('getMe'))
        return User.decode(j)

    def sendMessage(self, chat_id, text, parse_mode=None,
                    disable_web_page_preview=None, reply_to_message_id=None,
                    reply_markup=None):
        rep_markup = reply_markup.encode() if reply_markup else None
        j = TelegramAPI._sendRequest(
                self._getUrl('sendMessage'), chat_id=chat_id, text=text,
                parse_mode=parse_mode, reply_to_message_id=reply_to_message_id,
                disable_web_page_preview=disable_web_page_preview,
                reply_markup=rep_markup)

        return Message.decode(j)

    def forwardMessage(self, chat_id, from_chat_id, message_id):
        j = TelegramAPI._sendRequest(self._getUrl('forwardMessage'),
                                     chat_id=chat_id,
                                     from_chat_id=from_chat_id,
                                     message_id=message_id)
        return Message.decode(j)

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

        return Message.decode(j)

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
        return Message.decode(j)

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
        return Message.decode(j)

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
        return Message.decode(j)

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
        return Message.decode(j)

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
        return Message.decode(j)

    def sendLcation(self, chat_id, latitude, longitude,
                    reply_to_message_id=None, replay_markup=None):
        j = TelegramAPI._sendRequest(self._getUrl('sendLcation'),
                                     chat_id=chat_id, latitude=latitude,
                                     longitude=longitude,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendChatAction(self, chat_id, action):
        TelegramAPI._sendRequest(self._getUrl('sendChatAction'),
                                 chat_id=chat_id, action=action)

    def getUserProfilePhotos(self, user_id, offset=None, limit=None):
        j = TelegramAPI._sendRequest(self._getUrl('getUserProfilePhotos'),
                                     user_id=user_id, offset=offset,
                                     limit=limit)
        return UserProfilePhotos.decode(j)

    def getFile(self, file_id):
        j = TelegramAPI._sendRequest(self._getUrl('getFile'), file_id=file_id)
        return File.decode(j)

    def getUpdates(self, offset=None, limit=None, timeout=None):
        j = TelegramAPI._sendRequest(self._getUrl('getUpdates'),
                                     offset=offset, limit=limit,
                                     timeout=timeout)
        ris = []
        for el in j:
            ris.append(Update.decode(el))
        return ris

    def setWebhook(self, url=None, certificate_path=None):
        if certificate_path:
            files = {'certificate': open(certificate_path, 'rb')}
        else:
            files = {}
        TelegramAPI._sendRequest(self._getUrl('setWebhook'), files=files,
                                 url=url)

    def _getUrl(self, method):
        return self._url + method

    @staticmethod
    def _sendRequest(url, files={}, is_file_path=True, **kwargs):
        data = {}
        for key, value in kwargs.iteritems():
            if value:
                data[key] = value

        if is_file_path:
            req = requests.post(url, files=files, data=data)
        else:
            kwargs.update(files)
            req = requests.post(url, data=data)
        j = req.json()

        if 'ok' not in j or not j['ok']:
            raise TelegramException(j)

        return j['result']
