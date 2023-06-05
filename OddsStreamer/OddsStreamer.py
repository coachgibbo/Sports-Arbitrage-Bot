from Metadata import MetadataScraperFactory

if __name__ == '__main__':
    print("OddsStreamer V0.0.1")

    competition = int(input("Select a sport: \n1. AFL\n2. NRL\n3. Exit\n"))
    if competition < 0 or competition > 2:
        print("Exiting")
        exit(0)

    metadataScraper = MetadataScraperFactory.getScraper(competition)
    metadataScraper.getMetadata()
