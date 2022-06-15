import re

HTML = re.compile('<.*?>|:')


class _DictionaryWrappedData:
    def __init__(self, word, meanings, pronunciation, examples, related_vocabulary, extra_vocabulary):
        self.word = word
        self.meanings = meanings
        self.pronunciation = pronunciation
        self.examples = examples
        self.related_vocabulary = related_vocabulary
        self.extra_vocabulary = extra_vocabulary


class DictionaryWebScraperInterface:
    def __init__(self): pass

    def scrap(self, word: str):
        html_raw_data = self._get_html_raw_data(word)
        meanings = self._extract_meanings(html_raw_data)
        pronunciations = self._extract_pronunciations(html_raw_data)
        examples = self._extract_examples(html_raw_data)
        related_vocabulary = self._collect_related_vocabulary(html_raw_data)
        extra_vocabulary = self._collect_extra_vocabulary(html_raw_data)
        return _DictionaryWrappedData(word, meanings, pronunciations, examples, related_vocabulary, extra_vocabulary)

    def _extract_pronunciations(self, html_raw_data: str):
        pass

    def _get_html_raw_data(self, word: str):
        pass

    def _extract_meanings(self, html_raw_data: str):
        pass

    def _collect_related_vocabulary(self, html_raw_data: str):
        pass

    def _enliminate_html(self, raw_html: str):
        return re.sub(HTML, '', raw_html).strip()

    def _extract_examples(self, raw_html):
        pass

    def _collect_extra_vocabulary(self, raw_html):
        pass