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
        prounciation_containers = soup.find_all('span', {'class': 'dpron-i'})
        pronunciations = {}
        for pronunciation_tag in prounciation_containers:
            ipa_tag = pronunciation_tag.find('span', {'class': 'ipa'})
            if ipa_tag is None:
                continue
            ipa = self._enliminate_html(ipa_tag.text)
            sounds = self._get_sounds(pronunciation_tag.find_all('source'))
            if pronunciations.__contains__(ipa) or sounds.__len__() == 0:
                continue
            pronunciations[ipa] = sounds
        return pronunciations

    def _get_sounds(self, sound_tags):
        sounds = []
        for tag in sound_tags:
            sounds.append(tag['src'])
        return sounds

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

    def _collect_related_vocabulary(self, html_raw_data: str):
        soup = BeautifulSoup(html_raw_data, 'lxml')
        related_word_container = soup.find('div', {'class': 'dbrowse'})
        related_word_tags = related_word_container.find_all('div')
        related_words = {}
        for tag in related_word_tags:
            result = tag.find('span', {'class': 'results'})
            if result is None:
                continue
            word = self._enliminate_html(result.text)
            link_tag = tag.find('a')
            if link_tag is None:
                continue
            link = link_tag['href']
            if link is None or related_words.__contains__(word):
                continue
            related_words[word] = link
        return related_words

    def _extract_examples(self, raw_html):
        soup = BeautifulSoup(raw_html, 'lxml')
        example_tags = soup.find_all('div', {'class': 'examp dexamp'})
        examples = []
        for tag in example_tags:
            examples.append(self._enliminate_html(tag.text))
        return examples

    def _collect_extra_vocabulary(self, raw_html):
        soup = BeautifulSoup(raw_html, 'lxml')
        related_word_tags = soup.find_all('a', {'class': 'query'})
        related_words = {}
        for tag in related_word_tags:
            word = self._enliminate_html(tag.text)
            link = tag['href']
            related_words[word] = link
        return related_words
