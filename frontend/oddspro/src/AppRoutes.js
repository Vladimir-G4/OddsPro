import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './pages/App.js';
import NBADashboard from './pages/nba.js';
import NFL from './pages/nfl.js';
import MLB from './pages/mlb.js';

const AppRoutes = () => (
  <Router>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/nba" element={<NBADashboard />} />
      <Route path="/nfl" element={<NFL />} />
      <Route path="/mlb" element={<MLB />} />
    </Routes>
  </Router>
);

export default AppRoutes;
