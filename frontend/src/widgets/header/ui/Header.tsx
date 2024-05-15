import { TextInput, UnstyledButton, ActionIcon, rem } from '@mantine/core';
import styles from './Header.module.css';
import React, { useState } from 'react'
import { ColorSchemeToggler } from '~/shared/ui/color-scheme-toggler';
import { IconSearch, IconArrowRight } from '@tabler/icons-react';
import {User, useUpdateMeMutation} from '~/shared/api/services/users';

type ProfileViewProps = {
  user? : User;
};

export const Header: React.FC<ProfileViewProps> = ({ user }) => {
    const [formData, setFormData] = useState<FormData>(new FormData());
    const [updateProfileImage] = useUpdateMeMutation();

    const refPhoto = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const reader = new FileReader();
            reader.onload = (e) => {
                if (e.target) {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-expect-error
                    formData.append('profile_image', event.target.files[0]);
                    setFormData(formData);
                    updateProfileImage(formData);
                }
            };

            reader.readAsDataURL(event.target.files[0]);
        }
    };

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
                {/*<img className={styles.user_image} src={user.profile_image} alt='Фотка пользователя' />*/}
                <label htmlFor='photoInput'>
                    <img className={styles.user_image} src={user.profile_image} alt='Фотка пользователя'/>
                </label>
                <input
                    id='photoInput'
                    type='file'
                    accept='image/*'
                    style={{display: 'none'}}
                    onChange={refPhoto}
                />
                <span>{user.first_name} {user.last_name}</span>
            </UnstyledButton>
        ) : (
            <span>Пользователь не вошел</span>
        )}
      </div>
    </div>
    );
};