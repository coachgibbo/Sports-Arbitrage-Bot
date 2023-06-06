from Clients.sportsbet import SportsbetOpts
from Clients.sportsbet import SportsbetClient

if __name__ == '__main__':
    client = SportsbetClient()
    response = client.getTopSportsOdds(SportsbetOpts.Comps.AFL.value,
                                       {SportsbetOpts.Params.INCLUDE_TOP_MARKETS.value: "true",
                                        SportsbetOpts.Params.ROUND.value: "13"})

    for event in response["events"]:
        print(f"Match: {event['name']}")
        for market in event["marketList"]:
            print(f"{market['name']} - Selections:")
            for selection in market["selections"]:
                print(f"{selection['name']} - ({selection['price']['winPrice']})")
            print()

