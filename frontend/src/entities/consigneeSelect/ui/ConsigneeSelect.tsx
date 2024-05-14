import React from 'react';
import { Loader, Select, SelectProps } from '@mantine/core';
import { useLazyGetConsigneesQuery } from '~/shared/api/services/consignees';

export type ConsigneeSelectProps = SelectProps;

export const ConsigneeSelect: React.FC<ConsigneeSelectProps> = ({ ...props }) => {

    const [trigger, { data: consignees, isLoading }] = useLazyGetConsigneesQuery();

    const consigneeOptions = React.useMemo(() => {
        if (consignees == undefined) return [];
        return consignees.map((consignee) => ({
            value: consignee.id.toString(),
            label: `${consignee.name}`
        }));
    }, [consignees]);

    return (
        <Select
            leftSection={isLoading ? <Loader size='xs' /> : ''}
            data={consigneeOptions}
            onDropdownOpen={trigger}
            searchable
            {...props}
        />
    );
};
