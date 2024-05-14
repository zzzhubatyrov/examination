import { BaseQueryFn } from '@reduxjs/toolkit/query';
import { AxiosError, AxiosRequestConfig } from 'axios';
import { api } from './api';

export const baseQuery =
  ({
    baseURL
  }: {
    baseURL: string;
  }): BaseQueryFn<
    {
      url: string;
      method?: AxiosRequestConfig['method'];
      data?: AxiosRequestConfig['data'];
      params?: AxiosRequestConfig['params'];
      headers?: AxiosRequestConfig['headers'];
    },
    unknown,
    unknown
  > =>
  async ({ url, method, data, params, headers = {} }) => {
    // Check if the data is FormData
    if (data instanceof FormData) {
      // If it is, let the browser set the Content-Type to multipart/form-data
      delete headers['Content-Type'];
      headers = { ...headers, 'Content-Type': 'multipart/form-data' };
    } else {
      // If it's not, set the Content-Type header to application/json
      headers = { ...headers, 'Content-Type': 'application/json' };
    }

    try {
      const result = await api({
        url: baseURL + url,
        method,
        data,
        params,
        headers // Pass the adjusted headers here
      });
      return { data: result.data };
    } catch (axiosError) {
      const err = axiosError as AxiosError;
      return {
        error: {
          status: err.response?.status,
          data: err.response?.data || err.message
        }
      };
    }
  };
