import React from 'react';
import { Loader, Select, SelectProps } from '@mantine/core';
import { useLazyGetFacilitiesQuery } from '~/shared/api/services/tasks';

export type FacilitySelectProps = SelectProps;

export const FacilitiesSelect: React.FC<FacilitySelectProps> = ({ ...props }) => {

  const [trigger, { data: facilities, isLoading }] = useLazyGetFacilitiesQuery();

  const facilityOptions = React.useMemo(() => {
    if (facilities == undefined) return [];
    return facilities.map((facility) => ({
      value: facility.id.toString(),
      label: `${facility.facility}`
    }));
  }, [facilities]);

  return (
    <Select
      leftSection={isLoading ? <Loader size='xs' /> : ''}
      data={facilityOptions}
      onDropdownOpen={trigger}
      searchable
      {...props}
    />
  );
};
