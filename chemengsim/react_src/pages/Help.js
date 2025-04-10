import React, { useState } from 'react';
import styled from 'styled-components';

const HelpContainer = styled.div`
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
`;

const Title = styled.h1`
  color: ${({ theme }) => theme.primary};
  margin-bottom: 2rem;
`;

const TabContainer = styled.div`
  display: flex;
  border-bottom: 1px solid ${({ theme }) => theme.border};
  margin-bottom: 2rem;
`;

const Tab = styled.button`
  padding: 0.75rem 1.5rem;
  border: none;
  background-color: ${({ active, theme }) => 
    active ? theme.primary : 'transparent'};
  color: ${({ active, theme }) => 
    active ? 'white' : theme.text};
  border-radius: 4px 4px 0 0;
  cursor: pointer;
  font-weight: ${({ active }) => active ? 'bold' : 'normal'};
  transition: all 0.2s ease;
  
  &:hover {
    background-color: ${({ active, theme }) => 
      active ? theme.primary : theme.backgroundAlt};
  }
  
  &:not(:last-child) {
    margin-right: 0.5rem;
  }
`;

const ContentSection = styled.section`
  background-color: ${({ theme }) => theme.cardBackground};
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const Topic = styled.div`
  margin-bottom: 2.5rem;
  
  &:last-child {
    margin-bottom: 0;
  }
`;

const TopicTitle = styled.h2`
  color: ${({ theme }) => theme.secondary};
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  
  &::before {
    content: "→";
    margin-right: 0.5rem;
    color: ${({ theme }) => theme.primary};
  }
`;

const Paragraph = styled.p`
  margin-bottom: 1rem;
  line-height: 1.6;
`;

const List = styled.ul`
  margin-left: 2rem;
  margin-bottom: 1.5rem;
  
  li {
    margin-bottom: 0.75rem;
  }
`;

const StepList = styled.ol`
  margin-left: 2rem;
  margin-bottom: 1.5rem;
  counter-reset: steps;
  
  li {
    margin-bottom: 1rem;
    position: relative;
    
    &::before {
      counter-increment: steps;
      content: counter(steps);
      position: absolute;
      left: -2rem;
      top: -0.25rem;
      width: 1.5rem;
      height: 1.5rem;
      background-color: ${({ theme }) => theme.primary};
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: bold;
    }
  }
`;

const FAQItem = styled.div`
  margin-bottom: 1.5rem;
  border-bottom: 1px solid ${({ theme }) => theme.border};
  padding-bottom: 1.5rem;
  
  &:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
  }
`;

const Question = styled.h3`
  margin-bottom: 0.75rem;
  color: ${({ theme }) => theme.primary};
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  
  &:hover {
    color: ${({ theme }) => theme.secondary};
  }
`;

const Answer = styled.div`
  padding-left: 0.5rem;
  border-left: 3px solid ${({ theme }) => theme.primary};
`;

const Tip = styled.div`
  background-color: ${({ theme }) => theme.backgroundAlt};
  padding: 1rem;
  border-left: 4px solid ${({ theme }) => theme.secondary};
  margin: 1.5rem 0;
  border-radius: 0 4px 4px 0;
`;

const TipTitle = styled.h4`
  margin-bottom: 0.5rem;
  color: ${({ theme }) => theme.secondary};
