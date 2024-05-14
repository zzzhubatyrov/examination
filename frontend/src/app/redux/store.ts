import { configureStore } from '@reduxjs/toolkit';

import { tasksAPI } from '~/shared/api/services/tasks';
import { userAPI } from '~/shared/api/services/users';
import { kppsAPI } from '~/shared/api/services/kpps';
import { consigneeAPI } from '~/shared/api/services/consignees';
import { deliveriesAPI } from '~/shared/api/services/deliveries';
import { equipmentsAPI } from '~/shared/api/services/equipments';

export const store = configureStore({
  reducer: {
    [tasksAPI.reducerPath]: tasksAPI.reducer,
    [userAPI.reducerPath]: userAPI.reducer,
    [kppsAPI.reducerPath]: kppsAPI.reducer,
    [consigneeAPI.reducerPath]: consigneeAPI.reducer,
    [deliveriesAPI.reducerPath]: deliveriesAPI.reducer,
    [equipmentsAPI.reducerPath]: equipmentsAPI.reducer
  },

  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(tasksAPI.middleware).concat(userAPI.middleware).concat(kppsAPI.middleware).concat(consigneeAPI.middleware).concat(deliveriesAPI.middleware).concat(equipmentsAPI.middleware)
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
