from Clients.sportsbet.SportsbetOpts import Params, Comps
from Clients.sportsbet.SportsbetClient import SportsbetClient
from Metadata import MetadataScraperFactory

if __name__ == '__main__':
    print("OddsStreamer V0.0.1")

    competition = int(input("Select a sport: \n1. AFL\n2. NRL\n3. Exit\n"))
    if competition < 1 or competition > 2:
        print("Exiting")
        exit(0)

    metadataScraper = MetadataScraperFactory.getScraper(competition)
    selected_game, selected_game_data = metadataScraper.getMetadata()

    client = SportsbetClient()

    response = client.getOdds(Comps.AFL.value,
                              {Params.ROUND.value: str(selected_game_data['round']),
                               Params.INCLUDE_TOP_MARKETS.value: "true",
                               Params.EVENT_FILTER.value: "matches"})

    selected_markets = response['events'][selected_game - 1]['marketList']
    for market in selected_markets:
        titles = ""
        odds = ""
        for selection in market['selections']:
            titles += selection['name']
            titles += "  |  "
            odds += (str(selection['price']['winPrice']).center(len(selection['name'])))
            odds += "  |  "
        print(f"{market['name']}")
        print(f"{titles}\n{odds}\n")
