import React from 'react';
import { User } from '~/shared/api/services/users';

import styles from './ProfileView.module.css';
import { Card } from '@mantine/core';

type ProfileViewProps = {
  user: User;
};

export const ProfileView: React.FC<ProfileViewProps> = ({ user }) => {
  return (
    <Card className={styles.user}>
      <img className={styles.user_image} src={user.profile_image} alt='Фотка пользователя' />
      <div>id: {user.id}</div>
      <div>
        {user.middle_name} {user.first_name} {user.last_name}
      </div>
      <div>
        email: {user.email} | tel: {user.telegram}
      </div>
    </Card>
  );
};
