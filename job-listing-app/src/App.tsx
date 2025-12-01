import { useState, useEffect } from 'react';
import JobCard from './components/JobCard';
import jobsData from './assets/jobs.json';
import type { Job } from './types';

function App() {
  // State to store jobs (simulating fetching from API)
  const [jobs, setJobs] = useState<Job[]>([]);

  useEffect(() => {
    // In a real app, you'd fetch this from an endpoint
    setJobs(jobsData);
  }, []);

  return (
    <div className="min-h-screen bg-slate-50">
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
          <button className="text-sm font-semibold text-primary border border-primary px-4 py-2 rounded hover:bg-indigo-50">
            Login
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        
        {/* Page Title & Stats */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-slate-800 mb-2">
            Recommended Jobs
          </h1>
          <p className="text-slate-600">
            Based on your profile, here are <span className="font-semibold text-slate-800">{jobs.length}</span> jobs you might be interested in.
          </p>
        </div>

        {/* Grid Layout for Job Cards */}
        <div className="grid gap-6">
          {jobs.map((job) => (
            <JobCard key={job.id} job={job} />
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;