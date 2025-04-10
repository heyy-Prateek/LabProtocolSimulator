import React, { useMemo } from 'react';
import styled from 'styled-components';

const ChartContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
`;

const ChartHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
`;

const ChartTitle = styled.h3`
  font-size: 16px;
  margin: 0;
  color: ${props => props.theme.text.primary};
`;

const ChartControls = styled.div`
  display: flex;
  gap: 10px;
`;

const ChartSelect = styled.select`
  padding: 5px 10px;
  border-radius: 4px;
  border: 1px solid ${props => props.theme.divider};
  background-color: ${props => props.theme.background.paper};
  color: ${props => props.theme.text.primary};
  font-size: 14px;
  
  &:focus {
    outline: none;
    border-color: ${props => props.theme.primary.main};
  }
`;

const ChartCanvas = styled.div`
  flex: 1;
  min-height: 200px;
  position: relative;
  
  canvas {
    width: 100% !important;
    height: 100% !important;
  }
`;

const NoDataText = styled.div`
  display: flex;
  height: 100%;
  align-items: center;
  justify-content: center;
  color: ${props => props.theme.text.disabled};
`;

/**
 * Component for visualizing experiment data
 */
const ExperimentChart = ({ data, type = 'concentration' }) => {
  // Prepare chart data
  const chartData = useMemo(() => {
    if (!data) return null;
    
    // Extract relevant data based on chart type
    switch (type) {
      case 'concentration':
        if (!data.times || !data.conc_a || !data.conc_b) return null;
        
        return {
          labels: data.times,
          datasets: [
            {
              label: 'Concentration A',
              data: data.conc_a,
              borderColor: '#4CAF50',
              backgroundColor: 'rgba(76, 175, 80, 0.1)',
              borderWidth: 2,
              pointRadius: 0,
              tension: 0.3,
            },
            {
              label: 'Concentration B',
              data: data.conc_b,
              borderColor: '#2196F3',
              backgroundColor: 'rgba(33, 150, 243, 0.1)',
              borderWidth: 2,
              pointRadius: 0,
              tension: 0.3,
            }
          ]
        };
        
      case 'conversion':
        if (!data.times || !data.conversion_history) return null;
        
        return {
          labels: data.times,
          datasets: [
            {
              label: 'Conversion (%)',
              data: data.conversion_history,
              borderColor: '#F44336',
              backgroundColor: 'rgba(244, 67, 54, 0.1)',
              borderWidth: 2,
              pointRadius: 0,
              tension: 0.3,
            }
          ]
        };
        
      case 'rate':
        if (!data.times) return null;
        
        // Calculate reaction rate at each time point
        const reactionRates = data.times.map((time, index) => {
          if (!data.conc_a || index >= data.conc_a.length) return 0;
          // Rate = k * [A]
          return data.parameters?.rate_constant * data.conc_a[index];
        });
        
        return {
          labels: data.times,
          datasets: [
            {
              label: 'Reaction Rate',
              data: reactionRates,
              borderColor: '#9C27B0',
              backgroundColor: 'rgba(156, 39, 176, 0.1)',
              borderWidth: 2,
              pointRadius: 0,
              tension: 0.3,
            }
          ]
        };
        
      default:
        return null;
    }
  }, [data, type]);
  
  // Chart options
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
      },
      tooltip: {
        mode: 'index',
        intersect: false,
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Time (min)',
        },
        grid: {
          display: true,
          drawOnChartArea: true,
          drawTicks: true,
          color: 'rgba(200, 200, 200, 0.2)',
        },
      },
      y: {
        title: {
          display: true,
          text: type === 'concentration' ? 'Concentration (mol/L)' : 
                type === 'conversion' ? 'Conversion (%)' : 
                'Rate (mol/L·min)',
        },
        beginAtZero: true,
        grid: {
          display: true,
          drawOnChartArea: true,
          drawTicks: true,
          color: 'rgba(200, 200, 200, 0.2)',
        },
      },
    },
    interaction: {
      mode: 'nearest',
      axis: 'x',
      intersect: false,
    },
    animation: {
      duration: 500,
    },
  };
  
  // Render chart based on whether data is available
  const renderChart = () => {
    if (!chartData) {
      return <NoDataText>No data available for visualization</NoDataText>;
    }
    
    // Use a simple SVG-based visualization for demo purposes
    // In a real app, you would use a proper charting library like Chart.js or Recharts
    return (
      <ChartCanvas>
        <svg width="100%" height="100%" viewBox="0 0 1000 400">
          {/* Draw axes */}
          <line x1="50" y1="350" x2="950" y2="350" stroke="#666" strokeWidth="2" />
          <line x1="50" y1="50" x2="50" y2="350" stroke="#666" strokeWidth="2" />
          
          {/* X-axis label */}
          <text x="500" y="390" textAnchor="middle" fill="#666">Time (min)</text>
          
          {/* Y-axis label */}
          <text x="15" y="200" textAnchor="middle" fill="#666" transform="rotate(-90, 15, 200)">
            {type === 'concentration' ? 'Concentration (mol/L)' : 
             type === 'conversion' ? 'Conversion (%)' : 
             'Rate (mol/L·min)'}
          </text>
          
          {/* Draw data lines */}
          {chartData.datasets.map((dataset, index) => {
            // Calculate points for the polyline
            if (!dataset.data || dataset.data.length === 0) return null;
            
            const maxValue = Math.max(...dataset.data);
            const numPoints = dataset.data.length;
            
            // Create path for the dataset
            const points = dataset.data.map((value, i) => {
              const x = 50 + (900 * i) / (numPoints - 1);
              const y = 350 - (300 * value) / (maxValue || 1);
              return `${x},${y}`;
            }).join(' ');
            
            return (
              <g key={index}>
                <polyline
                  points={points}
                  fill="none"
                  stroke={dataset.borderColor}
                  strokeWidth="2"
                />
                
                {/* Legend item */}
                <rect
                  x={800}
                  y={50 + index * 25}
                  width="15"
                  height="15"
                  fill={dataset.borderColor}
                />
                <text
                  x={820}
                  y={62 + index * 25}
                  fill="#666"
                  fontSize="12"
                >
                  {dataset.label}
                </text>
              </g>
            );
          })}
        </svg>
      </ChartCanvas>
    );
  };
  
  return (
    <ChartContainer>
      <ChartHeader>
        <ChartTitle>
          {type === 'concentration' ? 'Concentration vs Time' : 
           type === 'conversion' ? 'Conversion vs Time' : 
           'Reaction Rate vs Time'}
        </ChartTitle>
      </ChartHeader>
      {renderChart()}
    </ChartContainer>
  );
};

export default ExperimentChart; 