import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './components/ThemeProvider';
import Dashboard from './pages/Dashboard';
import ExperimentView from './components/ExperimentView';
import Settings from './pages/Settings';
import Help from './pages/Help';
import About from './pages/About';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import GlobalStyle from './styles/GlobalStyle';

function App() {
  return (
    <ThemeProvider>
      <Router>
        <GlobalStyle />
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/experiment/:id" element={<ExperimentView />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="/help" element={<Help />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </ThemeProvider>
  );
}

export default App; 