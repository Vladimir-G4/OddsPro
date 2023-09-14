# Vladimir Gutierrez

# MLB Betting Odds Script
# This script retrieves today's MLB betting odds (Over/Under) using The Odds API and provides betting recommendations based on combined average runs scored over each team's last 5 games.
# Special Thanks to 'The Odds API (the-odds-api.com)' and 'Fox Sports (foxsports.com/mlb)'
#
# Prerequisites:
# - You need to obtain an API key from The Odds API.
# - Ensure required libraries are installed ('pip install requests', 'pip install beautifulsoup4') and you have internet access

import requests
import re
from bs4 import BeautifulSoup

API_KEY = "YOUR_API_KEY_HERE"

def getBets(API_KEY):

    """
    Retrieve MLB betting odds (Over/Under) using The Odds API.

    Args:
        API_KEY (str): Your API key for The Odds API.

    Returns:
        dict: A dictionary containing the bets for each game from various bookmakers.
              The bets are organized by game name.
              Example:
              {
                  'Away Team @ Home Team': [
                      'Bookmaker | Bet Type | Away Team @ Home Team | Over | 7.5 | +150',
                      # ... (more betting lines for the same game)
                  ],
                  # ... (more games with betting lines)
              }
    """

    API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/"
    PARAMS = {
        "apiKey": API_KEY,
        "regions": "us",
        "markets": "totals",
        "oddsFormat": "american",
    }

    RESPONSE = requests.get(API_URL, params=PARAMS)

    # If API call is successful, grab json response and print to array
    if RESPONSE.status_code == 200:
        JSON_DATA = RESPONSE.json()
        BETS = []
        BETS_BY_TEAM = {}

        for item in JSON_DATA:
            HOME_TEAM = item["home_team"]
            AWAY_TEAM = item["away_team"]
            for bookmaker in item["bookmakers"]:
                for market in bookmaker["markets"]:
                    for outcome in market["outcomes"]:
                        BOOKMAKER = bookmaker["title"]
                        BET_TYPE = market["key"]
                        OVER_UNDER = outcome["name"]
                        POINT = outcome["point"]
                        PRICE_FOR_OVER = outcome["price"]

                        STRING_RESULTS = f"{BOOKMAKER} | {BET_TYPE} | {AWAY_TEAM} @ {HOME_TEAM} | {OVER_UNDER} | {POINT} | {PRICE_FOR_OVER}"

                        ALLOWED_BOOKMAKERS = [
                            "DraftKings",
                            "Barstool Sportsbook",
                            "FanDuel",
                            "BetMGM",
                            "Unibet",
                            "WynnBET",
                            "PointsBet (US)",
                        ]

                        if BOOKMAKER not in ALLOWED_BOOKMAKERS:
                            continue

                        BETS.append(STRING_RESULTS)

        for BET in BETS:
            BET_INFO = BET.split(" | ")
            GAME_NAME = BET_INFO[2]

            if GAME_NAME in BETS_BY_TEAM:
                BETS_BY_TEAM[GAME_NAME].append(BET)
            else:
                BETS_BY_TEAM[GAME_NAME] = [BET]

        return BETS_BY_TEAM

    else:
        print(f"Error: {RESPONSE.status_code}")



def getLastFiveAvgRunsScored(TEAM):

    """
    Get the average runs scored by a specified MLB team in their last 5 games.

    Args:
        TEAM (str): The name of the MLB team.

    Returns:
        str: The average runs scored by the team in the last 5 games as a string,
             or a message indicating if the data was not found.
    """

    SCRAPE_TEAM = re.sub(r"[^a-zA-Z0-9]+", "-", TEAM).lower()

    MLB_URL = "https://www.foxsports.com/mlb/"
    MLB_END_URL = "-team-game-log/"
    TEAM_RESPONSE = requests.get(MLB_URL + SCRAPE_TEAM + MLB_END_URL)

    TEAM_SOUP = BeautifulSoup(TEAM_RESPONSE.text, "html.parser")
    AWAYS_DATA = TEAM_SOUP.find("tbody", class_="row-data")

    try:
        AWAYS_DATA = AWAYS_DATA.find_all("tr")
        AVG_RUNS = 0.0
        for row in AWAYS_DATA:
            RUNS_SCORED = row.find("td", {"data-index": "4"}).find("div").text.strip()
            AVG_RUNS += float(RUNS_SCORED)

        AVG_RUNS = AVG_RUNS / 5

    except AttributeError:
        AVG_RUNS = "\nAVG_RUNS Not Found For " + SCRAPE_TEAM

    return str(AVG_RUNS)



def getTeamLogoURL(TEAM):

    """
    Get the URL of the logo for a specified MLB team from the Fox Sports website.

    Args:
        TEAM (str): The name of the MLB team.

    Returns:
        str: The URL of the team's logo, or the team name as a fallback if the logo is not found.
    """

    SCRAPE_TEAM = re.sub(r"[^a-zA-Z0-9]+", "-", TEAM).lower()

    MLB_URL = "https://www.foxsports.com/mlb/"
    MLB_END_URL = "-team-game-log/"
    TEAM_RESPONSE = requests.get(MLB_URL + SCRAPE_TEAM + MLB_END_URL)

    TEAM_SOUP = BeautifulSoup(TEAM_RESPONSE.text, "html.parser")
    TEAM_LOGO = TEAM_SOUP.find("img", class_="entity-card-logo")

    try:

        if(TEAM_LOGO and "src" in TEAM_LOGO.attrs):
            TEAM_LOGO = TEAM_LOGO["src"]
            return TEAM_LOGO
        else:
            TEAM_LOGO = SCRAPE_TEAM
            return TEAM_LOGO
    except AttributeError:
        return SCRAPE_TEAM



