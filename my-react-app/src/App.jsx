import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './Navbar';             // Import Navbar
import SkillsAnalysis from './SkillsAnalysis'; // Import your components
import CoursesResume from './CoursesResume';   // Import your components
import HomePage from './HomePage';             // Import the HomePage component
import AI from './AI';                         // Import the AI (Chatbot) component

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />             {/* Route for homepage */}
        <Route path="/SkillsAnalysis" element={<SkillsAnalysis />} />
        <Route path="/CoursesResume" element={<CoursesResume />} />
        <Route path="/AI" element={<AI />} />                 {/* Route for chatbot page */}
      </Routes>
    </Router>
  );
}

export default App;
