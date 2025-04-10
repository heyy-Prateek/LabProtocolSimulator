import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body, #root {
    height: 100%;
    font-family: 'Roboto', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
  }

  body {
    background-color: ${({ theme }) => theme.background};
    color: ${({ theme }) => theme.text};
    transition: all 0.2s ease;
  }

  #root {
    display: flex;
    flex-direction: column;
  }

  main {
    flex: 1;
    margin-top: 60px; /* Height of the navbar */
    padding: 1.5rem;
    max-width: 1200px;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }

  h1, h2, h3, h4, h5, h6 {
    margin-bottom: 1rem;
    line-height: 1.2;
  }

  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.75rem;
  }

  h3 {
    font-size: 1.5rem;
  }

  h4 {
    font-size: 1.25rem;
  }

  p {
    margin-bottom: 1rem;
  }

  button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
  }

  button {
    cursor: pointer;
  }

  a {
    color: ${({ theme }) => theme.primary};
    text-decoration: none;
    
    &:hover {
      text-decoration: underline;
    }
  }

  img {
    max-width: 100%;
    height: auto;
  }

  /* Scrollbar styling */
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background: ${({ theme }) => theme.backgroundAlt};
  }

  ::-webkit-scrollbar-thumb {
    background: ${({ theme }) => theme.border};
    border-radius: 4px;
  }

  ::-webkit-scrollbar-thumb:hover {
    background: ${({ theme }) => theme.primary};
  }

  /* Form elements */
  input, select, textarea {
    padding: 0.5rem;
    border: 1px solid ${({ theme }) => theme.border};
    border-radius: 4px;
    background-color: ${({ theme }) => theme.inputBackground};
    color: ${({ theme }) => theme.text};
    transition: border-color 0.2s ease;
    
    &:focus {
      outline: none;
      border-color: ${({ theme }) => theme.primary};
      box-shadow: 0 0 0 2px ${({ theme }) => theme.primaryLight};
    }
  }

  /* Code blocks */
  pre, code {
    font-family: 'Courier New', Courier, monospace;
    background-color: ${({ theme }) => theme.codeBackground};
    border-radius: 4px;
  }

  pre {
    padding: 1rem;
    overflow-x: auto;
    margin-bottom: 1rem;
  }

  code {
    padding: 0.2rem 0.4rem;
  }
`;

export default GlobalStyle; 