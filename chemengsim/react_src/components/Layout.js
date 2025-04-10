import React from 'react';
import styled from 'styled-components';
import Header from './Header';
import Footer from './Footer';
import { useTheme } from './ThemeProvider';

const Main = styled.main`
  background-color: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.text};
  min-height: calc(100vh - 160px); /* Adjust based on header/footer height */
  padding: 2rem;
`;

const LayoutContainer = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const Layout = ({ children }) => {
  const { theme } = useTheme();
  
  return (
    <LayoutContainer>
      <Header />
      <Main theme={theme}>
        {children}
      </Main>
      <Footer />
    </LayoutContainer>
  );
};

export default Layout; 