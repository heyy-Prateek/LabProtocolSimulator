import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import styled from 'styled-components';
import { useTheme } from './ThemeProvider';
import ThemeToggle from './ThemeToggle';

const HeaderContainer = styled.header`
  background-color: ${({ theme }) => theme.primary};
  color: white;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
`;

const Logo = styled.div`
  font-size: 1.5rem;
  font-weight: bold;
  
  a {
    color: white;
    text-decoration: none;
    
    &:hover {
      text-decoration: none;
    }
  }
`;

const NavLinks = styled.div`
  display: flex;
  gap: 1.5rem;
  align-items: center;
`;

const NavLink = styled(Link)`
  color: white;
  text-decoration: none;
  font-weight: ${props => props.active ? 'bold' : 'normal'};
  padding-bottom: 2px;
  border-bottom: ${props => props.active ? '2px solid white' : 'none'};
  
  &:hover {
    border-bottom: 2px solid white;
  }
`;

const Header = () => {
  const { theme, toggleTheme } = useTheme();
  const location = useLocation();
  
  return (
    <HeaderContainer theme={theme}>
      <Nav>
        <Logo>
          <Link to="/">ChemEngSim</Link>
        </Logo>
        <NavLinks>
          <NavLink to="/" active={location.pathname === '/' ? 1 : 0}>
            Home
          </NavLink>
          <NavLink to="/experiments" active={location.pathname.includes('/experiments') ? 1 : 0}>
            Experiments
          </NavLink>
          <NavLink to="/chat" active={location.pathname === '/chat' ? 1 : 0}>
            Chat
          </NavLink>
          <ThemeToggle />
        </NavLinks>
      </Nav>
    </HeaderContainer>
  );
};

export default Header; 