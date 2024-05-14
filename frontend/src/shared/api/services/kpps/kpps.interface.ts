export type KppResponse = {
    id: number;
    name_number: string;
    name: string;
    description: string;
    tin: string;
    kpp: string;
    customer_contact_person: string;
    customer_phone: string;
    customer_email: string;
    consignee_details: {
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
    };
    delivery_method: {
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
    };
    contract: string;
    bill: string;
    price: string;
    payment_terms: string;
    payment_order: string;
    manager: {
        id: number;
        username: string;
        first_name: string;
        middle_name: string;
        last_name: string;
    };
    sold_by: string;
    priority: number;
    difficulty: number;
    date_started: string;
    date_end: string;
    status: {
        status: string;
    };
    document: {
        document: number;
    };
    task: {
        id: number;
        service: string;
        name: string;
        description: string;
        facility: {
            id: number;
            facility: string;
            address: string;
        };
        address: {
            id: number;
            facility: string;
            address: string;
        };
        applicant: {
            id: number;
            username: string;
        };
        tags: string;
        deadline: string;
        date_creation: string;
        date_end: string;
        difficulty: number;
        appointed: {
            id: number;
            username: string;
        };
        spectator: {
            id: number;
            username: string;
        };
        labor_intensity: number;
        document: {
            id: number;
        };
    };
    equipment: {
        id: number;
        name: string;
        specifications: string;
        delivery_set: string;
        documentation_set: string;
        documentation_set_before_bs: string;
        examination: string;
        samples: string;
        consignment_note: string;
        pnr: true;
        installation_supervision: string;
        guarantee: string;
        year_of_manufacture: string;
        factory_number: string;
        shipment_time: string;
    };
}

export type KppRequest = {
    name_number: string;
    name: string;
    description: string;
    tin: string;
    kpp: string;
    customer_contact_person: string;
    customer_phone: string;
    customer_email: string;
    consignee_details: number;
    delivery_method: number;
    contract: string;
    bill: string;
    price: string;
    payment_terms: string;
    payment_order: string;
    manager: number[];
    sold_by: string;
    priority: number;
    difficulty: number;
    date_end: string;
    status: number;
    document: FileList[];
    task: number[];
    equipment: number[];
}



export type KppsResponse = {
    count: number;
    page_size: number;
    results: KppResponse[];
};