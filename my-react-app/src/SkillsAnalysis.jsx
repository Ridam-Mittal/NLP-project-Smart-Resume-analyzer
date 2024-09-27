import React from 'react';
import Navbar from './Navbar';  // Make sure Navbar is imported

const SkillsAnalysis = () => {
  const pageStyle = {
    minHeight: '100vh', // Ensures the content takes up the full viewport height
    width: '99vw',      // Takes up the full width of the page
    backgroundColor: '#1c1c1c', // Matches the dark theme
    color: '#fff',      // White text for visibility
    padding: '20px',    // Add some padding to the content
    boxSizing: 'border-box',
  };

  const contentStyle = {
    textAlign: 'center', // Center-aligns the text and elements
    marginTop: '100px',  // Adds some top space for balance
  };

  return (
    <div style={pageStyle}>
      {/* <Navbar />  Include the Navbar */}
      <div style={contentStyle}>
        <h1>Skills Analysis Page</h1>
        <p>This page is for analyzing skills.</p>
      </div>
    </div>
  );
};

export default SkillsAnalysis;
