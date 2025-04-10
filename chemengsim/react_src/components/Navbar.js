import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import styled from 'styled-components';
import ThemeToggle from './ThemeToggle';
import { useTheme } from './ThemeProvider';

const NavbarContainer = styled.nav`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-color: ${props => props.theme.background.paper};
  color: ${props => props.theme.text.primary};
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 100;
  transition: ${props => props.theme.transition.main};
`;

const Logo = styled(Link)`
  font-size: 1.4rem;
  font-weight: bold;
  color: ${props => props.theme.primary.main};
  text-decoration: none;
  display: flex;
  align-items: center;
  
  span {
    margin-left: 8px;
  }
`;

const MenuButton = styled.button`
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 24px;
  width: 30px;
  position: relative;
  margin-right: 20px;
  
  span {
    width: 100%;
    height: 3px;
    background-color: ${props => props.theme.text.primary};
    border-radius: 3px;
    transition: ${props => props.theme.transition.main};
    transform-origin: 1px;
    
    &:nth-child(1) {
      transform: ${props => props.isOpen ? 'rotate(45deg)' : 'rotate(0)'};
    }
    
    &:nth-child(2) {
      opacity: ${props => props.isOpen ? '0' : '1'};
      transform: ${props => props.isOpen ? 'translateX(-20px)' : 'translateX(0)'};
    }
    
    &:nth-child(3) {
      transform: ${props => props.isOpen ? 'rotate(-45deg)' : 'rotate(0)'};
    }
  }
  
  @media (min-width: 769px) {
    display: none;
  }
`;

const NavItems = styled.div`
  display: flex;
  align-items: center;
`;

const NavLink = styled(Link)`
  color: ${props => props.theme.text.primary};
  text-decoration: none;
  margin-left: 20px;
  position: relative;
  transition: ${props => props.theme.transition.main};
  font-weight: ${props => props.isActive ? 'bold' : 'normal'};
  
  &:after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: ${props => props.isActive ? '100%' : '0'};
    height: 2px;
    background-color: ${props => props.theme.primary.main};
    transition: width 0.3s ease;
  }
  
  &:hover {
    color: ${props => props.theme.primary.main};
    
    &:after {
      width: 100%;
    }
  }
  
  @media (max-width: 768px) {
    display: none;
  }
`;

const ThemeToggleWrapper = styled.div`
  margin-left: 20px;
`;

const UserProfile = styled.div`
  display: flex;
  align-items: center;
  cursor: pointer;
  position: relative;
  
  img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    object-fit: cover;
    margin-left: 20px;
  }
`;

const NotificationBadge = styled.div`
  position: relative;
  margin-left: 20px;
  
  svg {
    width: 24px;
    height: 24px;
    color: ${props => props.theme.text.primary};
  }
  
  span {
    position: absolute;
    top: -5px;
    right: -5px;
    background-color: ${props => props.theme.error.main};
    color: white;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    font-size: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
`;

const Navbar = ({ toggleSidebar }) => {
  const [isOpen, setIsOpen] = useState(false);
  const { theme } = useTheme();
  const location = useLocation();
  
  const handleMenuClick = () => {
    setIsOpen(!isOpen);
    toggleSidebar();
  };

  return (
    <NavbarContainer>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <MenuButton onClick={handleMenuClick} isOpen={isOpen} aria-label="Toggle menu">
          <span />
          <span />
          <span />
        </MenuButton>
        <Logo to="/">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.59 7L21 8.41L15.44 14L12 10.56L2 20.56L3.41 22L12 13.42L15.44 16.86L22.41 9.91L24 11.5V7H19.59Z" fill={theme.primary.main} />
            <path d="M4 13.25L2 13.75V7H4V13.25Z" fill={theme.primary.main} />
            <path d="M8 10.5L6 11.25V7H8V10.5Z" fill={theme.primary.main} />
            <path d="M12 8.75L10 9.5V7H12V8.75Z" fill={theme.primary.main} />
          </svg>
          <span>ChemEngSim</span>
        </Logo>
      </div>
      
      <NavItems>
        <NavLink to="/" isActive={location.pathname === '/'}>
          Dashboard
        </NavLink>
        <NavLink to="/help" isActive={location.pathname === '/help'}>
          Help
        </NavLink>
        <NavLink to="/about" isActive={location.pathname === '/about'}>
          About
        </NavLink>
        <NavLink to="/settings" isActive={location.pathname === '/settings'}>
          Settings
        </NavLink>
        
        <NotificationBadge>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z" />
          </svg>
          <span>2</span>
        </NotificationBadge>
        
        <ThemeToggleWrapper>
          <ThemeToggle />
        </ThemeToggleWrapper>
        
        <UserProfile>
          <img src="https://ui-avatars.com/api/?name=User&background=random" alt="User profile" />
        </UserProfile>
      </NavItems>
    </NavbarContainer>
  );
};

export default Navbar; 