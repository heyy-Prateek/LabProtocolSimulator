import React from 'react';
import styled from 'styled-components';

const AboutContainer = styled.div`
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

const Paragraph = styled.p`
  margin-bottom: 1rem;
  line-height: 1.6;
`;

const List = styled.ul`
  margin-left: 1.5rem;
  margin-bottom: 1rem;
  
  li {
    margin-bottom: 0.5rem;
  }
`;

const TeamMember = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
`;

const Avatar = styled.div`
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: ${({ theme }) => theme.primary};
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin-right: 1rem;
`;

const MemberInfo = styled.div`
  flex: 1;
`;

const MemberName = styled.h3`
  margin: 0 0 0.25rem 0;
  color: ${({ theme }) => theme.primary};
`;

const MemberRole = styled.p`
  margin: 0;
  color: ${({ theme }) => theme.textSecondary};
  font-style: italic;
`;

function About() {
  return (
    <AboutContainer>
      <Title>About the Chemical Engineering Laboratory Simulator</Title>
      
      <Section>
        <SubTitle>Overview</SubTitle>
        <Paragraph>
          The Chemical Engineering Laboratory Simulator is an educational tool designed to provide students and professionals with a virtual environment to practice chemical engineering experiments and simulations. This platform offers a hands-on approach to learning without the need for physical laboratory equipment.
        </Paragraph>
        <Paragraph>
          Our simulator allows users to explore various chemical engineering principles, conduct virtual experiments, analyze data, and generate comprehensive reports—all within a user-friendly interface.
        </Paragraph>
      </Section>
      
      <Section>
        <SubTitle>Key Features</SubTitle>
        <List>
          <li><strong>Interactive Experiments:</strong> Conduct various chemical engineering experiments in a virtual environment.</li>
          <li><strong>Real-time Simulations:</strong> Observe how changes in parameters affect experimental outcomes.</li>
          <li><strong>Data Visualization:</strong> Analyze experimental data through intuitive charts and graphs.</li>
          <li><strong>Report Generation:</strong> Create detailed reports of your experimental findings.</li>
          <li><strong>Educational Content:</strong> Access theoretical background and procedural information for each experiment.</li>
          <li><strong>AI-Assisted Learning:</strong> Get help from our AI assistant for conceptual questions and troubleshooting.</li>
        </List>
      </Section>
      
      <Section>
        <SubTitle>Our Mission</SubTitle>
        <Paragraph>
          Our mission is to make chemical engineering education more accessible, engaging, and effective. By providing a virtual laboratory experience, we aim to:
        </Paragraph>
        <List>
          <li>Bridge the gap between theoretical knowledge and practical application</li>
          <li>Enable learning in environments where physical laboratory resources are limited</li>
          <li>Reduce the cost and safety risks associated with traditional laboratory experiments</li>
          <li>Prepare students for real-world chemical engineering challenges</li>
        </List>
      </Section>
      
      <Section>
        <SubTitle>Technical Information</SubTitle>
        <Paragraph>
          The Chemical Engineering Laboratory Simulator is built using a combination of modern technologies:
        </Paragraph>
        <List>
          <li><strong>Frontend:</strong> React, styled-components</li>
          <li><strong>Backend:</strong> Python, FastAPI</li>
          <li><strong>Simulation Engine:</strong> Custom numerical solvers built with NumPy, SciPy</li>
          <li><strong>Data Visualization:</strong> Recharts, Matplotlib</li>
          <li><strong>AI Assistant:</strong> Large Language Model integration</li>
        </List>
      </Section>
      
      <Section>
        <SubTitle>Development Team</SubTitle>
        <TeamMember>
          <Avatar>JD</Avatar>
          <MemberInfo>
            <MemberName>Dr. Jane Doe</MemberName>
            <MemberRole>Lead Chemical Engineer</MemberRole>
          </MemberInfo>
        </TeamMember>
        
        <TeamMember>
          <Avatar>JS</Avatar>
          <MemberInfo>
            <MemberName>John Smith</MemberName>
            <MemberRole>Software Developer</MemberRole>
          </MemberInfo>
        </TeamMember>
        
        <TeamMember>
          <Avatar>AR</Avatar>
          <MemberInfo>
            <MemberName>Alex Rodriguez</MemberName>
            <MemberRole>UX/UI Designer</MemberRole>
          </MemberInfo>
        </TeamMember>
        
        <TeamMember>
          <Avatar>MP</Avatar>
          <MemberInfo>
            <MemberName>Maria Patel</MemberName>
            <MemberRole>Educational Content Developer</MemberRole>
          </MemberInfo>
        </TeamMember>
      </Section>
      
      <Section>
        <SubTitle>Version Information</SubTitle>
        <Paragraph>
          <strong>Current Version:</strong> 1.0.0
        </Paragraph>
        <Paragraph>
          <strong>Last Updated:</strong> {new Date().toLocaleDateString()}
        </Paragraph>
        <Paragraph>
          <strong>License:</strong> MIT
        </Paragraph>
      </Section>
    </AboutContainer>
  );
}

export default About; 