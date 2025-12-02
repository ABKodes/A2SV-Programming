import { render, screen, fireEvent } from '@testing-library/react';
import JobCard from '../JobCard';
import type { Job } from '../../types';

// Mock data for the test
const mockJob: Job = {
  id: '1',
  title: 'Software Engineer',
  description: 'Test Description',
  orgName: 'Test Org',
  location: ['New York'],
  logoUrl: '',
  opType: 'Full-Time',
  categories: ['Tech'],
  members: 0,
  createdAt: '',
  updatedAt: '',
  status: 'active',
  deadline: ''
};

describe('JobCard Component', () => {
  test('renders job title and organization', () => {
    render(<JobCard job={mockJob} isBookmarked={false} onToggleBookmark={() => {}} />);
    
    // Check if the text appears on the screen
    expect(screen.getByText('Software Engineer')).toBeInTheDocument();
    expect(screen.getByText(/Test Org/)).toBeInTheDocument();
  });

  test('calls onToggleBookmark when bookmark button is clicked', () => {
    const mockToggle = jest.fn(); // Create a fake function to track clicks
    render(<JobCard job={mockJob} isBookmarked={false} onToggleBookmark={mockToggle} />);
    
    // Find the button by the test ID we added in JobCard.tsx
    const button = screen.getByTestId('bookmark-btn');
    fireEvent.click(button);
    
    // Verify the function was called exactly once with the correct ID
    expect(mockToggle).toHaveBeenCalledTimes(1);
    expect(mockToggle).toHaveBeenCalledWith('1');
  });
});