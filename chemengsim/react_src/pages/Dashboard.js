import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import Navbar from '../components/Navbar';
import { useSimulatorBridge } from '../api/SimulatorBridge';

const DashboardContainer = styled.div`
  padding: 20px;
`;

const WelcomeSection = styled.div`
  background-color: ${props => props.theme.background.paper};
  padding: 30px;
  border-radius: ${props => props.theme.borderRadius};
  margin-bottom: 30px;
  box-shadow: ${props => props.theme.shadow};
`;

const WelcomeTitle = styled.h1`
  color: ${props => props.theme.text.primary};
  margin-bottom: 10px;
`;

const WelcomeText = styled.p`
  color: ${props => props.theme.text.secondary};
  font-size: 1.1rem;
  line-height: 1.5;
  margin-bottom: 20px;
`;

const GetStartedButton = styled(Link)`
  display: inline-block;
  background-color: ${props => props.theme.primary.main};
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: ${props => props.theme.transition.main};
  
  &:hover {
    background-color: ${props => props.theme.primary.dark};
    transform: translateY(-2px);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  }
`;

const SectionTitle = styled.h2`
  color: ${props => props.theme.text.primary};
  margin-bottom: 20px;
  font-weight: 500;
`;

const ExperimentsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
`;

const ExperimentCard = styled(Link)`
  background-color: ${props => props.theme.background.paper};
  border-radius: ${props => props.theme.borderRadius};
  padding: 20px;
  transition: ${props => props.theme.transition.main};
  box-shadow: ${props => props.theme.shadow};
  display: flex;
  flex-direction: column;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  
  &:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    background-color: ${props => props.theme.primary.main};
  }
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  }
`;

const ExperimentTitle = styled.h3`
  color: ${props => props.theme.text.primary};
  margin-bottom: 10px;
`;

const ExperimentDescription = styled.p`
  color: ${props => props.theme.text.secondary};
  font-size: 0.9rem;
  line-height: 1.5;
  flex-grow: 1;
  margin-bottom: 15px;
`;

const ExperimentFooter = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: ${props => props.theme.text.disabled};
  font-size: 0.8rem;
  border-top: 1px solid ${props => props.theme.divider};
  padding-top: 10px;
`;

const StatsSection = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
`;

const StatCard = styled.div`
  background-color: ${props => props.theme.background.paper};
  border-radius: ${props => props.theme.borderRadius};
  padding: 20px;
  text-align: center;
  box-shadow: ${props => props.theme.shadow};
  transition: ${props => props.theme.transition.main};
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
  }
`;

const StatValue = styled.div`
  font-size: 2.5rem;
  font-weight: bold;
  color: ${props => props.color || props.theme.primary.main};
  margin-bottom: 5px;
`;

const StatLabel = styled.div`
  color: ${props => props.theme.text.secondary};
  font-size: 0.9rem;
`;

const LoadingState = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  background-color: ${props => props.theme.background.paper};
  border-radius: ${props => props.theme.borderRadius};
  box-shadow: ${props => props.theme.shadow};
  color: ${props => props.theme.text.secondary};
`;

const Dashboard = ({ toggleSidebar }) => {
  const [experiments, setExperiments] = useState([]);
  const [loading, setLoading] = useState(true);
  const { getExperiments } = useSimulatorBridge();
  
  useEffect(() => {
    const fetchExperiments = async () => {
      try {
        const data = await getExperiments();
        if (data) {
          setExperiments(data);
        }
        setLoading(false);
      } catch (error) {
        console.error('Failed to fetch experiments:', error);
        setLoading(false);
      }
    };
    
    fetchExperiments();
    
    // If getExperiments() failed or is not available, fall back to mock data
    const timeoutId = setTimeout(() => {
      if (loading) {
        setExperiments([
          { 
            id: 'batch_reactor', 
            name: 'Isothermal Batch Reactor', 
            description: 'Study the dynamics of chemical reactions in a batch reactor under isothermal conditions.',
            lastUpdated: '2 days ago',
            difficulty: 'Beginner'
          },
          { 
            id: 'semi_batch_reactor', 
            name: 'Semi-Batch Reactor', 
            description: 'Examine reactions with continuous addition of reactants while maintaining a constant volume.',
            lastUpdated: '3 days ago',
            difficulty: 'Intermediate'
          },
          { 
            id: 'cstr', 
            name: 'Continuous Stirred Tank Reactor', 
            description: 'Analyze steady-state and dynamic behavior of continuously stirred tank reactors.',
            lastUpdated: '1 week ago',
            difficulty: 'Intermediate'
          },
          { 
            id: 'pfr', 
            name: 'Plug Flow Reactor', 
            description: 'Study the behavior of reactants flowing through a tubular reactor with minimal mixing.',
            lastUpdated: '2 weeks ago',
            difficulty: 'Advanced'
          },
          { 
            id: 'filter_press', 
            name: 'Filter Press', 
            description: 'Examine solid-liquid separation through pressure filtration processes.',
            lastUpdated: '3 weeks ago',
            difficulty: 'Intermediate'
          },
          { 
            id: 'rotary_vacuum_filter', 
            name: 'Rotary Vacuum Filter', 
            description: 'Study continuous filtration using a rotating drum with vacuum suction.',
            lastUpdated: '1 month ago',
            difficulty: 'Advanced'
          }
        ]);
        setLoading(false);
      }
    }, 2000);
    
    return () => clearTimeout(timeoutId);
  }, [getExperiments, loading]);
  
  return (
    <>
      <Navbar toggleSidebar={toggleSidebar} />
      <DashboardContainer>
        <WelcomeSection>
          <WelcomeTitle>Welcome to Chemical Engineering Lab Simulator</WelcomeTitle>
          <WelcomeText>
            Explore various chemical engineering experiments in a virtual environment. 
            Gain hands-on experience without the risks and costs associated with real laboratory equipment.
          </WelcomeText>
          <GetStartedButton to="/experiment/batch_reactor">
            Get Started with an Experiment
          </GetStartedButton>
        </WelcomeSection>
        
        <SectionTitle>Available Experiments</SectionTitle>
        {loading ? (
          <LoadingState>Loading experiments...</LoadingState>
        ) : (
          <ExperimentsGrid>
            {experiments.map(experiment => (
              <ExperimentCard 
                key={experiment.id} 
                to={`/experiment/${experiment.id}`}
              >
                <ExperimentTitle>{experiment.name}</ExperimentTitle>
                <ExperimentDescription>{experiment.description}</ExperimentDescription>
                <ExperimentFooter>
                  <span>Last updated: {experiment.lastUpdated || 'Recently'}</span>
                  <span>Difficulty: {experiment.difficulty || 'All Levels'}</span>
                </ExperimentFooter>
              </ExperimentCard>
            ))}
          </ExperimentsGrid>
        )}
        
        <SectionTitle>Your Progress</SectionTitle>
        <StatsSection>
          <StatCard>
            <StatValue>6</StatValue>
            <StatLabel>Experiments Completed</StatLabel>
          </StatCard>
          <StatCard>
            <StatValue color="#f72585">84%</StatValue>
            <StatLabel>Average Score</StatLabel>
          </StatCard>
          <StatCard>
            <StatValue color="#4cc9f0">12</StatValue>
            <StatLabel>Hours Spent</StatLabel>
          </StatCard>
          <StatCard>
            <StatValue color="#4895ef">4</StatValue>
            <StatLabel>Reports Generated</StatLabel>
          </StatCard>
        </StatsSection>
      </DashboardContainer>
    </>
  );
};

export default Dashboard; 