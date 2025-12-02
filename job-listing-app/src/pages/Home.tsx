import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import JobCard from '../components/JobCard';
import type { Job, ApiResponse } from '../types';
import { useAuth } from '../context/AuthContext';

export const Home = () => {
  const [jobs, setJobs] = useState<Job[]>([]);
  const [bookmarkedIds, setBookmarkedIds] = useState<Set<string>>(new Set());
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const { isAuthenticated, logout, user, token } = useAuth();
  const navigate = useNavigate();

  // 1. Fetch Jobs
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

  // 2. Fetch Bookmarks (Only if logged in)
  useEffect(() => {
    if (isAuthenticated && token) {
      const fetchBookmarks = async () => {
        try {
          const response = await fetch('https://akil-backend.onrender.com/bookmarks', {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          const result = await response.json();
          if (result.success && Array.isArray(result.data)) {
            // Extract IDs from bookmark objects
            const ids = new Set(result.data.map((b: any) => b.eventID));
            setBookmarkedIds(ids);
          }
        } catch (err) {
          console.error("Failed to load bookmarks", err);
        }
      };
      fetchBookmarks();
    } else {
      setBookmarkedIds(new Set());
    }
  }, [isAuthenticated, token]);

  // 3. Toggle Logic
  const handleToggleBookmark = async (jobId: string) => {
    if (!isAuthenticated || !token) {
      alert("Please login to bookmark jobs.");
      navigate('/login');
      return;
    }

    const isBookmarked = bookmarkedIds.has(jobId);
    const url = `https://akil-backend.onrender.com/bookmarks/${jobId}`;
    const method = isBookmarked ? 'DELETE' : 'POST';

    // Optimistic UI Update
    setBookmarkedIds(prev => {
      const newSet = new Set(prev);
      if (isBookmarked) newSet.delete(jobId);
      else newSet.add(jobId);
      return newSet;
    });

    try {
      const response = await fetch(url, {
        method,
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });
      
      if (!response.ok) throw new Error('Failed to update bookmark');
      
    } catch (err) {
      console.error(err);
      // Revert on failure
      setBookmarkedIds(prev => {
        const newSet = new Set(prev);
        if (isBookmarked) newSet.add(jobId);
        else newSet.delete(jobId);
        return newSet;
      });
      alert("Failed to update bookmark. Please try again.");
    }
  };

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
                <span className="text-sm text-slate-600 hidden sm:block">Hi, {user?.name}</span>
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
            {jobs.map(job => (
              <JobCard 
                key={job.id} 
                job={job} 
                isBookmarked={bookmarkedIds.has(job.id)}
                onToggleBookmark={handleToggleBookmark}
              />
            ))}
           </div>
        )}
      </main>
    </div>
  );
};