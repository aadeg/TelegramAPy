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
from datetime import datetime

from ..exception import ObjectDecodingException
from .chat import Chat
from .user import User
from .audio import Audio
from .photosize import PhotoSize
from .document import Document
from .sticker import Sticker
from .contact import Contact
from .video import Video
from .voice import Voice
from .location import Location


class Message:
    FIELD_CHAT = 'chat'
    FIELD_DATE = 'date'
    FIELD_MESSAGEID = 'message_id'
    FIELD_FROM = 'from'
    FIELD_FORWARDFROM = 'forward_from'
    FIELD_FORWARDDATE = 'forward_date'
    FIELD_REPLYTOMESSAGE = 'reply_to_message'
    FIELD_TEXT = 'text'
    FIELD_AUDIO = 'audio'
    FIELD_DOCUMENT = 'document'
    FIELD_PHOTO = 'photo'
    FIELD_STICKER = 'sticker'
    FIELD_VIDEO = 'video'
    FIELD_VOICE = 'voice'
    FIELD_CAPTION = 'caption'
    FIELD_CONTACT = 'contact'
    FIELD_LOCATION = 'location'
    FIELD_NEWCHATPARTECIPANT = 'new_chat_partecipant'
    FIELD_LEFTCHATPARTECIPANT = 'left_chat_partecipant'
    FIELD_NEWCHATTITLE = 'new_chat_title'
    FIELD_NEWCHATPHOTO = 'new_chat_photo'
    FIELD_DELETECHATPHOTO = 'delete_chat_photo'
    FIELD_GROUPCHATCREATED = 'group_chat_created'
    FIELD_SUPERGROUPCHATCREATED = 'supergroup_chat_created'
    FIELD_CHANNELCHATCREATED = 'channel_chat_created'
    FIELD_MIGRATETOCHARID = 'migrate_to_chat_id'
    FIELD_MIGRATEFROMCHATID = 'migrate_from_chat_id'

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
            chat = Chat.decode(j[Message.FIELD_CHAT])
            date = datetime.fromtimestamp(j[Message.FIELD_DATE])
            obj = Message(j[Message.FIELD_MESSAGEID], date, chat)
            if Message.FIELD_FROM in j:
                obj.from_ = User.decode(j[Message.FIELD_FROM])
            if Message.FIELD_FORWARDFROM in j:
                obj.forward_from = User.decode(j[Message.FIELD_FORWARDFROM])
            if Message.FIELD_FORWARDDATE in j:
                obj.forward_date = datetime.fromtimestamp(
                    j[Message.FIELD_FORWARDDATE])
            if Message.FIELD_REPLYTOMESSAGE in j:
                obj.reply_to_message = Message.decode(
                    j[Message.FIELD_REPLYTOMESSAGE])
            if Message.FIELD_TEXT in j:
                obj.text = j[Message.FIELD_TEXT]
            if Message.FIELD_AUDIO in j:
                obj.audio = Audio.decode(j[Message.FIELD_AUDIO])
            if Message.FIELD_DOCUMENT in j:
                obj.document = Document.decode(j[Message.FIELD_DOCUMENT])
            if Message.FIELD_PHOTO in j:
                obj.photo = []
                for el in j[Message.FIELD_PHOTO]:
                    obj.photo.append(PhotoSize.decode(el))
            if Message.FIELD_STICKER in j:
                obj.sticker = Sticker.decode(j[Message.FIELD_STICKER])
            if Message.FIELD_VIDEO in j:
                obj.video = Video.decode(j[Message.FIELD_VIDEO])
            if Message.FIELD_VOICE in j:
                obj.voice = Voice.decode(j[Message.FIELD_VOICE])
            if Message.FIELD_CAPTION in j:
                obj.caption = j[Message.FIELD_CAPTION]
            if Message.FIELD_CONTACT in j:
                obj.contact = Contact.decode(j[Message.FIELD_CONTACT])
            if Message.FIELD_LOCATION in j:
                obj.location = Location.decode(j[Message.FIELD_LOCATION])
            if Message.FIELD_NEWCHATPARTECIPANT in j:
                obj.new_chat_partecipant = User.decode(
                    j[Message.FIELD_NEWCHATPARTECIPANT])
            if Message.FIELD_LEFTCHATPARTECIPANT in j:
                obj.left_chat_partecipant = User.decode(
                    j[Message.FIELD_LEFTCHATPARTECIPANT])
            if Message.FIELD_NEWCHATTITLE in j:
                obj.new_chat_title = j[Message.FIELD_NEWCHATTITLE]
            if Message.FIELD_NEWCHATPHOTO in j:
                obj.new_chat_photo = []
                for el in j[Message.FIELD_NEWCHATPHOTO]:
                    obj.new_chat_photo.append(PhotoSize.decode(el))
            if Message.FIELD_DELETECHATPHOTO in j:
                obj.delete_chat_photo = j[Message.FIELD_DELETECHATPHOTO]
            if Message.FIELD_GROUPCHATCREATED in j:
                obj.group_chat_created = j[Message.FIELD_GROUPCHATCREATED]
            if Message.FIELD_SUPERGROUPCHATCREATED in j:
                obj.supergroup_chat_created = j[Message.FIELD_SUPERGROUPCHATCREATED]
            if Message.FIELD_CHANNELCHATCREATED in j:
                obj.channel_chat_created = j[Message.FIELD_CHANNELCHATCREATED]
            if Message.FIELD_MIGRATETOCHARID in j:
                obj.migrate_to_chat_id = j[Message.FIELD_MIGRATETOCHARID]
            if Message.FIELD_MIGRATEFROMCHATID in j:
                obj.migrate_from_chat_id = j[Message.FIELD_MIGRATEFROMCHATID]
        except KeyError:
            raise ObjectDecodingException("Message", j)

        return obj
