/**
 * Theme configuration for the Chemical Engineering Lab Simulator
 * This file contains both dark and light theme variants
 */

const baseTheme = {
  fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
  borderRadius: '8px',
  spacing: (multiplier = 1) => `${4 * multiplier}px`,
  transition: {
    main: 'all 0.2s ease-in-out',
  },
};

export const lightTheme = {
  ...baseTheme,
  type: 'light',
  primary: {
    main: '#1976d2',
    light: '#42a5f5',
    dark: '#1565c0',
    contrastText: '#ffffff',
  },
  secondary: {
    main: '#9c27b0',
    light: '#ba68c8',
    dark: '#7b1fa2',
    contrastText: '#ffffff',
  },
  error: {
    main: '#d32f2f',
    light: '#ef5350',
    dark: '#c62828',
    contrastText: '#ffffff',
  },
  warning: {
    main: '#ed6c02',
    light: '#ff9800',
    dark: '#e65100',
    contrastText: '#ffffff',
  },
  info: {
    main: '#0288d1',
    light: '#03a9f4',
    dark: '#01579b',
    contrastText: '#ffffff',
  },
  success: {
    main: '#2e7d32',
    light: '#4caf50',
    dark: '#1b5e20',
    contrastText: '#ffffff',
  },
  background: {
    default: '#f5f5f5',
    paper: '#ffffff',
    card: '#ffffff',
  },
  text: {
    primary: '#212121',
    secondary: '#757575',
    disabled: '#9e9e9e',
  },
  divider: 'rgba(0, 0, 0, 0.12)',
  shadow: '0 2px 10px rgba(0, 0, 0, 0.08)',
  chart: {
    colors: ['#1976d2', '#9c27b0', '#2e7d32', '#ed6c02', '#0288d1', '#d32f2f'],
  },
};

export const darkTheme = {
  ...baseTheme,
  type: 'dark',
  primary: {
    main: '#90caf9',
    light: '#e3f2fd',
    dark: '#42a5f5',
    contrastText: '#000000',
  },
  secondary: {
    main: '#ce93d8',
    light: '#f3e5f5',
    dark: '#ab47bc',
    contrastText: '#000000',
  },
  error: {
    main: '#f44336',
    light: '#e57373',
    dark: '#d32f2f',
    contrastText: '#000000',
  },
  warning: {
    main: '#ffa726',
    light: '#ffb74d',
    dark: '#f57c00',
    contrastText: '#000000',
  },
  info: {
    main: '#29b6f6',
    light: '#4fc3f7',
    dark: '#0288d1',
    contrastText: '#000000',
  },
  success: {
    main: '#66bb6a',
    light: '#81c784',
    dark: '#388e3c',
    contrastText: '#000000',
  },
  background: {
    default: '#121212',
    paper: '#1e1e1e',
    card: '#252525',
  },
  text: {
    primary: '#ffffff',
    secondary: '#b0b0b0',
    disabled: '#6c6c6c',
  },
  divider: 'rgba(255, 255, 255, 0.12)',
  shadow: '0 2px 10px rgba(0, 0, 0, 0.5)',
  chart: {
    colors: ['#90caf9', '#ce93d8', '#66bb6a', '#ffa726', '#29b6f6', '#f44336'],
  },
}; 