def getLastFiveGameScores(TEAM):

    """
    Get the scores of the last 5 games played by a specified MLB team.

    Args:
        TEAM (str): The name of the MLB team.

    Returns:
        str: A string containing the game dates, opposing teams, and runs scored for each game,
             or a message indicating if no game data was found for the team.
    """

    SCRAPE_TEAM = re.sub(r"[^a-zA-Z0-9]+", "-", TEAM).lower()

    MLB_URL = "https://www.foxsports.com/mlb/"
    MLB_END_URL = "-team-game-log/"
    TEAM_RESPONSE = requests.get(MLB_URL + SCRAPE_TEAM + MLB_END_URL)

    TEAM_SOUP = BeautifulSoup(TEAM_RESPONSE.text, "html.parser")
    AWAYS_DATA = TEAM_SOUP.find("tbody", class_="row-data")
    GAME_DATA = f"\n{TEAM}"

    try:

        AWAYS_DATA = AWAYS_DATA.find_all("tr")
        AVG_RUNS = 0.0
        for row in AWAYS_DATA:
            GAME_DATE = row.find("td", {"data-index": "0"}).find("div").text.strip()
            OPPOSING_TEAM = (
                row.find("td", {"data-index": "1"}).find_all("a")[1].text.strip()
            )
            RUNS_SCORED = row.find("td", {"data-index": "4"}).find("div").text.strip()

            AVG_RUNS += float(RUNS_SCORED)
            GAME_DATA += f"\nDate: {GAME_DATE}, Opposing Team: {OPPOSING_TEAM}, Runs Scored: {RUNS_SCORED}"

        AVG_RUNS = AVG_RUNS / 5

    except AttributeError:
        GAME_DATA = "\nNo Game Data Found For " + SCRAPE_TEAM

    return "\n" + GAME_DATA + "\n"



def getTotalAvg(HOME_TEAM, AWAY_TEAM):

    """
    Calculate the total average runs scored for both specified MLB teams.

    Args:
        HOME_TEAM (str): The name of the home team.
        AWAY_TEAM (str): The name of the away team.

    Returns:
        float: The total average runs scored by both teams.
    """

    HOME_AVG = float(getLastFiveAvgRunsScored(HOME_TEAM))
    AWAY_AVG = float(getLastFiveAvgRunsScored(AWAY_TEAM))
    TOTAL_AVG = HOME_AVG + AWAY_AVG

    return TOTAL_AVG

def getRecommendedBets():

    """
    Retrieve and recommend MLB betting lines based on average runs scored over each team's last 5 games.

    This function iterates through the retrieved MLB betting odds (Over/Under) for each game and makes recommendations
    by comparing these odds to the calculated total average runs scored by the home and away teams. It selects the
    betting line (Over or Under) that is farthest from the calculated total average runs scored, considering both
    the point and odds.

    Returns:
        None: This function prints the recommended betting lines for each game.
    """

    for GAME, BETS in getBets(API_KEY).items():
    
        TEAMS = GAME.split(" @ ")
        AWAY_TEAM = TEAMS[0]
        AWAY_TEAM_LOGO_URL = getTeamLogoURL(AWAY_TEAM)
        HOME_TEAM = TEAMS[1]
        HOME_TEAM_LOGO_URL = getTeamLogoURL(HOME_TEAM)
        TOTAL_AVG = float(getTotalAvg(HOME_TEAM, AWAY_TEAM))
        FARTHEST_POINT = None
        BEST_ODDS = None
        BEST_BET = None
        FARTHEST_POINT_OVER = None
        BEST_ODDS_OVER = None
        BEST_BET_OVER = None
        FARTHEST_POINT_UNDER = None
        BEST_ODDS_UNDER = None
        BEST_BET_UNDER = None

        print(f"{GAME}\nCOMBINED AVG RUNS OVER LAST 5 GAMES: {TOTAL_AVG:.2f}")

        for BET in BETS:
            BET_INFO = BET.split(" | ")
            OVER_UNDER = BET_INFO[3]
            POINT = float(BET_INFO[4])
            ODDS = int(BET_INFO[5])
            if( OVER_UNDER == 'Over' and (FARTHEST_POINT_OVER is None or (abs(TOTAL_AVG - POINT)) >= abs(TOTAL_AVG - FARTHEST_POINT_OVER))) and (BEST_ODDS_OVER is None or max(ODDS, BEST_ODDS_OVER) == ODDS):
                FARTHEST_POINT_OVER = POINT
                BEST_BET_OVER = BET
                BEST_ODDS_OVER = ODDS
            elif( OVER_UNDER == 'Under' and (FARTHEST_POINT_UNDER is None or (abs(TOTAL_AVG - POINT)) >= abs(TOTAL_AVG - FARTHEST_POINT_UNDER))) and (BEST_ODDS_UNDER is None or max(ODDS, BEST_ODDS_UNDER) == ODDS):
                FARTHEST_POINT_UNDER = POINT
                BEST_BET_UNDER = BET
                BEST_ODDS_UNDER = ODDS
        
        FARTHEST_POINT = max(FARTHEST_POINT_OVER, FARTHEST_POINT_UNDER)
        if(FARTHEST_POINT < TOTAL_AVG):
            BEST_BET = BEST_BET_OVER
            BEST_ODDS = BEST_ODDS_OVER
        elif(FARTHEST_POINT > TOTAL_AVG):
            BEST_BET = BEST_BET_UNDER
            BEST_ODDS = BEST_ODDS_UNDER

        print(f"Recommended Bet: {BEST_BET}\n")

# ACCESSIBLE VARIABLES
# BEST_BET | HOME_TEAM | AWAY_TEAM | TOTAL_AVG:.2f | HOME_TEAM_LOGO_URL | AWAY_TEAM_LOGO_URL

getRecommendedBets()
