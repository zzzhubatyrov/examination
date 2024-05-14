import { TextInput, UnstyledButton, ActionIcon, rem } from '@mantine/core';
import styles from './Header.module.css';
import { ColorSchemeToggler } from '~/shared/ui/color-scheme-toggler';
import { IconSearch, IconArrowRight } from '@tabler/icons-react';
import { User } from '~/shared/api/services/users';

type ProfileViewProps = {
  user? : User;
};

export const Header: React.FC<ProfileViewProps> = ({ user }) => {
  return (
    <div className={styles.header}>
      <div className={styles.section}>
        <TextInput
          radius='xl'
          // size='md'
          placeholder='Поиск..' 
          rightSectionWidth={42}
          leftSection={<IconSearch style={{ width: rem(18), height: rem(18) }} stroke={1.5} />}
          rightSection={
            <ActionIcon size={32} radius='xl' variant='filled'>
              <IconArrowRight style={{ width: rem(18), height: rem(18) }} stroke={1.5} />
            </ActionIcon>
          }
        />
      </div>
      <div className={styles.section}>
        <ColorSchemeToggler />
        {user ? (
          <UnstyledButton className={styles.user}>
            <img className={styles.user_image} src={user.profile_image} alt='Фотка пользователя' />
            <span>{user.first_name} {user.last_name}</span>
          </UnstyledButton>
        ) : (
          <span>Пользователь не вошел</span>
        )}
      </div>
    </div>
  );
};