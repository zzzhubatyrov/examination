import { TaskResponse, useGetMyTasksQuery } from '~/shared/api/services/tasks';
import { DataTable, DataTableSortStatus } from 'mantine-datatable';

import styles from './TasksTable.module.css';
import { TextInput } from '@mantine/core';
import { useState } from 'react';

export const TasksTable: React.FC = () => {
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState('');
  const [sortStatus, setSortStatus] = useState<DataTableSortStatus<TaskResponse>>({
    columnAccessor: 'id',
    direction: 'asc'
  });
  const {
    data: tasks,
    isLoading,
    isFetching
  } = useGetMyTasksQuery({
    page,
    search,
    sort: { accessor: sortStatus.columnAccessor, direction: sortStatus.direction }
  });
  console.log(tasks)

  return (
    <div className={styles.table}>
      <header className={styles.header}>
        <TextInput
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          placeholder='Поиск..'
        />
      </header>
      <DataTable
        className={styles.data_table}
        striped
        fetching={isFetching || isLoading}
        verticalSpacing='md'
        highlightOnHover
        records={tasks?.results}
        totalRecords={tasks?.count}
        page={page}
        onPageChange={setPage}
        recordsPerPage={25}
        paginationSize='md'
        columns={[
          { accessor: 'id', title: 'ID', sortable: true },
          { accessor: 'service', title: 'Сервис', sortable: true },
          { accessor: 'name', title: 'Название', sortable: true },
          { accessor: 'description', title: 'Описание', sortable: true },
          { accessor: 'priority', title: 'Приоритет', sortable: true },
          { accessor: 'tags', title: 'Теги', sortable: true },
          { accessor: 'difficulty', title: 'Сложность', sortable: true }
        ]}
        sortStatus={sortStatus}
        onSortStatusChange={setSortStatus}
      />
    </div>
  );
};
