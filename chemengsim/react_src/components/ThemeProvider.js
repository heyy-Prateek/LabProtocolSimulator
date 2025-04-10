import React, { createContext, useState, useContext, useEffect } from 'react';
import { ThemeProvider as StyledThemeProvider, createGlobalStyle } from 'styled-components';
import { lightTheme, darkTheme } from '../theme/theme';

// Create a context for the theme
const ThemeContext = createContext({
  theme: lightTheme,
  isDarkMode: false,
  toggleTheme: () => {},
});

// Global styles that apply to the entire app
const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    font-family: ${props => props.theme.fontFamily};
    background-color: ${props => props.theme.background.default};
    color: ${props => props.theme.text.primary};
    transition: all 0.3s ease-in-out;
  }

  * {
    box-sizing: border-box;
  }

  a {
    color: ${props => props.theme.primary.main};
    text-decoration: none;
  }

  h1, h2, h3, h4, h5, h6 {
    margin-top: 0;
  }
`;

// Custom hook to use the theme
export const useTheme = () => useContext(ThemeContext);

// ThemeProvider component
export const ThemeProvider = ({ children }) => {
  // Check for user's preferred theme from local storage or system preferences
  const getInitialTheme = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      return savedTheme === 'dark';
    }
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  };

  const [isDarkMode, setIsDarkMode] = useState(getInitialTheme());
  const theme = isDarkMode ? darkTheme : lightTheme;

  // Toggle theme function
  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
    localStorage.setItem('theme', !isDarkMode ? 'dark' : 'light');
  };

  // Update theme when system preference changes
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleChange = () => {
      if (localStorage.getItem('theme') === null) {
        setIsDarkMode(mediaQuery.matches);
      }
    };
    
    mediaQuery.addEventListener('change', handleChange);
    return () => mediaQuery.removeEventListener('change', handleChange);
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, isDarkMode, toggleTheme }}>
      <StyledThemeProvider theme={theme}>
        <>
          <GlobalStyle />
          {children}
        </>
      </StyledThemeProvider>
    </ThemeContext.Provider>
  );
}; 