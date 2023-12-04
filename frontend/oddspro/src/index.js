// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import AppRoutes from './AppRoutes';
import reportWebVitals from './reportWebVitals';

const root = document.getElementById('root');

ReactDOM.createRoot(root).render(
  <React.StrictMode>
    <AppRoutes />
  </React.StrictMode>
);

reportWebVitals();
