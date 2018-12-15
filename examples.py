from pyforvo import Forvo, lang_codes

""" Initiate """
api_key = 'YOUR_API_KEY'
forvo = Forvo(api_key)

""" Download mp3 of single pronunciation """

word = forvo.pronunciation('こんにちは', lang=lang_codes.japanese)
word.download(fmt='mp3')

""" Play pronunciation (only supports Linux with mplayer installed) """
word = forvo.pronunciation('hello', lang=lang_codes.english)
word.play()

""" Download all pronunciations of word"""
words = forvo.pronunciations('goodbye')
for word in words:
    word.download()
