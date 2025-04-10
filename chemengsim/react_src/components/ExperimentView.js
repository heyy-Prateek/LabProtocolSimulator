import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import styled from 'styled-components';
import { useSimulatorBridge } from '../api/SimulatorBridge';
import ExperimentDashboard from './ExperimentDashboard';

const ExperimentContainer = styled.div`
  padding: 20px;
  background-color: ${props => props.theme.background.paper};
  border-radius: 8px;
  box-shadow: ${props => props.theme.shadow};
  margin-bottom: 20px;
`;

const ExperimentHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
`;

const Title = styled.h2`
  color: ${props => props.theme.text.primary};
  margin: 0;
`;

const Description = styled.p`
  color: ${props => props.theme.text.secondary};
  margin-bottom: 20px;
`;

const StatusIndicator = styled.div`
  display: flex;
  align-items: center;
  
  span {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 8px;
    background-color: ${props => {
      switch (props.status) {
        case 'running':
          return props.theme.success.main;
        case 'paused':
          return props.theme.warning.main;
        case 'completed':
          return props.theme.info.main;
        case 'error':
          return props.theme.error.main;
        default:
          return props.theme.action.disabled;
      }
    }};
  }
`;

const ControlPanel = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
`;

const Button = styled.button`
  background-color: ${props => {
    if (props.primary) return props.theme.primary.main;
    if (props.secondary) return props.theme.secondary.main;
    if (props.danger) return props.theme.error.main;
    if (props.success) return props.theme.success.main;
    if (props.warning) return props.theme.warning.main;
    return props.theme.background.default;
  }};
  color: ${props => {
    if (props.primary || props.secondary || props.danger || props.success || props.warning) {
      return props.theme.text.primary === '#ffffff' ? '#ffffff' : '#ffffff';
    }
    return props.theme.text.primary;
  }};
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  
  &:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
  
  svg {
    margin-right: 6px;
  }
`;

const ParametersPanel = styled.div`
  background-color: ${props => props.theme.background.default};
  padding: 15px;
  border-radius: 4px;
  margin-bottom: 20px;
`;

const ParameterGroup = styled.div`
  margin-bottom: 15px;
  
  h3 {
    font-size: 16px;
    margin-bottom: 10px;
    color: ${props => props.theme.text.primary};
  }
`;

const ParameterRow = styled.div`
  display: flex;
  margin-bottom: 10px;
  align-items: center;
`;

const ParameterLabel = styled.label`
  flex: 1;
  font-size: 14px;
  color: ${props => props.theme.text.secondary};
`;

const ParameterInput = styled.input`
  width: 120px;
  padding: 6px 10px;
  border: 1px solid ${props => props.theme.divider};
  border-radius: 4px;
  background-color: ${props => props.theme.background.paper};
  color: ${props => props.theme.text.primary};
  
  &:focus {
    outline: none;
    border-color: ${props => props.theme.primary.main};
  }
`;

const DataVisualization = styled.div`
  background-color: ${props => props.theme.background.default};
  border-radius: 4px;
  padding: 15px;
  display: flex;
  flex-direction: column;
  position: relative;
  min-height: ${props => props.empty ? '300px' : 'auto'};
`;

const LoadingOverlay = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  backdrop-filter: blur(2px);
`;

const NoDataMessage = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: ${props => props.theme.text.disabled};
  flex-direction: column;
  
  svg {
    margin-bottom: 10px;
    font-size: 40px;
  }
`;

