import React from 'react';
import { AppShell } from '@mantine/core';
import { Navbar } from './Navbar';

type AppLayoutProps = {
  title: string;
  children: JSX.Element;
};

export const AppLayout: React.FC<AppLayoutProps> = ({ children }) => {
  return (
    <AppShell layout='alt' navbar={{ width: 200, breakpoint: 0 }}>
      <AppShell.Navbar p='md'>
        <Navbar />
      </AppShell.Navbar>
      <AppShell.Main>{children}</AppShell.Main>
    </AppShell>
  );
};
