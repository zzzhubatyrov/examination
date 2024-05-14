import React from 'react';
import { Loader, MultiSelect, MultiSelectProps } from '@mantine/core';
import { useLazyGetEquipmentsQuery } from '~/shared/api/services/equipments';

export type EquipmentSelectProps = MultiSelectProps;

export const EquipmentSelect: React.FC<EquipmentSelectProps> = ({ ...props }) => {
  //
  const [trigger, { data: equipments, isLoading }] = useLazyGetEquipmentsQuery();

  const equipmentOptions = React.useMemo(() => {
    if (!equipments) return [];
    return equipments.map((equipment) => ({
      value: equipment.id.toString(),
      label: `${equipment.name} ${equipment.factory_number}`,
    }));
  }, [equipments]);

  return (
    <MultiSelect
      leftSection={isLoading ? <Loader size='xs' /> : ''}
      data={equipmentOptions}
      onDropdownOpen={trigger}
      searchable
      {...props}
    />
  );
};
