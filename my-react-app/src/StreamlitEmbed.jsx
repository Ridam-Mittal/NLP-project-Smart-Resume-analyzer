import React from 'react';

const StreamlitEmbed = () => {
  return (
    <div style={{ width: '100%', height: '100vh' }}>  {/* Ensure the parent div is full width and height */}
      <iframe
        src="http://localhost:8501"
        style={{
          width: '99vw',      // Full width of the parent container
          height: '100vh',     // Full height of the parent container
          border: 'none',      // Removes the iframe border
          color: 'black'
        }}
        title="Streamlit App"
      />
    </div>
  );
};

export default StreamlitEmbed;
