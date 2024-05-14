import React from 'react';
import { Loader, MultiSelect, MultiSelectProps } from '@mantine/core';
import { useLazyGetTasksQuery } from '~/shared/api/services/tasks';

export type TaskSelectProps = MultiSelectProps;

export const TaskSelect: React.FC<TaskSelectProps> = ({ ...props }) => {
  //
  const [trigger, { data: tasks, isLoading }] = useLazyGetTasksQuery();

  const taskOptions = React.useMemo(() => {
    if (!tasks) return [];
    return tasks.map((task) => ({
      value: task.id.toString(),
      label: `${task.service} ${task.name}`,
    }));
  }, [tasks]);

  return (
    <MultiSelect
      leftSection={isLoading ? <Loader size='xs' /> : ''}
      data={taskOptions}
      onDropdownOpen={trigger}
      searchable
      {...props}
    />
  );
};