const ExperimentView = () => {
  // Get experimentId from URL parameters
  const { experimentId } = useParams();
  
  const {
    isConnected,
    experimentData,
    simulationState,
    startExperiment,
    stopExperiment,
    pauseExperiment,
    resumeExperiment,
    updateParameters,
    getExperiments,
    getExperimentDetails,
    generateReport
  } = useSimulatorBridge();
  
  const [experiment, setExperiment] = useState(null);
  const [parameters, setParameters] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Fetch experiment details when the component mounts or experimentId changes
  useEffect(() => {
    const fetchExperimentDetails = async () => {
      if (!experimentId) return;
      
      try {
        setLoading(true);
        const experimentDetails = await getExperimentDetails(experimentId);
        
        if (experimentDetails) {
          setExperiment(experimentDetails);
          setParameters(experimentDetails.parameters || {});
        } else {
          setError('Failed to fetch experiment details');
        }
      } catch (err) {
        setError(`Error: ${err.message}`);
      } finally {
        setLoading(false);
      }
    };
    
    fetchExperimentDetails();
  }, [experimentId, getExperimentDetails]);
  
  // Handle parameter change
  const handleParameterChange = (key, value) => {
    const updatedParameters = { ...parameters, [key]: value };
    setParameters(updatedParameters);
    
    // If simulation is running, update the parameters in real-time
    if (simulationState.status === 'running') {
      updateParameters({ [key]: value });
    }
  };
  
  // Start the experiment simulation
  const handleStartExperiment = () => {
    if (!experimentId) return;
    startExperiment(experimentId, parameters);
  };
  
  // Generate a report
  const handleGenerateReport = async () => {
    if (!experimentId) return;
    
    try {
      const report = await generateReport({
        experimentId,
        title: experiment ? experiment.name : 'Experiment Report',
        includeCharts: true
      });
      
      if (report && report.reportPath) {
        // Open the report in a new tab
        window.open(report.reportPath, '_blank');
      } else {
        setError('Failed to generate report');
      }
    } catch (err) {
      setError(`Error generating report: ${err.message}`);
    }
  };
  
  if (loading) {
    return (
      <ExperimentContainer>
        <LoadingOverlay>
          <p>Loading experiment data...</p>
        </LoadingOverlay>
      </ExperimentContainer>
    );
  }
  
  if (error) {
    return (
      <ExperimentContainer>
        <Title>Error</Title>
        <Description>{error}</Description>
        <Button onClick={() => setError(null)}>Dismiss</Button>
      </ExperimentContainer>
    );
  }
  
  if (!experiment) {
    return (
      <ExperimentContainer>
        <Title>Experiment Not Found</Title>
        <Description>The requested experiment could not be found.</Description>
      </ExperimentContainer>
    );
  }
  
  const isRunning = simulationState.status === 'running';
  const isPaused = simulationState.status === 'paused';
  const isCompleted = simulationState.status === 'completed';
  
  return (
    <ExperimentContainer>
      <ExperimentHeader>
        <Title>{experiment.name}</Title>
        <StatusIndicator status={simulationState.status}>
          <span></span>
          {simulationState.status || 'idle'}
        </StatusIndicator>
      </ExperimentHeader>
      
      <Description>{experiment.description}</Description>
      
      <ControlPanel>
        {!isRunning && !isPaused && !isCompleted && (
          <Button primary onClick={handleStartExperiment}>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
              <path d="M8 5v14l11-7z" />
            </svg>
            Start Simulation
          </Button>
        )}
        
        {isRunning && (
          <Button warning onClick={pauseExperiment}>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
              <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
            </svg>
            Pause
          </Button>
        )}
        
        {isPaused && (
          <Button success onClick={resumeExperiment}>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
              <path d="M8 5v14l11-7z" />
            </svg>
            Resume
          </Button>
        )}
        
        {(isRunning || isPaused) && (
          <Button danger onClick={stopExperiment}>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
              <path d="M6 6h12v12H6z" />
            </svg>
            Stop
          </Button>
        )}
        
        {(isCompleted || Object.keys(experimentData).length > 0) && (
          <Button secondary onClick={handleGenerateReport}>
            <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
              <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z" />
            </svg>
            Generate Report
          </Button>
        )}
      </ControlPanel>
      
      <ParametersPanel>
        <ParameterGroup>
          <h3>Simulation Parameters</h3>
          {Object.entries(parameters).map(([key, value]) => (
            <ParameterRow key={key}>
              <ParameterLabel>{key}</ParameterLabel>
              <ParameterInput
                type="number"
                value={value}
                onChange={(e) => handleParameterChange(key, parseFloat(e.target.value))}
                disabled={isCompleted}
              />
            </ParameterRow>
          ))}
        </ParameterGroup>
      </ParametersPanel>
      
      <DataVisualization empty={Object.keys(experimentData).length === 0}>
        {Object.keys(experimentData).length === 0 ? (
          <NoDataMessage>
            <svg viewBox="0 0 24 24" width="48" height="48" fill="currentColor" opacity="0.5">
              <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14z" />
              <path d="M7 12h2v5H7zm4-3h2v8h-2zm4-3h2v11h-2z" />
            </svg>
            <p>No simulation data available yet. Start the simulation to see results.</p>
          </NoDataMessage>
        ) : (
          <ExperimentDashboard data={{...experimentData, parameters}} />
        )}
      </DataVisualization>
    </ExperimentContainer>
  );
};

export default ExperimentView; 