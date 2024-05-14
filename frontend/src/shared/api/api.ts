import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost/api/',
  headers: { 'Content-Type': 'application/json' },
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  withCredentials: true
});
