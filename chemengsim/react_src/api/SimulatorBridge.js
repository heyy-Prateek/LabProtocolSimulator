import { createContext, useContext, useState, useCallback } from 'react';

// Create a context for the simulator bridge
const SimulatorBridgeContext = createContext(null);

// API base URL
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? window.location.origin + '/api'  // In production, use same origin
  : 'http://localhost:8000';         // In development, use port 8000

/**
 * SimulatorBridge provides API communication between the React frontend
 * and the Python backend simulator.
 */
export const SimulatorBridgeProvider = ({ children }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Generic API request function
   */
  const apiRequest = useCallback(async (endpoint, method = 'GET', data = null) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const options = {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
      };
      
      if (data) {
        options.body = JSON.stringify(data);
      }
      
      const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `API request failed with status ${response.status}`);
      }
      
      // For no-content responses
      if (response.status === 204) {
        return null;
      }
      
      return await response.json();
    } catch (err) {
      setError(err.message);
      console.error('API request error:', err);
      return null;
    } finally {
      setIsLoading(false);
    }
  }, []);
  
  /**
   * Get list of available experiments
   */
  const getExperiments = useCallback(async () => {
    return apiRequest('/experiments');
  }, [apiRequest]);
  
  /**
   * Get details of a specific experiment
   */
  const getExperiment = useCallback(async (experimentId) => {
    return apiRequest(`/experiments/${experimentId}`);
  }, [apiRequest]);
  
  /**
   * Start a new simulation with the given parameters
   */
  const startSimulation = useCallback(async (experimentId, parameters) => {
    return apiRequest(`/experiments/${experimentId}/start`, 'POST', parameters);
  }, [apiRequest]);
  
  /**
   * Get current simulation data
   */
  const getSimulationData = useCallback(async (simulationId) => {
    return apiRequest(`/simulations/${simulationId}`);
  }, [apiRequest]);
  
  /**
   * Update simulation parameters during runtime
   */
  const updateSimulation = useCallback(async (simulationId, parameters) => {
    return apiRequest(`/simulations/${simulationId}`, 'PUT', parameters);
  }, [apiRequest]);
  
  /**
   * Stop a running simulation
   */
  const stopSimulation = useCallback(async (simulationId) => {
    return apiRequest(`/simulations/${simulationId}/stop`, 'POST');
  }, [apiRequest]);
  
  /**
   * Generate a report for a completed simulation
   */
  const generateReport = useCallback(async (simulationId, format = 'pdf') => {
    return apiRequest(`/simulations/${simulationId}/report?format=${format}`, 'GET');
  }, [apiRequest]);
  
  /**
   * Submit quiz answers for evaluation
   */
  const submitQuiz = useCallback(async (quizId, answers) => {
    return apiRequest(`/quizzes/${quizId}/submit`, 'POST', { answers });
  }, [apiRequest]);
  
  /**
   * Ask a question to the simulator's assistant
   */
  const askAssistant = useCallback(async (question, context = {}) => {
    return apiRequest('/assistant/ask', 'POST', { question, context });
  }, [apiRequest]);
  
  // The bridge value that will be provided to the context
  const bridge = {
    isLoading,
    error,
    getExperiments,
    getExperiment,
    startSimulation,
    getSimulationData,
    updateSimulation,
    stopSimulation,
    generateReport,
    submitQuiz,
    askAssistant
  };
  
  return (
    <SimulatorBridgeContext.Provider value={bridge}>
      {children}
    </SimulatorBridgeContext.Provider>
  );
};

/**
 * Custom hook to use the simulator bridge
 */
export const useSimulatorBridge = () => {
  const context = useContext(SimulatorBridgeContext);
  if (!context) {
    throw new Error('useSimulatorBridge must be used within a SimulatorBridgeProvider');
  }
  return context;
}; 