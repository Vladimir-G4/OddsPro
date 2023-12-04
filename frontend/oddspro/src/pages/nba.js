// nba.js
import React from 'react';
import './nba.css'; // Import your styles here
import nbaData from '../dummy_data/nba.json';
import Footer from '../components/Footer.js';
import Header from '../components/Header.js';

const NBAGameCard = ({ game }) => (
  <div className="nba-game-card">
    <div className="teams">
      <div className="team-info">
        <img src={game.homeTeam.logoURL} alt={game.homeTeam.name} className="team-logo" />
        <p>{game.homeTeam.name}</p>
        <p>{game.homeTeam.record}</p>
      </div>
      <div className="vs">vs</div>
      <div className="team-info">
        <img src={game.awayTeam.logoURL} alt={game.awayTeam.name} className="team-logo" />
        <p>{game.awayTeam.name}</p>
        <p>{game.awayTeam.record}</p>
      </div>
    </div>
    <div className="bets">
      <table>
        <thead>
          <tr>
            <th>Sportsbook</th>
            <th>Bet</th>
            <th>Points</th>
            <th>Odds</th>
          </tr>
        </thead>
        <tbody>
          {game.bets.map((bet, index) => (
            <tr key={index} className={bet.highlight ? 'recommended-bet-row' : ''}>
              <td>{bet.sportsbook}</td>
              <td>{bet.bet}</td>
              <td>{bet.points}</td>
              <td>{bet.odds}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);

const NBADashboard = () => (
  <div className="nba-dashboard">
    <Header />

    <div className="dashboard-container">
      {nbaData.games.map((game, index) => (
        <NBAGameCard key={index} game={game} />
      ))}
    </div>

    <Footer />
  </div>
);

export default NBADashboard;