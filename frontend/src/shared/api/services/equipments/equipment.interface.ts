export type EquipmentResponse = {
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
}

export type EquipmentRequest = {
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