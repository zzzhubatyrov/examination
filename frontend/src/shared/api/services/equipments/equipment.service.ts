import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api/baseQuery';
import { EquipmentRequest, EquipmentResponse } from './equipment.interface';

export const equipmentsAPI = createApi({
  reducerPath: 'equipmentAPI',
  baseQuery: baseQuery({ baseURL: 'equipment/' }),
  tagTypes: ['equipments'],
  endpoints: (build) => ({
    getEquipments: build.query<EquipmentResponse[], void>({
      query: () => ({
        url: ``,
        method: 'GET'
      }),
      providesTags: ['equipments']
    }),
    createEquipment: build.mutation<EquipmentResponse, EquipmentRequest>({
      query: (data) => ({
        url: '',
        method: 'POST',
        data
      })
    }),
    getEquipmentById: build.query<EquipmentResponse, string>({
      query: (id) => ({
        url: id,
        method: 'GET'
      }),
      providesTags: ['equipments']
    }),
    updateEquipment: build.mutation<EquipmentResponse, EquipmentRequest>({
      query: (data) => ({
        url: data.id.toString(),
        method: 'PUT',
        data
      }),
      invalidatesTags: ['equipments']
    }),
    deleteEquipment: build.mutation<EquipmentResponse, string>({
      query: (id) => ({
        url: id,
        method: 'DELETE'
      }),
      invalidatesTags: ['equipments']
    })
  })
});

export const {
  useGetEquipmentsQuery,
  useLazyGetEquipmentsQuery,
  useCreateEquipmentMutation,
  useGetEquipmentByIdQuery,
  useUpdateEquipmentMutation,
  useDeleteEquipmentMutation,

  endpoints
} = equipmentsAPI;
