import { Paper, Title } from '@mantine/core';

import cl from './Login.module.css';
import { LoginForm } from '~/features/loginForm';

export const Login = () => {
  return (
    <div className={cl.wrapper}>
      <Paper className={cl.form} radius={0} p={30}>
        <Title order={2} className={cl.title} ta='center' mt='md' mb={50}>
          Добро пожаловать!
        </Title>
        <LoginForm />
      </Paper>
    </div>
  );
};
