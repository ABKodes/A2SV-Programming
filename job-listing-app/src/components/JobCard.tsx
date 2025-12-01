import React from 'react';
import type { Job } from '../types';

interface JobCardProps {
  job: Job;
}

const JobCard: React.FC<JobCardProps> = ({ job }) => {
  // Helper to handle missing images gracefully
  const logo = job.logoUrl || 'https://via.placeholder.com/150?text=No+Logo';

  return (
    <div className="group flex items-start gap-4 p-6 bg-white border border-gray-200 rounded-xl hover:border-primary hover:shadow-lg transition-all duration-200 cursor-pointer">
      
      {/* Avatar / Logo Section */}
      <div className="flex-shrink-0">
        <img 
          src={logo} 
          alt={`${job.orgName} logo`} 
          className="w-16 h-16 rounded-lg object-cover border border-gray-100"
          onError={(e) => {
            (e.target as HTMLImageElement).src = 'https://via.placeholder.com/150?text=No+Logo';
          }}
        />
      </div>

      {/* Main Content Section */}
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
          {/* Bookmark Icon */}
          <button className="text-gray-400 hover:text-primary">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
            </svg>
          </button>
        </div>

        <p className="text-sm text-slate-600 mb-4 leading-relaxed line-clamp-2">
          {job.description}
        </p>

        {/* Tags & Actions Footer */}
        <div className="flex justify-between items-center mt-auto">
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1 text-xs font-semibold text-blue-600 bg-blue-50 rounded-full border border-blue-100">
              {job.opType}
            </span>
            <div className="h-4 w-px bg-gray-300 mx-1 self-center hidden sm:block"></div>
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