import React from 'react';
import type { Job } from '../types';

interface JobCardProps {
  job: Job;
  isBookmarked: boolean;
  onToggleBookmark: (id: string) => void;
}

const JobCard: React.FC<JobCardProps> = ({ job, isBookmarked, onToggleBookmark }) => {
  const logo = job.logoUrl || 'https://via.placeholder.com/150?text=No+Logo';

  return (
    <div data-testid={`job-card-${job.id}`} className="group flex items-start gap-4 p-6 bg-white border border-gray-200 rounded-xl hover:border-primary hover:shadow-lg transition-all duration-200 cursor-pointer relative">
      
      <div className="flex-shrink-0">
        <img 
          src={logo} 
          alt={`${job.orgName} logo`} 
          className="w-16 h-16 rounded-lg object-cover border border-gray-100"
          onError={(e) => { (e.target as HTMLImageElement).src = 'https://via.placeholder.com/150?text=No+Logo'; }}
        />
      </div>

      <div className="flex-grow">
        <div className="flex justify-between items-start mb-2">
          <div>
            <h3 className="text-lg font-bold text-slate-800 group-hover:text-primary transition-colors">
              {job.title}
            </h3>
            <p className="text-sm text-slate-600 font-medium">
              {job.orgName} • <span className="text-slate-400">{job.location.join(', ')}</span>
            </p>
          </div>
          
          {/* Bookmark Toggle Button */}
          <button 
            data-testid="bookmark-btn"
            onClick={(e) => {
              e.stopPropagation(); // Prevent card click event
              onToggleBookmark(job.id);
            }}
            className={`p-2 rounded-full transition-colors ${
              isBookmarked ? 'text-primary bg-indigo-50' : 'text-gray-400 hover:text-primary hover:bg-gray-50'
            }`}
          >
            {isBookmarked ? (
              // Filled Icon
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
                <path fillRule="evenodd" d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z" clipRule="evenodd" />
              </svg>
            ) : (
              // Outline Icon
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
              </svg>
            )}
          </button>
        </div>

        <p className="text-sm text-slate-600 mb-4 leading-relaxed line-clamp-2">
          {job.description}
        </p>

        <div className="flex justify-between items-center mt-auto">
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1 text-xs font-semibold text-blue-600 bg-blue-50 rounded-full border border-blue-100">
              {job.opType}
            </span>
            {job.categories.map((tag, index) => (
              <span key={index} className="px-3 py-1 text-xs font-medium text-yellow-600 bg-yellow-50 rounded-full border border-yellow-100">
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobCard;