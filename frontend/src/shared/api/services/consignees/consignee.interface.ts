export type ConsigneeResponse = {
    id: number;
    name: string;
    tin: string;
    kpp: string;
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

export type ConsigneeRequest = {
    id: number;
    name: string;
    tin: string;
    kpp: string;
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

// export type ConsigneesResponse = {
//     count: number;
//     page_size: number;
//     results: ConsigneeResponse[];
// };