import React from 'react';
import styled from 'styled-components';
import { useTheme } from './ThemeProvider';

const ToggleContainer = styled.button`
  background: ${props => props.theme.background.paper};
  border: 2px solid ${props => props.theme.divider};
  border-radius: 30px;
  cursor: pointer;
  display: flex;
  font-size: 0.5rem;
  justify-content: space-between;
  margin: 0 auto;
  overflow: hidden;
  padding: 0.5rem;
  position: relative;
  width: 60px;
  height: 30px;
  outline: none;
  transition: ${props => props.theme.transition.main};

  &:hover {
    border-color: ${props => props.theme.primary.main};
  }
`;

const Icons = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
  transition: ${props => props.theme.transition.main};
  transform: ${props => props.isDarkMode ? 'translateX(0)' : 'translateX(0)'};
  
  svg {
    width: 16px;
    height: 16px;
    transition: ${props => props.theme.transition.main};
    color: ${props => props.theme.text.primary};
    
    &:first-child {
      opacity: ${props => props.isDarkMode ? 1 : 0.5};
    }
    
    &:last-child {
      opacity: ${props => props.isDarkMode ? 0.5 : 1};
    }
  }
`;

const Indicator = styled.div`
  background: ${props => props.theme.primary.main};
  border-radius: 50%;
  position: absolute;
  top: 3px;
  left: 3px;
  height: 20px;
  width: 20px;
  transform: ${props => props.isDarkMode ? 'translateX(0)' : 'translateX(30px)'};
  transition: transform 0.2s ease-in-out;
`;

const ThemeToggle = ({ className }) => {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <ToggleContainer className={className} onClick={toggleTheme} aria-label="Toggle dark mode">
      <Icons isDarkMode={isDarkMode}>
        {/* Moon Icon */}
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 3a9 9 0 1 0 9 9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 0 1-4.4 2.26 5.403 5.403 0 0 1-3.14-9.8c-.44-.06-.9-.1-1.36-.1z" />
        </svg>
        {/* Sun Icon */}
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2a1 1 0 0 0 0-2H2a1 1 0 0 0 0 2zm18 0h2a1 1 0 0 0 0-2h-2a1 1 0 0 0 0 2zM11 2v2a1 1 0 0 0 2 0V2a1 1 0 0 0-2 0zm0 18v2a1 1 0 0 0 2 0v-2a1 1 0 0 0-2 0zM5.99 4.58a.996.996 0 0 0-1.41 0 .996.996 0 0 0 0 1.41l1.06 1.06a.997.997 0 0 0 1.41-1.41L5.99 4.58zm12.37 12.37a.996.996 0 0 0-1.41 0 .996.996 0 0 0 0 1.41l1.06 1.06a.997.997 0 0 0 1.41-1.41l-1.06-1.06zm1.06-10.96a.997.997 0 0 0-1.41 1.41l1.06 1.06a.997.997 0 0 0 1.41-1.41l-1.06-1.06zM7.05 18.36a.997.997 0 0 0-1.41-1.41l-1.06 1.06a.997.997 0 0 0 1.41 1.41l1.06-1.06z" />
        </svg>
      </Icons>
      <Indicator isDarkMode={isDarkMode} />
    </ToggleContainer>
  );
};

export default ThemeToggle; 