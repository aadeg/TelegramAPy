from setuptools import setup

setup(name='telegramapy',
      version='0.1.0',
      description='Library for interacting with the Telegram Bot API.',
      url='https://github.com/aadeg/TelegramAPy',
      author='Giove Andrea',
      author_email='andreagiove@outlook.com',
      license='GNU GPL v2.0',
      packages=['telegramapy'],
      install_requires=[
        'requests'
      ],
      zip_safe=False)
