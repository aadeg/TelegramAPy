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
            chat = Chat.decode(j['chat'])
            date = datetime.fromtimestamp(j['date'])
            obj = Message(j['message_id'], date, chat)
            if 'from' in j:
                obj.from_ = User.decode(j['from'])
            if 'forward_from' in j:
                obj.forward_from = User.decode(j['forward_from'])
            if 'forward_date' in j:
                obj.forward_date = datetime.fromtimestamp(
                    j['forward_date'])
            if 'reply_to_message' in j:
                obj.reply_to_message = Message.decode(
                    j['reply_to_message'])
            if 'text' in j:
                obj.text = j['text']
            if 'audio' in j:
                obj.audio = Audio.decode(j['audio'])
            if 'document' in j:
                obj.document = Document.decode(j['document'])
            if 'photo' in j:
                obj.photo = []
                for el in j['photo']:
                    obj.photo.append(PhotoSize.decode(el))
            if 'sticker' in j:
                obj.sticker = Sticker.decode(j['sticker'])
            if 'video' in j:
                obj.video = Video.decode(j['video'])
            if 'voice' in j:
                obj.voice = Voice.decode(j['voice'])
            if 'caption' in j:
                obj.caption = j['caption']
            if 'contact' in j:
                obj.contact = Contact.decode(j['contact'])
            if 'location' in j:
                obj.location = Location.decode(j['location'])
            if 'new_chat_partecipant' in j:
                obj.new_chat_partecipant = User.decode(
                    j['new_chat_partecipant'])
            if 'left_chat_partecipant' in j:
                obj.left_chat_partecipant = User.decode(
                    j['left_chat_partecipant'])
            if 'new_chat_title' in j:
                obj.new_chat_title = j['new_chat_title']
            if 'new_chat_photo' in j:
                obj.new_chat_photo = []
                for el in j['new_chat_photo']:
                    obj.new_chat_photo.append(PhotoSize.decode(el))
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
            raise ObjectDecodingException("Message", j)

        return obj
