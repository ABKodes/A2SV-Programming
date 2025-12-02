import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import JobCard from '../components/JobCard';
import type { Job, ApiResponse } from '../types';
import { useAuth } from '../context/AuthContext';

// Notice: 'export const' here (Named Export), NOT 'export default'
export const Home = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const { isAuthenticated, logout, user } = useAuth();

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const response = await fetch('https://akil-backend.onrender.com/opportunities/search');
        const result: ApiResponse = await response.json();
        if (result.success && Array.isArray(result.data)) {
          setJobs(result.data);
        }
      } catch (err) {
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchJobs();
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 font-sans">
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
             <div className="w-8 h-8 bg-primary rounded-full flex items-center justify-center text-white font-bold">J</div>
             <span className="text-xl font-bold text-slate-800">JobFinder</span>
          </div>
          
          <div className="flex gap-3 items-center">
            {isAuthenticated ? (
              <>
                <span className="text-sm text-slate-600 hidden sm:block">Hi, {user?.name || 'User'}</span>
                <button onClick={logout} className="text-sm font-bold text-red-500 border border-red-200 px-4 py-2 rounded hover:bg-red-50">
                  Logout
                </button>
              </>
            ) : (
              <>
                 <Link to="/login" className="text-sm font-bold text-primary px-4 py-2 rounded hover:bg-indigo-50">
                  Login
                </Link>
                <Link to="/signup" className="text-sm font-bold text-white bg-primary px-4 py-2 rounded hover:bg-indigo-700">
                  Sign Up
                </Link>
              </>
            )}
          </div>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-10">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-slate-800 mb-2">Opportunities</h1>
          <p className="text-slate-600">Showing {jobs.length} results</p>
        </div>

        {isLoading ? (
           <p className="text-center py-10">Loading jobs...</p> 
        ) : (
           <div className="flex flex-col gap-6">
            {jobs.map(job => <JobCard key={job.id} job={job} />)}
           </div>
        )}
      </main>
    </div>
  );
};