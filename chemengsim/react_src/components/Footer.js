import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const FooterContainer = styled.footer`
  background-color: ${props => props.theme.background.paper};
  color: ${props => props.theme.text.secondary};
  padding: 2rem 1rem;
  margin-top: auto;
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.05);
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  
  @media (min-width: 768px) {
    flex-direction: row;
    justify-content: space-between;
  }
`;

const FooterSection = styled.div`
  margin-bottom: 1.5rem;
  
  @media (min-width: 768px) {
    margin-bottom: 0;
  }
`;

const FooterTitle = styled.h3`
  font-size: 1rem;
  margin-bottom: 1rem;
  color: ${props => props.theme.text.primary};
`;

const FooterLinks = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const FooterLink = styled.li`
  margin-bottom: 0.5rem;
  
  a {
    color: ${props => props.theme.text.secondary};
    text-decoration: none;
    transition: color 0.2s ease;
    
    &:hover {
      color: ${props => props.theme.primary.main};
    }
  }
`;

const Copyright = styled.div`
  text-align: center;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid ${props => props.theme.divider};
  font-size: 0.875rem;
`;

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <FooterContainer>
      <FooterContent>
        <FooterSection>
          <FooterTitle>ChemEngSim</FooterTitle>
          <FooterLinks>
            <FooterLink>
              <Link to="/">Dashboard</Link>
            </FooterLink>
            <FooterLink>
              <Link to="/help">Help</Link>
            </FooterLink>
            <FooterLink>
              <Link to="/about">About</Link>
            </FooterLink>
          </FooterLinks>
        </FooterSection>
        
        <FooterSection>
          <FooterTitle>Resources</FooterTitle>
          <FooterLinks>
            <FooterLink>
              <a href="https://en.wikipedia.org/wiki/Chemical_engineering" target="_blank" rel="noopener noreferrer">
                Chemical Engineering Basics
              </a>
            </FooterLink>
            <FooterLink>
              <a href="https://www.aiche.org/" target="_blank" rel="noopener noreferrer">
                AIChE
              </a>
            </FooterLink>
            <FooterLink>
              <a href="https://www.sciencedirect.com/topics/chemical-engineering" target="_blank" rel="noopener noreferrer">
                Research Papers
              </a>
            </FooterLink>
          </FooterLinks>
        </FooterSection>
        
        <FooterSection>
          <FooterTitle>Contact</FooterTitle>
          <FooterLinks>
            <FooterLink>
              <a href="mailto:contact@chemengsim.example.com">
                Email Us
              </a>
            </FooterLink>
            <FooterLink>
              <a href="https://github.com/example/chemengsim" target="_blank" rel="noopener noreferrer">
                GitHub
              </a>
            </FooterLink>
            <FooterLink>
              <a href="https://twitter.com/chemengsim" target="_blank" rel="noopener noreferrer">
                Twitter
              </a>
            </FooterLink>
          </FooterLinks>
        </FooterSection>
      </FooterContent>
      
      <Copyright>
        © {currentYear} Chemical Engineering Laboratory Simulator. All rights reserved.
      </Copyright>
    </FooterContainer>
  );
};

export default Footer; 