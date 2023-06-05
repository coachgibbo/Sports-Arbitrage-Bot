from Metadata.Scrapers.AFLMetadataScraper import AFLMetadataScraper
from Metadata.Scrapers.NRLMetadataScraper import NRLMetadataScraper

sports = {1: AFLMetadataScraper(), 2: NRLMetadataScraper()}


def getScraper(sport_id):
    return sports[sport_id]
