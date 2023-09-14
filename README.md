# MLB Betting Odds Script

![MLB Logo](https://www.mlbstatic.com/team-logos/league-on-dark/1.svg)

## Overview

This Python script retrieves today's MLB (Major League Baseball) betting odds for Over/Under bets using The Odds API and provides betting recommendations based on the combined average runs scored by each team over their last 5 games.

## Special Thanks

Special thanks to the following services for making this script possible:

- [The Odds API](https://the-odds-api.com): The primary data source for retrieving MLB betting odds.
- [Fox Sports MLB](https://www.foxsports.com/mlb/): The source of data for obtaining team statistics.

## Prerequisites

Before you can use this script, you'll need to ensure the following prerequisites are met:

1. **API Key from The Odds API**: You must obtain an API key from [The Odds API](https://the-odds-api.com) to access MLB betting odds data.

2. **Required Python Libraries**: Make sure you have the following Python libraries installed. You can install them using pip:

    ```bash
   pip install requests
   pip install beautifulsoup4

## Usage

1. Clone or download this repository to your local machine.

2. Replace the `API_KEY` variable in the script with your own API key from The Odds API.

3. Run the script using Python:

   ```bash
   python main.py

## Example Output
Washington Nationals @ Pittsburgh Pirates
COMBINED AVG RUNS OVER LAST 5 GAMES: 9.40
Recommended Bet: Unibet | totals | Washington Nationals @ Pittsburgh Pirates | Over | 8.5 | -105

Cincinnati Reds @ Detroit Tigers
COMBINED AVG RUNS OVER LAST 5 GAMES: 7.60
Recommended Bet: BetMGM | totals | Cincinnati Reds @ Detroit Tigers | Under | 9.0 | -115

New York Yankees @ Boston Red Sox
COMBINED AVG RUNS OVER LAST 5 GAMES: 7.80
Recommended Bet: PointsBet (US) | totals | New York Yankees @ Boston Red Sox | Under | 9.5 | -120
