import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', None)
TEST_CHAT_ID = os.getenv('TEST_CHAT_ID', None)

TESTS_PATH = os.path.dirname(os.path.realpath(__file__))
DECODING_FILES_PATH = os.path.join(TESTS_PATH, 'decoding')
SEND_MESSAGES = False
