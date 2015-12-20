'''
TelegramAPy
Copyright (C) 2015  Giove Andrea

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
import re
import requests

from .exception import TelegramException, InvalidTokenException
from .types import Message, User, UserProfilePhotos, File, Update


class TelegramAPy:
    TOKEN_REGEX = r'^[0-9]+\:[a-zA-Z0-9_\-]+$'
    TELEGRAM_URL = 'https://api.telegram.org/'

    METHOD_GETME = 'getMe'
    METHOD_SENDMESSAGE = 'sendMessage'
    METHOD_FORWARDMESSAGE = 'forwardMessage'
    METHOD_SENDPHOTO = 'sendPhoto'
    METHOD_SENDAUDIO = 'sendAudio'
    METHOD_SENDDOCUMENT = 'sendDocument'
    METHOD_SENDSTICKER = 'sendSticker'
    METHOD_SENDVIDEO = 'sendVideo'
    METHOD_SENDVOICE = 'sendVoice'
    METHOD_SENDLOCATION = 'sendLocation'
    METHOD_SENDCHATACTION = 'sendChatAction'
    METHOD_GETUSERPROFILEPHOTOS = 'getUserProfilePhotos'
    METHOD_GETFILE = 'getFile'
    METHOD_GETUPDATES = 'getUpdates'
    METHOD_SETWEBHOOK = 'setWebhook'

    MARKDOWN_MODE = "markdown"

    def __init__(self, token):
        if re.match(TelegramAPy.TOKEN_REGEX, token) is None:
            raise InvalidTokenException()

        self._token = token
        self._url = "%sbot%s/" % (TelegramAPy.TELEGRAM_URL, self._token)

    def getMe(self):
        j = TelegramAPy._sendRequest(self._getUrl('getMe'))
        return User.decode(j)

    def sendMessage(self, chat_id, text, parse_mode=None,
                    disable_web_page_preview=None, reply_to_message_id=None,
                    reply_markup=None):
        rep_markup = reply_markup.encode() if reply_markup else None
        j = TelegramAPy._sendRequest(
                self._getUrl(TelegramAPy.METHOD_SENDMESSAGE),
                chat_id=chat_id, text=text, parse_mode=parse_mode,
                reply_to_message_id=reply_to_message_id,
                disable_web_page_preview=disable_web_page_preview,
                reply_markup=rep_markup)

        return Message.decode(j)

    def forwardMessage(self, chat_id, from_chat_id, message_id):
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_FORWARDMESSAGE),
            chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
        return Message.decode(j)

    def sendPhoto(self, chat_id, photo, is_path=True, caption=None,
                  reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'photo': open(photo, 'rb')}
        else:
            files = {'photo': photo}
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SENDPHOTO),
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
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SENDAUDIO),
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
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDDOCUMENT),
            files=files, is_file_path=is_path, chat_id=chat_id,
            replay_markup=replay_markup,
            reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendSticker(self, chat_id, sticker, is_path=True,
                    reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'sticker': open(sticker, 'rb')}
        else:
            files = {'sticker': sticker}
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDSTICKER), files=files,
            is_file_path=is_path, chat_id=chat_id, replay_markup=replay_markup,
            reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendVideo(self, chat_id, video, is_path=True, duration=None,
                  caption=None, reply_to_message_id=None, replay_markup=None):
        if is_path:
            files = {'video': open(video, 'rb')}
        else:
            files = {'video': video}
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SENDVIDEO),
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
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SENDVOICE),
                                     files=files, is_file_path=is_path,
                                     chat_id=chat_id, duration=duration,
                                     replay_markup=replay_markup,
                                     reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendLocation(self, chat_id, latitude, longitude,
                    reply_to_message_id=None, replay_markup=None):
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDLOCATION), chat_id=chat_id,
            latitude=latitude, longitude=longitude, replay_markup=replay_markup,
            reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendChatAction(self, chat_id, action):
        TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDCHATACTION), chat_id=chat_id,
            action=action)

    def getUserProfilePhotos(self, user_id, offset=None, limit=None):
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_GETUSERPROFILEPHOTOS),
            user_id=user_id, offset=offset, limit=limit)
        return UserProfilePhotos.decode(j)

    def getFile(self, file_id):
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_GETFILE),
                                     file_id=file_id)
        return File.decode(j)

    def getUpdates(self, offset=None, limit=None, timeout=None):
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_GETUPDATES), offset=offset,
            limit=limit, timeout=timeout)
        ris = []
        for el in j:
            ris.append(Update.decode(el))
        return ris

    def setWebhook(self, url=None, certificate_path=None):
        if certificate_path:
            files = {'certificate': open(certificate_path, 'rb')}
        else:
            files = {}
        TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SETWEBHOOK),
                                 files=files, url=url)

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
