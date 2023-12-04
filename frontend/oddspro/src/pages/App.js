// App.js
import React from 'react';
import { Link } from 'react-router-dom';
import Footer from '../components/Footer';
import Header from '../components/Header';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header className="OddsPro-header"/>
      
      <div className="Button-container">
        <Link to="/nfl" className="OddsPro-button">
          <span>🏈 NFL</span>
          <img src="nfl.svg" alt="NFL" className="Button-image" />
        </Link>
        <Link to="/mlb" className="OddsPro-button">
          <span>⚾ MLB</span>
          <img src="mlb.svg" alt="MLB" className="Button-image" />
        </Link>
        <Link to="/nba" className="OddsPro-button">
          <span>🏀 NBA</span>
          <img src="nba.svg" alt="NBA" className="Button-image" />
        </Link>
      </div>

      <div className="About">
        <h2 className="About-title">Welcome to OddsPro – Your Winning Playbook! 📋</h2>
        <p className="About-description">OddsPro is your new go-to resource for smart and strategic wagering. Dive into the latest odds, game insights, and receive tailored recommendations based on historical data across a variety of sports leagues.</p>
        <div className="About-why-choose">
          <h3>Why Choose OddsPro?</h3>
          <ul>
            <li><strong>✅ Real-time Odds:</strong> Stay updated with the latest odds for NFL, MLB, and NBA games.</li>
            <li><strong>✅ Data-Driven Recommendations:</strong> Leverage insights based on historical data to enhance your betting strategy.</li>
            <li><strong>✅ User-Friendly Interface:</strong> Enjoy a smooth and intuitive experience designed with you in mind.</li>
          </ul>
        </div>
        <p className="About-get-started">Ready to get started? Explore featured sports leagues or jump into specific games. Bet confidently with OddsPro by your side!</p>
      </div>

      <Footer />
    </div>
  );
}

export default App;
