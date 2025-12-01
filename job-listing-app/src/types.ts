export interface Job {
  id: string; // API returns string IDs
  title: string;
  description: string;
  logoUrl: string;
  orgName: string;
  location: string[]; // API returns an array of strings
  opType: string;
  categories: string[];
  members: number; // Using this for applicants count if available, or defaulting
  createdAt: string;
  updatedAt: string;
  status: string;
  deadline: string;
}

export interface ApiResponse {
  success: boolean;
  message: string;
  data: Job[];
  count: number;
}