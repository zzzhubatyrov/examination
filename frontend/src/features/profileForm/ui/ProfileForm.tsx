import {Button, Card, Loader, TextInput, FileInput} from '@mantine/core';
import {useGetMeQuery, useUpdateMeMutation} from '~/shared/api/services/users';
import React, { useState } from 'react';

import styles from './ProfileForm.module.css';

export const ProfileForm = () => {
  const [updateMe] = useUpdateMeMutation();
  const { data: me, isLoading } = useGetMeQuery();
  const [formData, setFormData] = useState(new FormData());

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    formData.append(e.target.name, e.target.value);
    setFormData(formData);
  };

  const handleFileInput = (e: File | null) => {
    formData.append('profile_image', e as File);
    setFormData(formData);
  }

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    updateMe(formData);
  };

  if (isLoading || !me) return <Loader type='bars' />;

  return (
    <Card className={styles.profile_form}>
      <form
        onSubmit={handleSubmit}
      >
        <div className={styles.inputs}>
          <div>
            <img
              className={styles.profile_image}
              src={me?.profile_image}
              alt="Фото пользователя"
              onClick={() => handleFileInput(null)}
              style={{cursor: "pointer"}}
            />
            <FileInput
              accept="image/*"
              name="profile_image"
              onChange={handleFileInput}
              label="Выберите изображение"
            ></FileInput>
            <div>
            </div>
          </div>
          <div className={styles.inputs_block}>
            <TextInput
              label='Фамилия'
              placeholder='Ваша фамилия'
              name='middle_name'
              value={me.middle_name}
              onChange={handleInputChange}
            />
            <TextInput
              label='Имя'
              placeholder='Ваше имя'
              mt='md'
              name='first_name'
              value={me.first_name}
              onChange={handleInputChange}
            />
            <TextInput
              label='Отчество'
              placeholder='Ваше отчество'
              mt='md'
              name='last_name'
              value={me.last_name}
              onChange={handleInputChange}
            />
            <TextInput
              label='Логин'
              placeholder='Ваш логин'
              mt='md'
              name='username'
              value={me.username}
              onChange={handleInputChange}
            />
          </div>
          <div className={styles.inputs_block}>
          <TextInput
              label='Email'
              placeholder='Введите ваш email'
              name='email'
              value={me.email}
              onChange={handleInputChange}
            />
            <TextInput
              label='Мобильный телефон'
              placeholder='Ваш мобильный телефон'
              mt='md'
              name='mobile_phone'
              value={me.mobile_phone}
              onChange={handleInputChange}
            />
            <TextInput
              label='Офисный телефон'
              placeholder='Ваш офисный телефон'
              mt='md'
              name='office_phone'
              value={me.office_phone}
              onChange={handleInputChange}
            />
            <TextInput
              label='Телеграм'
              placeholder='Ваш телеграм'
              mt='md'
              name='telegram'
              value={me.telegram}
              onChange={handleInputChange}
            />
          </div>
        </div>
        <Button fullWidth mt='xl' type='submit'> 
          Сохранить
        </Button>
      </form>
    </Card>
  );
};
