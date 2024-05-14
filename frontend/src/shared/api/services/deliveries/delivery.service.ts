import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api/baseQuery';
import { DeliveryRequest, DeliveryResponse } from './delivery.interface';

export const deliveriesAPI = createApi({
  reducerPath: 'deliveryAPI',
  baseQuery: baseQuery({ baseURL: 'delivery/' }),
  tagTypes: ['deliveries'],
  endpoints: (build) => ({
    getDeliveries: build.query<DeliveryResponse[], void>({
      query: () => ({
        url: ``,
        method: 'GET'
      }),
      providesTags: ['deliveries']
    }),
    createDelivery: build.mutation<DeliveryResponse, DeliveryRequest>({
        query: (data) => ({
          url: '',
          method: 'POST',
          data
        })
      }),
    getDeliveryById: build.query<DeliveryResponse, string>({
      query: (id) => ({
        url: id,
        method: 'GET'
      }),
      providesTags: ['deliveries']
    }),
    updateDelivery: build.mutation<DeliveryResponse, DeliveryRequest>({
      query: (data) => ({
        url: data.id.toString(),
        method: 'PUT',
        data
      }),
      invalidatesTags: ['deliveries']
    }),
    deleteDelivery: build.mutation<DeliveryResponse, string>({
      query: (id) => ({
        url: id,
        method: 'DELETE'
      }),
      invalidatesTags: ['deliveries']
    })
  })
});

export const {
  useGetDeliveriesQuery,
  useLazyGetDeliveriesQuery,
  useCreateDeliveryMutation,
  useGetDeliveryByIdQuery,
  useUpdateDeliveryMutation,
  useDeleteDeliveryMutation,

  endpoints
} = deliveriesAPI;
