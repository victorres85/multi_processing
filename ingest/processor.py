from collections import Counter
from typing import Dict

import spacy

from ingest.debugging import app_logger as log

class DataProcessor():

    def __init__(self) -> None:
        log.info('spacy:loading model')
        self.nlp = spacy.load('en_core_web_sm')
        self.skip = ['CARDINAL', 'MONEY', 'ORDINAL', 'DATE', 'TIME']
        log.info('spacy: loaded model')

    def entities(self, doc) -> Counter:
        t = [e.text.lower() for e in doc.ents if e.label_ not in self.skip]
        return Counter(t)

    def process(self, text: str) -> Dict:
        return {'entities': self.entities(self.nlp(text))}
    
    def process_message(self, post):
        return None