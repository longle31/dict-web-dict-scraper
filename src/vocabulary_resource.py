from flask_restful import Resource
from cambridge_dictionary_scraper import  CambridgeDictionaryScraper


class VocabularyResource(Resource):
    def __init__(self):
        self.scaper = CambridgeDictionaryScraper()

    def get(self, vocab):
        return self.scaper.scrap(vocab).__dict__
