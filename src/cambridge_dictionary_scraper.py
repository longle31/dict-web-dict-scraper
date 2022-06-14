from dictionary_web_scraper_interface import DictionaryWebScraperInterface
import requests
from bs4 import BeautifulSoup


class CambridgeDictionaryScraper(DictionaryWebScraperInterface):
    def __init__(self):
        super(CambridgeDictionaryScraper, self).__init__()

    def scrap(self, word: str):
        return super(CambridgeDictionaryScraper, self).scrap(word)

    def _extract_pronunciations(self, html_raw_data: str):
        soup = BeautifulSoup(html_raw_data, 'lxml')
        prounciation_containers = soup.find_all('span', {'class': 'pron dpron'})
        pronunciations = []
        for meaning in prounciation_containers:
            pronunciations.append(self._enliminate_html(meaning.text))
        return list(dict.fromkeys(pronunciations))

    def _get_html_raw_data(self, word: str) -> str:
        return requests.get('https://dictionary.cambridge.org/dictionary/english/' + word, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/51.0.2704.103 Safari/537.36 "
        }).text

    def _extract_meanings(self, html_raw_data: str):
        soup = BeautifulSoup(html_raw_data, 'lxml')
        meaning_containers = soup.find_all('div', {'class': 'def ddef_d db'})
        meanings = []
        for meaning in meaning_containers:
            meanings.append(self._enliminate_html(meaning.text))
        return meanings

    def _collect_related_words(self, html_raw_data: str):
        soup = BeautifulSoup(html_raw_data, 'lxml')
        related_word_tags = soup.find_all('a', {'class': 'query'})
        related_words = {}
        for tag in related_word_tags:
            word = self._enliminate_html(tag.text)
            link = tag['href']
            related_words[word] = link
        return related_words

    def _extract_examples(self, raw_html):
        soup = BeautifulSoup(raw_html, 'lxml')
        example_tags = soup.find_all('div', {'class': 'examp dexamp'})
        examples = []
        for tag in example_tags:
            examples.append(self._enliminate_html(tag.text))
        return examples
