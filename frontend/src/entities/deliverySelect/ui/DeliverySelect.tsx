import React from 'react';
import { Loader, Select, SelectProps } from '@mantine/core';
import { useLazyGetDeliveriesQuery } from '~/shared/api/services/deliveries';

export type DeliverySelectProps = SelectProps;

export const DeliverySelect: React.FC<DeliverySelectProps> = ({ ...props }) => {

    const [trigger, { data: deliveries, isLoading }] = useLazyGetDeliveriesQuery();

    const deliveryOptions = React.useMemo(() => {
        if (deliveries == undefined) return [];
        return deliveries.map((delivery) => ({
            value: delivery.id.toString(),
            label: `${delivery.who_pays}`
        }));
    }, [deliveries]);

    return (
        <Select
            leftSection={isLoading ? <Loader size='xs' /> : ''}
            data={deliveryOptions}
            onDropdownOpen={trigger}
            searchable
            {...props}
        />
    );
};
