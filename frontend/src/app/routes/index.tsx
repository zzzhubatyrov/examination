import { Outlet, createBrowserRouter } from 'react-router-dom';
import { AppLayout } from '~/shared/ui/layouts';
import { Login } from '~/pages/login';
import { Profile } from '~/pages/profile';
import { Tasks } from '~/pages/tasks';
import { TaskForm } from '~/features/taskForm';
import { MyProfile } from '~/pages/myProfile';
import { ProfileForm } from '~/features/profileForm';
import { Header } from '~/widgets/header/ui/Header';
import { useGetMeQuery } from '~/shared/api/services/users';
import { Kpps } from '~/pages/kpps';
import { CreateKpp } from "~/pages/createKpp";
import { EditKpp } from '~/pages/editKpp';

const Router = () => {
  const { data: user, error, isLoading } = useGetMeQuery();
  
  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.toString()}</p>;
  }

  return (
    <AppLayout title='test'>
      <>
        <Header user={user} />
        <Outlet />
      </>
    </AppLayout>
  );
};

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Router />,
    children: [
      {
        path: '/kpps',
        element: <Kpps />
      },
      {
        path: '/tasks',
        element: <Tasks />
      },
      {
        path: '/profile/:userId',
        element: <Profile />
      },
      {
        path: 'createtask',
        element: <TaskForm />
      },
      {
        path: 'createkpp',
        element: <CreateKpp />
      },
      {
        path: 'profile',
        element: <MyProfile />
      },
      {
        path: 'profileform',
        element: <ProfileForm />
      },
      {
        path: `editkpp?id=`,
        element: <EditKpp />
      }
    ]
  },
  {
    path: '/login',
    element: <Login />
  }
]);
