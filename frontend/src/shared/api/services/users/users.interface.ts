export type User = {
  id: number;
  first_name: string;
  middle_name: string;
  last_name: string;
  username: string;
  email: string;
  mobile_phone: string;
  office_phone: number;
  telegram: string;
  department: number;
  post: number;
  profile_image: string;
  is_superuser: true;
  is_staff: true;
};

export type PartialUser = Partial<User> & { id: number };
