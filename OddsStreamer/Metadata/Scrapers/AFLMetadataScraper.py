from datetime import datetime

from .MetadataScraper import MetadataScraper


class AFLMetadataScraper(MetadataScraper):

    url = "https://api.squiggle.com.au/"

    def __init__(self):
        pass

    def getMetadata(self):
        games = self.get(f"{self.url}?q=games;complete=0").json()["games"]
        selected_round = int(input(f"Enter a round to view games for ({games[0]['round']} - {min(24, games[-1]['round'])}): "))

        game_index = -1
        for i, game in enumerate(games):
            if game['round'] == selected_round:
                game_index = i
                break

        print("Select a game to stream odds: ")
        game_map = {}
        i = 1
        while games[game_index]['round'] == selected_round:
            game_map[i] = games[game_index]
            print(f"{i}. {games[game_index]['hteam']} vs {games[game_index]['ateam']} - {datetime.strptime(games[game_index]['date'], '%Y-%m-%d %H:%M:%S').strftime('%A %d %b, %I:%M %p')}")
            game_index += 1
            i += 1

        selected_game = int(input(""))
        print(f"Selected Game: {game_map[selected_game]['hteam']} vs {game_map[selected_game]['ateam']}")
        return selected_game, game_map[selected_game]
