export interface Job {
  id: number;
  company: string;
  logo: string;
  title: string;
  location: string;
  type: string;
  description: string;
  tags: string[];
  applicants: number;
}