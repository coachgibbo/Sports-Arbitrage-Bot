import requests


class SportsbetClient:
    url = "https://www.sportsbet.com.au/apigw/sportsbook-sports/Sportsbook/Sports/Competitions/"

    def getOdds(self, comp, params=None):
        curr_url = f"{self.url}{comp}"

        if params:
            curr_url += "?"
            for key, value in params.items():
                curr_url += f"{key}={value}"
                curr_url += "&"
            curr_url = curr_url[:-1]

        return requests.get(curr_url).json()
