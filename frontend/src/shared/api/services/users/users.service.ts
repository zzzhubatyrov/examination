import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api';
import { User } from './users.interface';

export const userAPI = createApi({
  reducerPath: 'userAPI',
  baseQuery: baseQuery({ baseURL: 'user/' }),
  tagTypes: ['me', 'users'],
  endpoints: (build) => ({
    getMe: build.query<User, void>({
      query: () => ({
        url: 'me',
        method: 'GET'
      }),
      providesTags: ['me']
    }),
    updateMe: build.mutation<User, FormData>({
      query: (data) => ({
        url: 'me',
        method: 'PUT',
        data
      }),
      invalidatesTags: ['me']
    }),
    getUserById: build.query<User, number>({
      query: (id) => ({
        url: `${id}/`,
        method: 'GET'
      }),
      providesTags: ['users']
    }),
    getUsers: build.query<User[], void>({
      query: () => ({
        url: 'users',
        method: 'GET'
      })
    })
  })
});

export const {
  useGetMeQuery,
  useLazyGetMeQuery,
  useUpdateMeMutation,
  useLazyGetUsersQuery,
  useGetUsersQuery,
  endpoints
} = userAPI;
