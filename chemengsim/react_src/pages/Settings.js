import React, { useState, useContext } from 'react';
import styled from 'styled-components';
import { ThemeContext } from '../components/ThemeProvider';

const SettingsContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
`;

const Title = styled.h1`
  color: ${({ theme }) => theme.primary};
  margin-bottom: 2rem;
`;

const Section = styled.section`
  margin-bottom: 2rem;
  background-color: ${({ theme }) => theme.cardBackground};
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const SubTitle = styled.h2`
  color: ${({ theme }) => theme.secondary};
  margin-bottom: 1rem;
`;

const SettingRow = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid ${({ theme }) => theme.borderColor};
  
  &:last-child {
    border-bottom: none;
  }
`;

const SettingLabel = styled.label`
  font-weight: 500;
`;

const SettingDescription = styled.p`
  margin-top: 0.25rem;
  font-size: 0.875rem;
  color: ${({ theme }) => theme.textSecondary};
`;

const Toggle = styled.label`
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
  
  input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  span {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
    border-radius: 34px;
    
    &:before {
      position: absolute;
      content: "";
      height: 26px;
      width: 26px;
      left: 4px;
      bottom: 4px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }
  }
  
  input:checked + span {
    background-color: ${({ theme }) => theme.primary};
  }
  
  input:checked + span:before {
    transform: translateX(26px);
  }
`;

const Select = styled.select`
  padding: 0.5rem;
  border: 1px solid ${({ theme }) => theme.borderColor};
  border-radius: 4px;
  background-color: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.text};
`;

const Button = styled.button`
  background-color: ${({ theme }) => theme.primary};
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  
  &:hover {
    background-color: ${({ theme }) => theme.primaryDark};
  }
`;

function Settings() {
  const { theme, toggleTheme } = useContext(ThemeContext);
  const [useAPI, setUseAPI] = useState(false);
  const [autoSave, setAutoSave] = useState(true);
  const [units, setUnits] = useState('SI');
  const [apiKey, setApiKey] = useState('');
  
  const handleSaveSettings = () => {
    // Mock function to save settings
    localStorage.setItem('chem_sim_settings', JSON.stringify({
      useAPI,
      autoSave,
      units
    }));
    
    alert('Settings saved successfully!');
  };
  
  return (
    <SettingsContainer>
      <Title>Settings</Title>
      
      <Section>
        <SubTitle>Appearance</SubTitle>
        <SettingRow>
          <div>
            <SettingLabel>Dark Mode</SettingLabel>
            <SettingDescription>Switch between light and dark themes</SettingDescription>
          </div>
          <Toggle>
            <input 
              type="checkbox" 
              checked={theme === 'dark'} 
              onChange={toggleTheme} 
            />
            <span></span>
          </Toggle>
        </SettingRow>
      </Section>
      
      <Section>
        <SubTitle>API Settings</SubTitle>
        <SettingRow>
          <div>
            <SettingLabel>Use External API</SettingLabel>
            <SettingDescription>Connect to external API for advanced simulation capabilities</SettingDescription>
          </div>
          <Toggle>
            <input 
              type="checkbox" 
              checked={useAPI} 
              onChange={() => setUseAPI(!useAPI)} 
            />
            <span></span>
          </Toggle>
        </SettingRow>
        
        {useAPI && (
          <SettingRow>
            <div>
              <SettingLabel>API Key</SettingLabel>
              <SettingDescription>Enter your API key for external services</SettingDescription>
            </div>
            <input 
              type="password" 
              value={apiKey} 
              onChange={(e) => setApiKey(e.target.value)}
              style={{ padding: '0.5rem', borderRadius: '4px', border: '1px solid #ccc' }}
            />
          </SettingRow>
        )}
      </Section>
      
      <Section>
        <SubTitle>Simulation Preferences</SubTitle>
        <SettingRow>
          <div>
            <SettingLabel>Auto-save Results</SettingLabel>
            <SettingDescription>Automatically save simulation results</SettingDescription>
          </div>
          <Toggle>
            <input 
              type="checkbox" 
              checked={autoSave} 
              onChange={() => setAutoSave(!autoSave)} 
            />
            <span></span>
          </Toggle>
        </SettingRow>
        
        <SettingRow>
          <div>
            <SettingLabel>Units System</SettingLabel>
            <SettingDescription>Choose your preferred units system</SettingDescription>
          </div>
          <Select value={units} onChange={(e) => setUnits(e.target.value)}>
            <option value="SI">SI Units (kg, m, s)</option>
            <option value="Imperial">Imperial Units (lb, ft, s)</option>
            <option value="CGS">CGS Units (g, cm, s)</option>
          </Select>
        </SettingRow>
      </Section>
      
      <Button onClick={handleSaveSettings}>Save Settings</Button>
    </SettingsContainer>
  );
}

export default Settings; 