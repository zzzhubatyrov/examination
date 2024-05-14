import React from 'react';
import { RouterProvider } from 'react-router-dom';
import { Provider } from 'react-redux';

import { router } from '../routes';
import { store } from '../redux/store';

import '@mantine/core/styles.layer.css';
import '@mantine/dates/styles.css';
import 'mantine-datatable/styles.layer.css';

import { LoadingOverlay, MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  primaryColor: 'orange'
});

export default function App() {
  return (
    <React.Suspense fallback={<LoadingOverlay />}>
      <Provider store={store}>
        <MantineProvider theme={theme} defaultColorScheme='auto'>
          <RouterProvider router={router} />
        </MantineProvider>
      </Provider>
    </React.Suspense>
  );
}
