import { createGlobalStyle } from 'styled-components';

export const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
      'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
      sans-serif;
  }

  body {
    margin: 0;
    padding: 0;
    background-color: ${props => props.theme.background};
    color: ${props => props.theme.text};
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  
  /* Animations */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  @keyframes slideIn {
    from { transform: translateX(-20px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }
  
  /* Custom scrollbar */
  ::-webkit-scrollbar {
    width: 6px;
    height: 6px;
  }
  
  ::-webkit-scrollbar-track {
    background: ${props => props.theme.scrollbarTrack};
  }
  
  ::-webkit-scrollbar-thumb {
    background: ${props => props.theme.scrollbarThumb};
    border-radius: 3px;
  }
`;

export const darkTheme = {
  background: '#121212',
  surface: '#1E1E1E',
  primary: '#BB86FC',
  primaryVariant: '#3700B3',
  secondary: '#03DAC6',
  error: '#CF6679',
  text: '#FFFFFF',
  textSecondary: '#B0B0B0',
  border: '#333333',
  cardBackground: '#252525',
  scrollbarTrack: '#121212',
  scrollbarThumb: '#333333',
  hoverBackground: 'rgba(255, 255, 255, 0.05)',
  shadowLight: '0 4px 12px rgba(0, 0, 0, 0.15)',
  shadowMedium: '0 8px 24px rgba(0, 0, 0, 0.2)'
}; 