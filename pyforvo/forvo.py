import requests
from pyforvo.word import Word


class Forvo(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'https://apifree.forvo.com/key/{api_key}/format/json/action'

    def pronunciation(self, word, lang=None):
        if lang:
            url = f'{self.base_url}/standard-pronunciation/word/{word}/language/{lang}'
        else:
            url = f'{self.base_url}/standard-pronunciation/word/{word}/'

        item = self._get(url)[0]
        return self._word(item)

    def pronunciations(self, word):
        # TODO: add optional arguments
        url = f'{self.base_url}/word-pronunciations/word/{word}'
        words = []
        items = self._get(url)
        for item in items:
            words.append(self._word(item))
        return words

    def _get(self, url):
        response = requests.get(url)
        # print(response.status_code, response.reason, response.json())
        rjson = response.json()
        if rjson.get('items'):
            return rjson.get('items')

    @staticmethod
    def _word(item):
        word = Word(id=item.get('id'),
                    word=item.get('word'),
                    original=item.get('original'),
                    added=item.get('addtime'),
                    hits=item.get('hits'),
                    username=item.get('username'),
                    sex=item.get('sex'),
                    country=item.get('country'),
                    code=item.get('code'),
                    language=item.get('langname'),
                    mp3_path=item.get('pathmp3'),
                    ogg_path=item.get('pathogg'),
                    rate=item.get('rate'),
                    votes=item.get('num_votes'),
                    positive_votes=item.get('num_positive_votes'))
        return word
