from abc import ABC, abstractmethod

import requests


class MetadataScraper(ABC):

    @abstractmethod
    def getMetadata(self):
        pass

    def get(self, url):
        return requests.get(url)
