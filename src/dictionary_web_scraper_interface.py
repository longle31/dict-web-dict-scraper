import re

HTML = re.compile('<.*?>|:')


class _DictionaryWrappedData:
    def __init__(self, word, meanings, pronunciation, examples, related_words):
        self.word = word
        self.meanings = meanings
        self.pronunciation = pronunciation
        self.examples = examples
        self.related_words = related_words


class DictionaryWebScraperInterface:
    def __init__(self): pass

    def scrap(self, word: str):
        html_raw_data = self._get_html_raw_data(word)
        meanings = self._extract_meanings(html_raw_data)
        pronunciations = self._extract_pronunciations(html_raw_data)
        examples = self._extract_examples(html_raw_data)
        related_words = self._collect_related_words(html_raw_data)
        return _DictionaryWrappedData(word, meanings, pronunciations, examples, related_words)

    def _extract_pronunciations(self, html_raw_data: str):
        pass

    def _get_html_raw_data(self, word: str):
        pass

    def _extract_meanings(self, html_raw_data: str):
        pass

    def _collect_related_words(self, html_raw_data: str):
        pass

    def _enliminate_html(self, raw_html: str):
        return re.sub(HTML, '', raw_html).strip()

    def _extract_examples(self, raw_html):
        pass
