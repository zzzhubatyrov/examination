import { KppResponse, useGetKppsQuery } from '~/shared/api/services/kpps';
import { DataTable, DataTableSortStatus } from 'mantine-datatable';

import styles from './KppTable.module.css';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ActionIcon, Group } from '@mantine/core';

export const KppTable: React.FC = () => {
  const [page, setPage] = useState(1);
  const [sortStatus, setSortStatus] = useState<DataTableSortStatus<KppResponse>>({
    columnAccessor: 'id',
    direction: 'asc'
  });
  const {
    data: kpps,
    isLoading,
    isFetching
  } = useGetKppsQuery();

  const navigate = useNavigate();

  const navigateToKpp = (id: number) => {
    navigate(`/editkpp?id=${id}`);
  }

  return (
    <div className={styles.table}>
      <DataTable
        className={styles.data_table}
        striped
        fetching={isFetching || isLoading}
        verticalSpacing='md'
        highlightOnHover
        records={kpps?.results}
        totalRecords={kpps?.count}
        page={page}
        onPageChange={setPage}
        recordsPerPage={25}
        paginationSize='md'
        columns={[
          { accessor: 'name_number', title: 'Номер', sortable: true },
          { accessor: 'name', title: 'Название', sortable: true },
          { accessor: 'description', title: 'description', sortable: true },
          { accessor: 'tin', title: 'ИНН', sortable: true },
          { accessor: 'kpp', title: 'КПП', sortable: true },
          { accessor: 'customer_contact_person', title: 'Представитель заказчика', sortable: true },
          { accessor: 'customer_phone', title: 'Телефон представителя', sortable: true },
          { accessor: 'customer_email', title: 'Почта представителя', sortable: true },
          { accessor: 'consignee_details.name', title: 'Заказчик', sortable: true },
          { accessor: 'delivery_method.who_pays', title: 'Способ доставки', sortable: true },
          { accessor: 'sold_by', title: 'Продано компанией', sortable: true },
          { accessor: 'priority', title: 'Приоритет', sortable: true },
          { accessor: 'difficulty', title: 'Сложность', sortable: true },
          {
            accessor: 'actions',
            render: (row) => (
              <Group gap={4} justify="right" wrap="nowrap">
                <ActionIcon
                  size="sm"
                  variant="subtle"
                  color="blue"
                  onClick={() => navigateToKpp(row.id)}
                >
                  fuck
                </ActionIcon>
              </Group>
            ),
          },
        ]}
        sortStatus={sortStatus}
        onSortStatusChange={setSortStatus}
      />
    </div>
  );
};