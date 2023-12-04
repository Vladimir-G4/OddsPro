// Header.js
import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';

const Header = () => (
    <header className="OddsPro-header">
      <Link to="/" className="Link">
        <img src="oddspro.svg" className="OddsPro-logo" alt="logo" />
      </Link>
      <h1>Welcome to OddsPro</h1>
      <p>The Ultimate Sports Betting Companion</p>
    </header>
);

export default Header;
