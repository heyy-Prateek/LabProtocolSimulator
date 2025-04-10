import React, { useState } from 'react';
import styled from 'styled-components';
import ExperimentChart from './ExperimentChart';

const DashboardContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
  width: 100%;
  margin-top: 15px;
`;

const ChartCard = styled.div`
  background-color: ${props => props.theme.background.paper};
  border-radius: 8px;
  box-shadow: ${props => props.theme.shadow};
  padding: 15px;
  height: 350px;
  display: flex;
  flex-direction: column;
`;

const ChartTypeSelector = styled.div`
  display: flex;
  justify-content: center;
  margin-bottom: 15px;
`;

const ChartTypeButton = styled.button`
  background-color: ${props => props.active ? props.theme.primary.main : props.theme.background.default};
  color: ${props => props.active ? props.theme.primary.contrastText : props.theme.text.primary};
  border: 1px solid ${props => props.active ? props.theme.primary.main : props.theme.divider};
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &:not(:last-child) {
    margin-right: 10px;
  }
  
  &:hover {
    background-color: ${props => props.active ? props.theme.primary.main : props.theme.background.paper};
  }
`;

/**
 * Dashboard component for visualizing experiment data
 */
const ExperimentDashboard = ({ data }) => {
  const [selectedCharts, setSelectedCharts] = useState(['concentration', 'conversion']);
  
  const toggleChartType = (type) => {
    if (selectedCharts.includes(type)) {
      // If already selected, remove it
      if (selectedCharts.length > 1) { // Ensure at least one chart is always displayed
        setSelectedCharts(selectedCharts.filter(chart => chart !== type));
      }
    } else {
      // Add it to the selection
      setSelectedCharts([...selectedCharts, type]);
    }
  };
  
  return (
    <>
      <ChartTypeSelector>
        <ChartTypeButton 
          active={selectedCharts.includes('concentration')} 
          onClick={() => toggleChartType('concentration')}
        >
          Concentration
        </ChartTypeButton>
        <ChartTypeButton 
          active={selectedCharts.includes('conversion')} 
          onClick={() => toggleChartType('conversion')}
        >
          Conversion
        </ChartTypeButton>
        <ChartTypeButton 
          active={selectedCharts.includes('rate')} 
          onClick={() => toggleChartType('rate')}
        >
          Reaction Rate
        </ChartTypeButton>
      </ChartTypeSelector>
      
      <DashboardContainer>
        {selectedCharts.includes('concentration') && (
          <ChartCard>
            <ExperimentChart data={data} type="concentration" />
          </ChartCard>
        )}
        
        {selectedCharts.includes('conversion') && (
          <ChartCard>
            <ExperimentChart data={data} type="conversion" />
          </ChartCard>
        )}
        
        {selectedCharts.includes('rate') && (
          <ChartCard>
            <ExperimentChart data={data} type="rate" />
          </ChartCard>
        )}
      </DashboardContainer>
    </>
  );
};

export default ExperimentDashboard; 