import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  /* CSS Reset */
  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  /* Base styles */
  html {
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  
  body {
    background: ${({ theme }) => theme.background.default};
    color: ${({ theme }) => theme.text.primary};
    font-family: 'Roboto', 'Helvetica', 'Arial', sans-serif;
    transition: all 0.3s ease;
    line-height: 1.5;
  }

  h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    margin-bottom: 0.5em;
    color: ${({ theme }) => theme.text.primary};
  }

  p {
    margin-bottom: 1em;
    color: ${({ theme }) => theme.text.secondary};
  }

  a {
    color: ${({ theme }) => theme.primary.main};
    text-decoration: none;
    
    &:hover {
      text-decoration: underline;
    }
  }

  button {
    cursor: pointer;
  }

  /* Custom scrollbar */
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background: ${({ theme }) => theme.background.paper};
  }

  ::-webkit-scrollbar-thumb {
    background: ${({ theme }) => theme.action.hover};
    border-radius: 4px;
  }

  ::-webkit-scrollbar-thumb:hover {
    background: ${({ theme }) => theme.action.selected};
  }

  .card {
    background: ${({ theme }) => theme.surface};
    border-radius: 8px;
    box-shadow: ${({ theme }) => theme.shadow};
    padding: 1rem;
    margin-bottom: 1rem;
  }

  /* Additional custom global styles can be added here */
`;

export default GlobalStyles; 