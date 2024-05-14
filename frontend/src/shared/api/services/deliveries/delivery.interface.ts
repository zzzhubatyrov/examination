export type DeliveryResponse = {
    id: number;
    name: {
        name: string;
    };
    who_pays: string;
    postal_code: number;
    region: string;
    city: string;
    address: string;
    middle_name: string;
    first_name: string;
    last_name: string;
    phone: string;
    email: string;
}

export type DeliveryRequest = {
    id: number;
    name: number;
    who_pays: string;
    postal_code: number;
    region: string;
    city: string;
    address: string;
    middle_name: string;
    first_name: string;
    last_name: string;
    phone: string;
    email: string;
}