`;

function Help() {
  const [activeTab, setActiveTab] = useState('getting-started');
  const [expandedFaqs, setExpandedFaqs] = useState({});
  
  const toggleFAQ = (id) => {
    setExpandedFaqs({
      ...expandedFaqs,
      [id]: !expandedFaqs[id]
    });
  };
  
  return (
    <HelpContainer>
      <Title>Help & Documentation</Title>
      
      <TabContainer>
        <Tab 
          active={activeTab === 'getting-started'} 
          onClick={() => setActiveTab('getting-started')}
        >
          Getting Started
        </Tab>
        <Tab 
          active={activeTab === 'experiments'} 
          onClick={() => setActiveTab('experiments')}
        >
          Running Experiments
        </Tab>
        <Tab 
          active={activeTab === 'features'} 
          onClick={() => setActiveTab('features')}
        >
          Features Guide
        </Tab>
        <Tab 
          active={activeTab === 'faq'} 
          onClick={() => setActiveTab('faq')}
        >
          FAQ
        </Tab>
      </TabContainer>
      
      <ContentSection>
        {activeTab === 'getting-started' && (
          <>
            <Topic>
              <TopicTitle>Welcome to the Simulator</TopicTitle>
              <Paragraph>
                The Chemical Engineering Laboratory Simulator is designed to provide a virtual environment for conducting chemical engineering experiments. This guide will help you get started with using the simulator.
              </Paragraph>
              <Paragraph>
                Whether you're a student learning the basics or a professional refreshing your knowledge, our simulator offers a safe, accessible way to practice and understand key chemical engineering concepts.
              </Paragraph>
            </Topic>
            
            <Topic>
              <TopicTitle>System Requirements</TopicTitle>
              <Paragraph>
                To ensure the simulator runs smoothly, make sure your system meets these requirements:
              </Paragraph>
              <List>
                <li><strong>Operating System:</strong> Windows 10/11, macOS 10.14+, or Linux</li>
                <li><strong>Browser:</strong> Latest version of Chrome, Firefox, Safari, or Edge</li>
                <li><strong>Internet Connection:</strong> Required for API features</li>
                <li><strong>Display:</strong> Minimum resolution of 1280 × 720</li>
                <li><strong>Hardware:</strong> 4GB RAM, dual-core processor</li>
              </List>
            </Topic>
            
            <Topic>
              <TopicTitle>Quick Start Guide</TopicTitle>
              <StepList>
                <li>
                  <strong>Navigate to the Dashboard:</strong> The dashboard shows all available experiments. Click on any experiment tile to view details and start the simulation.
                </li>
                <li>
                  <strong>Experiment Setup:</strong> Configure your experiment parameters in the setup panel. Each parameter has a description and default values.
                </li>
                <li>
                  <strong>Run the Simulation:</strong> Click the "Start Simulation" button to begin. You can pause or stop the simulation at any time.
                </li>
                <li>
                  <strong>Analyze Results:</strong> Once the simulation is complete, view the data visualization tab to see graphs and numerical results.
                </li>
                <li>
                  <strong>Generate Reports:</strong> Use the report generation feature to create a PDF or HTML report of your experiment results.
                </li>
              </StepList>
              
              <Tip>
                <TipTitle>Pro Tip</TipTitle>
                <Paragraph>
                  Use the dark mode toggle in the settings to reduce eye strain during extended sessions. You can also save your experiment configurations for future use.
                </Paragraph>
              </Tip>
            </Topic>
          </>
        )}
        
        {activeTab === 'experiments' && (
          <>
            <Topic>
              <TopicTitle>Available Experiments</TopicTitle>
              <Paragraph>
                The simulator currently offers the following experiments:
              </Paragraph>
              <List>
                <li><strong>Batch Reactor:</strong> Simulate chemical reactions in a batch reactor with adjustable parameters.</li>
                <li><strong>Continuous Stirred-Tank Reactor (CSTR):</strong> Study steady-state and dynamic behavior of a CSTR.</li>
                <li><strong>Plug Flow Reactor (PFR):</strong> Analyze concentration profiles in a tubular reactor.</li>
                <li><strong>Distillation Column:</strong> Investigate separation of binary mixtures.</li>
                <li><strong>Heat Exchanger:</strong> Examine heat transfer between fluids.</li>
              </List>
            </Topic>
            
            <Topic>
              <TopicTitle>Conducting an Experiment</TopicTitle>
              <StepList>
                <li>
                  <strong>Select an Experiment:</strong> From the dashboard, click on the experiment you wish to conduct.
                </li>
                <li>
                  <strong>Review Theory:</strong> Read the background information provided to understand the key concepts.
                </li>
                <li>
                  <strong>Configure Parameters:</strong> Adjust the experimental parameters according to your learning objectives.
                </li>
                <li>
                  <strong>Run Simulation:</strong> Start the simulation and observe the real-time changes in the system.
                </li>
                <li>
                  <strong>Interpret Results:</strong> Analyze the graphs and data tables to draw conclusions about the experiment.
                </li>
                <li>
                  <strong>Save or Export:</strong> Save your experiment configuration or export results for further analysis.
                </li>
              </StepList>
            </Topic>
            
            <Topic>
              <TopicTitle>Understanding Simulation Controls</TopicTitle>
              <Paragraph>
                Each experiment includes various control options:
              </Paragraph>
              <List>
                <li><strong>Start:</strong> Begins the simulation with the current parameters.</li>
                <li><strong>Pause:</strong> Temporarily halts the simulation while preserving the current state.</li>
                <li><strong>Reset:</strong> Returns all parameters to their default values.</li>
                <li><strong>Step Forward:</strong> Advances the simulation by one time step (available in some experiments).</li>
                <li><strong>Speed Control:</strong> Adjusts the speed of the simulation.</li>
              </List>
              
              <Tip>
                <TipTitle>Pro Tip</TipTitle>
                <Paragraph>
                  For more accurate results, start with small parameter changes and observe their effects before making larger adjustments.
                </Paragraph>
              </Tip>
            </Topic>
          </>
        )}
        
        {activeTab === 'features' && (
          <>
            <Topic>
              <TopicTitle>Data Visualization</TopicTitle>
              <Paragraph>
                The simulator offers various visualization tools to help you understand experimental results:
              </Paragraph>
              <List>
                <li><strong>Line Graphs:</strong> Show changes in variables over time.</li>
                <li><strong>Bar Charts:</strong> Compare values across different conditions.</li>
                <li><strong>Heat Maps:</strong> Visualize temperature or concentration distributions.</li>
                <li><strong>3D Plots:</strong> Examine relationships between multiple variables.</li>
                <li><strong>Data Tables:</strong> View numerical data in tabular format.</li>
              </List>
              <Paragraph>
                To customize visualizations, use the options panel next to each graph. You can select variables, adjust axes, and change display settings.
              </Paragraph>
            </Topic>
            
            <Topic>
              <TopicTitle>Report Generation</TopicTitle>
              <Paragraph>
                Generate comprehensive reports of your experiments with the following steps:
              </Paragraph>
              <StepList>
                <li>Complete your experiment and ensure all data is collected.</li>
                <li>Navigate to the "Reports" tab in the experiment view.</li>
                <li>Select the sections you want to include in your report (e.g., methodology, results, discussion).</li>
                <li>Choose the format (PDF, HTML, or Word).</li>
                <li>Click "Generate Report" and wait for processing.</li>
                <li>Download or directly print your report.</li>
              </StepList>
            </Topic>
            
            <Topic>
              <TopicTitle>AI Assistant</TopicTitle>
              <Paragraph>
                The built-in AI assistant can help you with:
              </Paragraph>
              <List>
                <li><strong>Conceptual Questions:</strong> Explanations of chemical engineering principles.</li>
                <li><strong>Procedural Guidance:</strong> Step-by-step instructions for conducting experiments.</li>
                <li><strong>Result Interpretation:</strong> Help understanding experimental outcomes.</li>
                <li><strong>Troubleshooting:</strong> Solutions for common issues.</li>
              </List>
              <Paragraph>
                To use the AI assistant, click the chat icon in the bottom right corner of the interface and type your question. The assistant will respond based on built-in knowledge or using an API if enabled in settings.
              </Paragraph>
            </Topic>
          </>
        )}
        
        {activeTab === 'faq' && (
          <>
            <Topic>
              <TopicTitle>Frequently Asked Questions</TopicTitle>
              
              <FAQItem>
                <Question onClick={() => toggleFAQ('faq1')}>
                  How accurate are the simulations compared to real lab experiments?
                  {expandedFaqs['faq1'] ? '−' : '+'}
                </Question>
                {expandedFaqs['faq1'] && (
                  <Answer>
                    <Paragraph>
                      Our simulations are based on established mathematical models and principles of chemical engineering. While they provide a high degree of accuracy for educational purposes, they may not account for all real-world variables and conditions that might affect experimental outcomes in an actual laboratory. 
                    </Paragraph>
                    <Paragraph>
                      The simulator is designed primarily as an educational tool to help understand concepts and trends, rather than to produce results that match specific industrial equipment or conditions with perfect accuracy.
                    </Paragraph>
                  </Answer>
                )}
              </FAQItem>
              
              <FAQItem>
                <Question onClick={() => toggleFAQ('faq2')}>
                  Can I save my experiment progress and continue later?
                  {expandedFaqs['faq2'] ? '−' : '+'}
                </Question>
                {expandedFaqs['faq2'] && (
                  <Answer>
                    <Paragraph>
                      Yes, you can save your experiment configurations and results. In the experiment view, use the "Save" button to store your current setup and progress. When you return to the simulator, go to "Saved Experiments" in the dashboard to continue where you left off.
                    </Paragraph>
                  </Answer>
                )}
              </FAQItem>
              
              <FAQItem>
                <Question onClick={() => toggleFAQ('faq3')}>
                  Why am I getting unrealistic results in my simulation?
                  {expandedFaqs['faq3'] ? '−' : '+'}
                </Question>
                {expandedFaqs['faq3'] && (
                  <Answer>
                    <Paragraph>
                      Unrealistic results can occur for several reasons:
                    </Paragraph>
                    <List>
                      <li><strong>Extreme Parameter Values:</strong> Setting parameters to values far outside typical ranges can lead to numerical instabilities.</li>
                      <li><strong>Incompatible Combinations:</strong> Some combinations of parameters may not be physically reasonable.</li>
                      <li><strong>Model Limitations:</strong> The underlying models have assumptions and limitations that may not accommodate certain scenarios.</li>
                    </List>
                    <Paragraph>
                      Try resetting parameters to default values and make incremental changes to identify where the issue begins. If problems persist, consult the AI assistant for specific guidance.
                    </Paragraph>
                  </Answer>
                )}
              </FAQItem>
              
              <FAQItem>
                <Question onClick={() => toggleFAQ('faq4')}>
                  Does the simulator require an internet connection?
                  {expandedFaqs['faq4'] ? '−' : '+'}
                </Question>
                {expandedFaqs['faq4'] && (
                  <Answer>
                    <Paragraph>
                      The core simulator functionality works offline, but certain features require an internet connection:
                    </Paragraph>
                    <List>
                      <li>AI assistant when using API mode</li>
                      <li>Accessing cloud-saved experiments</li>
                      <li>Receiving application updates</li>
                      <li>Sharing reports via email</li>
                    </List>
                    <Paragraph>
                      If you plan to use the simulator in an environment without internet access, make sure to download any necessary resources beforehand.
                    </Paragraph>
                  </Answer>
                )}
              </FAQItem>
              
              <FAQItem>
                <Question onClick={() => toggleFAQ('faq5')}>
                  How can I suggest a new experiment to be added to the simulator?
                  {expandedFaqs['faq5'] ? '−' : '+'}
                </Question>
                {expandedFaqs['faq5'] && (
                  <Answer>
                    <Paragraph>
                      We welcome suggestions for new experiments! To submit your idea:
                    </Paragraph>
                    <StepList>
                      <li>Go to the "About" page in the application.</li>
                      <li>Click on the "Contact Us" button.</li>
                      <li>Fill out the form, selecting "Feature Request" as the category.</li>
                      <li>Describe the experiment you'd like to see added, including its educational value and key parameters.</li>
                    </StepList>
                    <Paragraph>
                      Our development team regularly reviews suggestions and prioritizes new experiments based on educational value and implementation feasibility.
                    </Paragraph>
                  </Answer>
                )}
              </FAQItem>
            </Topic>
          </>
        )}
      </ContentSection>
    </HelpContainer>
  );
}

export default Help; 