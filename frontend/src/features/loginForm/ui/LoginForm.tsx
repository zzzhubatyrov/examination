import { Button, PasswordInput, TextInput } from '@mantine/core';
import { zodResolver } from 'mantine-form-zod-resolver';
import { useForm } from '@mantine/form';
import { z } from 'zod';
import { api } from '~/shared/api';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
export const LoginForm = () => {
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const loginSchema = z.object({
    username: z
      .string(),
      // .min(3, { message: 'Логин должен быть длиннее 3 символов.' })
      // .max(20, { message: 'Логин должен быть короче 20 символов.' }),
    password: z
      .string()
      // .min(3, { message: 'Пароль должен быть длиннее 3 символов.' })
      // .max(20, { message: 'Пароль должен быть короче 20 символов.' })
  });

  type loginSchema = z.infer<typeof loginSchema>;

  const form = useForm<loginSchema>({
    validate: zodResolver(loginSchema)
  });

  const onSubmit = (values: loginSchema) => {
      api.post('/user/login/', values)
      .then((res) => {
        if (res.status === 200) {
          navigate('/');
        } else if (res.status === 401) {
          setErrorMessage('Неверные данные');
        }
      })
      .catch((error) => {
        console.error('Ошибка при отправке запроса:', error);
        setErrorMessage('Произошла ошибка при отправке запроса');
      });
  };

  return (
    <form onSubmit={form.onSubmit((values) => onSubmit(values))}>
      <TextInput
        label='Логин'
        placeholder='Ваш логин'
        size='md'
        {...form.getInputProps('username')}
      />
      <PasswordInput
        label='Пароль'
        placeholder='Ваш пароль'
        mt='md'
        size='md'
        {...form.getInputProps('password')}
      />
        {errorMessage && <div style={{ color: 'red', marginTop: '8px' }}>{errorMessage}</div>} {/* Отображение сообщения об ошибке */}
      <Button fullWidth mt='xl' size='md' type='submit'>
        Войти
      </Button>
    </form>
  );
};
