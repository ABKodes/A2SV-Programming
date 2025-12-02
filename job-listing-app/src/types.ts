export interface Job {
  id: string;
  title: string;
  description: string;
  logoUrl: string;
  orgName: string;
  location: string[];
  opType: string;
  categories: string[];
  members: number;
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