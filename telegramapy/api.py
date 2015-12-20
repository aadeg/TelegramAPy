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
    """Allow to send requests to the Telegram Bot API

    Its methods take the name directly from the Telegram page and
    allow you to send messages, send objects (photos, videos, ...) and
    get updates using the Telegram inteface.

    :param str token: Token generated by Telegram (BotFather)

    Usage::

        >>> from telegramapy.api import TelegramAPy
        >>> api = TelegramAPy('TokenGeneratedByTelegram')
        <TelegramAPy>
    """

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
        self._file_url = "%sfile/bot%s/" % (TelegramAPy.TELEGRAM_URL,
                                            self._token)

    def __repr__(self):
        return '<TelegramAPy>'

    def getMe(self):
        """Returns a :class:`User <User>` with basic information
        about the bot.

        :return: :class:`User <User>` object
        :rtype: telegramapy.types.User
        """
        j = TelegramAPy._sendRequest(self._getUrl('getMe'))
        return User.decode(j)

    def sendMessage(self, chat_id, text, parse_mode=None,
                    disable_web_page_preview=None, reply_to_message_id=None,
                    reply_markup=None):
        """Sends a message to the specified chat_id.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str text: Text of the message to be sent.
        :param str parse_mode: Pass :attr:`TelegramAPy.MARKDOWN_MODE`
            if you want to show bold, italic and inline URLs in your message.
        :param bool disable_web_page_preview: Disables link previewsfor links
            in this message.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
        rep_markup = reply_markup.encode() if reply_markup else None
        j = TelegramAPy._sendRequest(
                self._getUrl(TelegramAPy.METHOD_SENDMESSAGE),
                chat_id=chat_id, text=text, parse_mode=parse_mode,
                reply_to_message_id=reply_to_message_id,
                disable_web_page_preview=disable_web_page_preview,
                reply_markup=rep_markup)

        return Message.decode(j)

    def forwardMessage(self, chat_id, from_chat_id, message_id):
        """Forwards a message.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param from_chat_id: Unique identifier for the chat where the original
            message was sent.
        :type from_chat_id: int or str
        :param int message_id: Unique message identifier
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_FORWARDMESSAGE),
            chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
        return Message.decode(j)

    def sendPhoto(self, chat_id, photo, is_path=True, caption=None,
                  reply_to_message_id=None, replay_markup=None):
        """Sends a photo to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str photo: Photo to send. You can either pass a *file_id* as
            String to resend a photo that is already on the Telegram server,
            or the path of the photo if you want to upload a new photo.
        :param bool is_path: True if you passed a path in the *photo* argument;
            False if you passed a *file_id* in the *photo*.
        :param str caption: Photo caption.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends an audio to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str audio: Audio to send. You can either pass a *file_id* as
            String to resend an audio that is already on the Telegram server,
            or the path of the audio if you want to upload a new audio.
        :param bool is_path: True if you passed a path in the *audio* argument;
            False if you passed a *file_id* in the *audio*.
        :param int duration: Duration of the audio in seconds.
        :param str performer: Performer.
        :param str title: Track name.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends a document to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str document: File to send. You can either pass a *file_id* as
            String to resend an file that is already on the Telegram server,
            or the path of the file if you want to upload a new file.
        :param bool is_path: True if you passed a path in the *document*
            argument; False if you passed a *file_id* in the *document*.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends a sticker to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str sticker: Sticker to send. You can either pass a *file_id* as
            String to resend an sticker that is already on the Telegram server,
            or the path of the sticker if you want to upload a new sticker.
        :param bool is_path: True if you passed a path in the *sticker*
            argument; False if you passed a *file_id* in the *sticker*.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends an video to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str video: Video to send. You can either pass a *file_id* as
            String to resend an video that is already on the Telegram server,
            or the path of the video if you want to upload a new video.
        :param bool is_path: True if you passed a path in the *video* argument;
            False if you passed a *file_id* in the *video*.
        :param int duration: Duration of the video in seconds.
        :param str caption: Video caption.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends voice message to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str voice: Voice to send. You can either pass a *file_id* as
            String to resend an voice that is already on the Telegram server,
            or the path of the voice if you want to upload a new voice.
        :param bool is_path: True if you passed a path in the *voice* argument;
            False if you passed a *file_id* in the *voice*.
        :param int duration: Duration of the voice in seconds.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
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
        """Sends location to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param int latitude: Latitude of location.
        ::param int longitude: Longitude of location.
        :param int reply_to_message_id: If the message is a reply, ID of the
            original message.
        :param reply_markup: Additional interface options. Pass a
            :class:`ReplyKeyboardMarkup <ReplyKeyboardMarkup>` object,
            :class:`ReplyKeyboardHide <ReplyKeyboardHide>` object or
            :class:`ForceReply <ForceReply>` object.
        :return: :class:`Message <Message>` object
        :rtype: telegramapy.types.Message
        """
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDLOCATION), chat_id=chat_id,
            latitude=latitude, longitude=longitude,
            replay_markup=replay_markup,
            reply_to_message_id=reply_to_message_id)
        return Message.decode(j)

    def sendChatAction(self, chat_id, action):
        """Sends a chat action to the specified chat.

        :param chat_id: Unique identifier for the target chat or username
            of the target channel.
        :type chat_id: int or str
        :param str action: Type of action to broadcast.
        """
        TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_SENDCHATACTION), chat_id=chat_id,
            action=action)

    def getUserProfilePhotos(self, user_id, offset=None, limit=None):
        """Returns a list of profile pictures for a user.

        :param int user_id: Unique identifier of the target user.
        :param int offset: Sequential number of the first photo to be returned.
            By default, all photos are returned.
        :param int limit: Limits the number of photos to be retrieved. Values
            between 1 - 100 are accepted. Defaults to 100.
        :return: :class:`UserProfilePhotos <UserProfilePhotos>` object
        :rtype: telegramapy.types.UserProfilePhotos
        """
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_GETUSERPROFILEPHOTOS),
            user_id=user_id, offset=offset, limit=limit)
        return UserProfilePhotos.decode(j)

    def getFile(self, file_id):
        """Use this method to basic info about a file and repare it for downloading.

        :param str file_id: File identifier to get info about.
        :return: :class:`File <File>` object
        :rtype: telegramapy.types.File
        """
        j = TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_GETFILE),
                                     file_id=file_id)
        return File.decode(j)

    def getUpdates(self, offset=None, limit=None, timeout=None):
        """Use to receive incoming updates using long polling.

        :param int offset: Identifier of the first update to be returned.
        :param int limit: Limits the number of updates t be retrieved. Values
            between 1 - 100 are accepted. Defaults to 100.
        :param int timeout: Timeout in seconds for long polling.
        :return: List of :class:`Update <Update>` object
        :rtype: [telegramapy.types.Update]
        """
        j = TelegramAPy._sendRequest(
            self._getUrl(TelegramAPy.METHOD_GETUPDATES), offset=offset,
            limit=limit, timeout=timeout)
        ris = []
        for el in j:
            ris.append(Update.decode(el))
        return ris

    def setWebhook(self, url=None, certificate_path=None):
        """Use this method to specify a url and receive incoming updates via
        an outgoing webhook.

        :param str url: HTTPS url to send updates to. Use an empty string to
            remove webhook intergration.
        :param str certificate_path: Path of the certificate that Telegram
            will use to validate the connection.
        """
        if certificate_path:
            files = {'certificate': open(certificate_path, 'rb')}
        else:
            files = {}
        TelegramAPy._sendRequest(self._getUrl(TelegramAPy.METHOD_SETWEBHOOK),
                                 files=files, url=url)

    def downloadFile(self, file_, file_path):
        """Download a file from Telegram servers.

        :param file_: :class:`File <File>` object to download.
        :param file_path: Path where to save the downloaded file.
        """
        req = requests.get(self._file_url + file_.file_path, stream=True)
        if req.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in req:
                    f.write(chunk)
        else:
            raise TelegramException('Unable to download file.')

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
