export type TaskResponse = {
  id: number;
  service: string;
  name: string;
  description: string;
  facility: {
    id: number;
    facility: string;
    address: string;
  };
  address: {
    id: number;
    facility: string;
    address: string;
  };
  applicant: {
    id: number;
    username: string;
  };
  tags: string;
  deadline: string;
  date_creation: string;
  date_end: string;
  difficulty: number;
  appointed: {
    id: number;
    username: string;
  };
  spectator: {
    id: number;
    username: string;
  };
  labor_intensity: number;
  document: {
    id: number;
  };
};

export type TaskRequest = {
  service: string;
  name: string;
  description: string;
  facility: number;
  address: number;
  applicant: number[];
  tags: string;
  deadline: string;
  date_end: string;
  appointed: number[];
  spectator: number[];
  labor_intensity: number;
  document: number[];
  status: number;
};

export type TasksResponse = {
  count: number;
  page_size: number;
  results: TaskResponse[];
};

export type Facility = {
  id: number;
  facility: string;
  address: string;
}