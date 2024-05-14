import { ProfileView } from '~/features/profileView/ui';
import { useGetMeQuery } from '~/shared/api/services/users';

export const MyProfile = () => {
  const { data, isLoading } = useGetMeQuery();

  if (isLoading || !data) return 'loading...';

  return (
    <div>
      <ProfileView user={data} />
    </div>
  );
};
