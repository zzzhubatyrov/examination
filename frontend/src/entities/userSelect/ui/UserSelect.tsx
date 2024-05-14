import React from 'react';
import { Loader, MultiSelect, MultiSelectProps } from '@mantine/core';
import { useLazyGetUsersQuery } from '~/shared/api/services/users';

export type UserSelectProps = MultiSelectProps;

export const UserSelect: React.FC<UserSelectProps> = ({ ...props }) => {
  //
  const [trigger, { data: users, isLoading }] = useLazyGetUsersQuery();

  const userOptions = React.useMemo(() => {
    if (!users) return [];
    return users.map((user) => ({
      value: user.id.toString(),
      label: `${user.middle_name} ${user.first_name} ${user.last_name}`,
    }));
  }, [users]);

  return (
    <MultiSelect
      leftSection={isLoading ? <Loader size='xs' /> : ''}
      data={userOptions}
      onDropdownOpen={trigger}
      searchable
      {...props}
    />
  );
};
