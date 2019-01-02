# Python Library for Forvo API 

Examples:

```python

from pyforvo import Forvo

""" Initiate """
api_key = 'YOUR_API_KEY'
forvo = Forvo(api_key)

""" Download mp3 of 'こんにちは' """
word = forvo.get_pronunciation('こんにちは', language='ja')
word.download(fmt='mp3')

""" Play pronunciation of 'Hello' (only supports Linux with mplayer installed) """
word = forvo.get_pronunciation('hello', language='en')
word.play()

""" Download all female pronunciations of 'goodbye' """
words = forvo.get_pronunciations('goodbye', sex='f')
for word in words:
    word.download()

""" Find the language code for 'Spanish' and download ogg of 'adios' """
code = forvo.get_language_code('Spanish')
word = forvo.get_pronunciation('adios', language=code)
word.download(fmt='ogg')

```