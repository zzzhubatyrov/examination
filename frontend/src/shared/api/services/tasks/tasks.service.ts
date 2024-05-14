import { createApi } from '@reduxjs/toolkit/query/react';
import { baseQuery } from '~/shared/api/baseQuery';
import { TaskResponse, TasksResponse, Facility } from './tasks.interface';

export const tasksAPI = createApi({
  reducerPath: 'taskAPI',
  baseQuery: baseQuery({ baseURL: 'taskpage/' }),
  tagTypes: ['tasks'],
  endpoints: (build) => ({
    getTasks: build.query<TaskResponse[], void>({
      query: () => ({
        url: ``,
        method: 'GET'
      }),
      providesTags: ['tasks']
    }),
    getTaskById: build.query<TaskResponse, string>({
      query: (id) => ({
        url: id,
        method: 'GET'
      }),
      providesTags: ['tasks']
    }),
    createTask: build.mutation<void, FormData>({
      query: (data) => ({
        url: '',
        method: 'POST',
        data
      }),
      invalidatesTags: ['tasks']
    }),
    deleteTask: build.mutation<TaskResponse, number>({
      query: (id) => ({
        url: `${id}`,
        method: 'DELETE'
      }),
      invalidatesTags: ['tasks']
    }),
    getMyTasks: build.query<
      TasksResponse,
      { page: number; search?: string; sort: { accessor: string; direction: string } }
    >({
      query: ({ page, search, sort }) => ({
        url: 'me',
        method: 'GET',
        params: {
          page,
          service: search,
          task_list: `${sort.direction === 'asc' ? '' : '-'}${sort.accessor}`
        }
      }),
      providesTags: ['tasks'],
      keepUnusedDataFor: 30
    }),
    getFacilities: build.query<Facility[], void>({
      query: () => ({
        url: `facilities/`,
        method: 'GET'
      }),
    }),
  })
});

export const {
  useGetTasksQuery,
  useLazyGetTasksQuery,
  useCreateTaskMutation,
  useDeleteTaskMutation,
  useGetTaskByIdQuery,
  useGetMyTasksQuery,
  useGetFacilitiesQuery,
  useLazyGetFacilitiesQuery,
  endpoints
} = tasksAPI;
