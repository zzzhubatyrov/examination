import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api/baseQuery';
import { KppResponse, KppsResponse } from './kpps.interface.ts';

export const kppsAPI = createApi({
  reducerPath: 'kppAPI',
  baseQuery: baseQuery({ baseURL: 'kpp/' }),
  tagTypes: ['kpps'],
  endpoints: (build) => ({
    getKpps: build.query<
      KppsResponse,
      void
      >({
      query: () => ({
        url: '',
        method: 'GET'
      }),
      providesTags: ['kpps'],
      keepUnusedDataFor: 30
    }),
    getkppById: build.query<KppResponse, number>({
      query: (id) => ({
        url: `${id}`,
        method: 'GET'
      }),
      providesTags: ['kpps']
    }),
    updatekpp: build.mutation<KppResponse, { id: number; data: FormData }>({
      query: ({ id, data }) => ({
        url: `${id}`,
        method: 'PUT',
        data,
      }),
      invalidatesTags: ['kpps']
    }),
    createkpp: build.mutation<void, FormData>({
      query: (data) => ({
        url: '',
        method: 'POST',
        data
      }),
      invalidatesTags: ['kpps']
    }),
    deletekpp: build.mutation<KppResponse, number>({
      query: (id) => ({
        url: `${id}`,
        method: 'DELETE'
      }),
      invalidatesTags: ['kpps']
    })
  })
});

export const {
  useGetKppsQuery,
  useCreatekppMutation,
  useGetkppByIdQuery,
  useUpdatekppMutation,
  useDeletekppMutation,
  useLazyGetKppsQuery,
  useLazyGetkppByIdQuery,
  endpoints
} = kppsAPI;
