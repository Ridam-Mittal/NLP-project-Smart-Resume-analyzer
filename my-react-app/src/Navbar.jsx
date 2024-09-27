import React from 'react';
import { Link } from 'react-router-dom'; // Use Link instead of <a>

const Navbar = () => {
  const navbarStyle = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'black',
    color: 'white',
    padding: '10px 20px',
  };

  const logoStyle = {
    fontSize: '24px',
    fontWeight: 'bold',
  };

  const navLinksStyle = {
    listStyleType: 'none',
    display: 'flex',
    gap: '20px',
  };

  const linkStyle = {
    color: '#fff',
    textDecoration: 'none',
    fontSize: '18px',
    transition: 'color 0.3s',
  };

  const linkHoverStyle = {
    color: '#bbb',
  };

  return (
    <nav style={navbarStyle}>
      <div style={logoStyle}>MySite</div>
      <ul style={navLinksStyle}>
        <li>
          <Link to="/" style={linkStyle} onMouseEnter={(e) => e.target.style.color = linkHoverStyle.color} onMouseLeave={(e) => e.target.style.color = '#fff'}>
            Home
          </Link>
        </li>
        <li>
          <Link to="/SkillsAnalysis" style={linkStyle} onMouseEnter={(e) => e.target.style.color = linkHoverStyle.color} onMouseLeave={(e) => e.target.style.color = '#fff'}>
            Skills Analysis
          </Link>
        </li>
        <li>
          <Link to="/CoursesResume" style={linkStyle} onMouseEnter={(e) => e.target.style.color = linkHoverStyle.color} onMouseLeave={(e) => e.target.style.color = '#fff'}>
            Courses/Resume
          </Link>
        </li>
        <li>
          <Link to="/AI" style={linkStyle} onMouseEnter={(e) => e.target.style.color = linkHoverStyle.color} onMouseLeave={(e) => e.target.style.color = '#fff'}>
            Chatbot
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
