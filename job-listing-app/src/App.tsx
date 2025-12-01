import { useState, useEffect } from 'react';
import JobCard from './components/JobCard';
import type { Job, ApiResponse } from './types';

function App() {
  // 1. State for storing data, loading status, and errors
  const [jobs, setJobs] = useState<Job[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // 2. Fetch function wrapped in useEffect
  useEffect(() => {
    const fetchJobs = async () => {
      try {
        setIsLoading(true);
        // Fetching from the provided API endpoint
        const response = await fetch('https://akil-backend.onrender.com/opportunities/search');
        
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result: ApiResponse = await response.json();
        
        // The API wraps the array in a 'data' property
        if (result.success && Array.isArray(result.data)) {
          setJobs(result.data);
        } else {
          throw new Error('Invalid data structure received from API');
        }
      } catch (err) {
        // 3. Error handling
        console.error("Failed to fetch jobs:", err);
        setError('Failed to load job opportunities. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchJobs();
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 font-sans">
      {/* Header Section */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
             <div className="w-8 h-8 bg-primary rounded-full flex items-center justify-center text-white font-bold">
              J
            </div>
            <span className="text-xl font-bold text-slate-800 tracking-tight">JobFinder</span>
          </div>
          <nav className="hidden md:flex gap-6 text-sm font-medium text-slate-600">
            <a href="#" className="text-primary">Find Jobs</a>
            <a href="#" className="hover:text-primary">Companies</a>
            <a href="#" className="hover:text-primary">Salaries</a>
          </nav>
          <div className="flex gap-3">
             <button className="text-sm font-bold text-primary px-4 py-2 rounded hover:bg-indigo-50">
              Login
            </button>
            <button className="text-sm font-bold text-white bg-primary px-4 py-2 rounded hover:bg-indigo-700">
              Sign Up
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        
        {/* Title Section */}
        <div className="mb-8 flex justify-between items-end">
          <div>
            <h1 className="text-3xl font-bold text-slate-800 mb-2">
              Opportunities
            </h1>
            <p className="text-slate-600">
              Showing {jobs.length} results
            </p>
          </div>
           <div className="text-slate-500 text-sm">
             Sort by: <span className="font-semibold text-slate-800">Most Relevant</span> 
           </div>
        </div>

        {/* 4. Conditional Rendering for Loading and Error States */}
        {isLoading && (
          <div className="flex justify-center items-center h-64">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg text-center">
            <p className="font-medium">Error</p>
            <p>{error}</p>
            <button 
              onClick={() => window.location.reload()} 
              className="mt-2 text-sm underline hover:text-red-800"
            >
              Retry
            </button>
          </div>
        )}

        {/* Grid Layout for Job Cards */}
        {!isLoading && !error && (
          <div className="flex flex-col gap-6">
            {jobs.map((job) => (
              <JobCard key={job.id} job={job} />
            ))}
            
            {jobs.length === 0 && (
              <p className="text-center text-slate-500 py-10">No jobs found.</p>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;