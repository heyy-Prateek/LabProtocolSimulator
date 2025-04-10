import React from 'react';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

const SidebarContainer = styled.div`
  width: ${props => props.isOpen ? '280px' : '0'};
  height: 100%;
  background-color: ${props => props.theme.surface};
  border-right: 1px solid ${props => props.theme.border};
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  overflow: hidden;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: 999;
  box-shadow: ${props => props.isOpen ? props.theme.shadow : 'none'};
  
  @media (max-width: 768px) {
    width: ${props => props.isOpen ? '100%' : '0'};
  }
`;

const Logo = styled.div`
  padding: 24px 20px;
  border-bottom: 1px solid ${props => props.theme.border};
  margin-bottom: 20px;
  
  h1 {
    color: ${props => props.theme.primary};
    font-size: 1.5rem;
    margin: 0;
  }
  
  span {
    color: ${props => props.theme.textSecondary};
    font-size: 0.8rem;
  }
`;

const NavSection = styled.div`
  margin-bottom: 24px;
`;

const SectionTitle = styled.div`
  padding: 8px 20px;
  color: ${props => props.theme.textSecondary};
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
`;

const NavItemStyled = styled(NavLink)`
  display: flex;
  align-items: center;
  padding: 12px 20px;
  color: ${props => props.theme.text};
  text-decoration: none;
  position: relative;
  transition: all 0.2s ease;
  
  &:hover {
    background-color: ${props => props.theme.hoverBackground};
  }
  
  &.active {
    color: ${props => props.theme.primary};
    background-color: rgba(187, 134, 252, 0.08);
    
    &::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      width: 4px;
      background-color: ${props => props.theme.primary};
    }
  }
  
  svg {
    margin-right: 12px;
    width: 20px;
    height: 20px;
  }
`;

const ExperimentsList = styled.div`
  max-height: 300px;
  overflow-y: auto;
`;

const experiments = [
  { id: 1, name: "Isothermal Batch Reactor" },
  { id: 2, name: "Isothermal Semi-batch Reactor" },
  { id: 3, name: "Isothermal CSTR" },
  { id: 4, name: "Isothermal PFR" },
  { id: 5, name: "Crushers and Ball Mill" },
  { id: 6, name: "Plate and Frame Filter Press" },
  { id: 7, name: "Rotary Vacuum Filter" },
  { id: 8, name: "Centrifuge and Flotation" },
  { id: 9, name: "Classifiers" },
  { id: 10, name: "Trommel" }
];

function Sidebar({ isOpen }) {
  return (
    <SidebarContainer isOpen={isOpen}>
      <Logo>
        <h1>ChemEng Lab</h1>
        <span>Chemical Engineering Simulator</span>
      </Logo>
      
      <NavSection>
        <SectionTitle>Main</SectionTitle>
        <NavItemStyled to="/" end>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
            <polyline points="9 22 9 12 15 12 15 22" />
          </svg>
          Dashboard
        </NavItemStyled>
        
        <NavItemStyled to="/chat">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2v10z" />
          </svg>
          Chat Assistant
        </NavItemStyled>
        
        <NavItemStyled to="/reports">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
            <polyline points="10 9 9 9 8 9" />
          </svg>
          Reports
        </NavItemStyled>
      </NavSection>
      
      <NavSection>
        <SectionTitle>Experiments</SectionTitle>
        <ExperimentsList>
          {experiments.map(exp => (
            <NavItemStyled 
              key={exp.id} 
              to={`/experiment/${exp.id}`}
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M9 3v2m0 0v5.5A2.5 2.5 0 0 0 11.5 13H13m4-7.5V3m0 0v12.5M13 13l4 4m-1.5-4.5V18.5a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2h2m5.5 1a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0Z" />
              </svg>
              {exp.name}
            </NavItemStyled>
          ))}
        </ExperimentsList>
      </NavSection>
    </SidebarContainer>
  );
}

export default Sidebar; 