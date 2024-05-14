import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api/baseQuery';
import { ConsigneeRequest, ConsigneeResponse } from './consignee.interface';

export const consigneeAPI = createApi({
  reducerPath: 'consigneeAPI',
  baseQuery: baseQuery({ baseURL: 'consignee/' }),
  tagTypes: ['consignees'],
  endpoints: (build) => ({
    getConsignees: build.query<ConsigneeResponse[], void>({
      query: () => ({
        url: ``,
        method: 'GET'
      }),
      providesTags: ['consignees']
    }),
    createConsignee: build.mutation<ConsigneeResponse, ConsigneeRequest>({
        query: (data) => ({
          url: '',
          method: 'POST',
          data
        })
      }),
    getConsigneeById: build.query<ConsigneeResponse, string>({
      query: (id) => ({
        url: id,
        method: 'GET'
      }),
      providesTags: ['consignees']
    }),
    updateConsignee: build.mutation<ConsigneeResponse, ConsigneeRequest>({
      query: (data) => ({
        url: data.id.toString(),
        method: 'PUT',
        data
      }),
      invalidatesTags: ['consignees']
    }),
    deleteConsignee: build.mutation<ConsigneeResponse, string>({
      query: (id) => ({
        url: id,
        method: 'DELETE'
      }),
      invalidatesTags: ['consignees']
    })
  })
});

export const {
  useGetConsigneesQuery,
  useLazyGetConsigneesQuery,
  useCreateConsigneeMutation,
  useGetConsigneeByIdQuery,
  useUpdateConsigneeMutation,
  useDeleteConsigneeMutation,
  endpoints
} = consigneeAPI;
