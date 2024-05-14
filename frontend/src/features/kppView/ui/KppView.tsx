import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { Button, Card, ComboboxItem, FileInput, TextInput } from '@mantine/core';
import { DateInput, DateValue } from '@mantine/dates';
import { useUpdatekppMutation, useGetkppByIdQuery } from '~/shared/api/services/kpps';
import { UserSelect } from '~/entities/userSelect';
import { ConsigneeSelect } from '~/entities/consigneeSelect';
import { DeliverySelect } from '~/entities/deliverySelect';
import { EquipmentSelect } from '~/entities/equipmentSelect';
import { TaskSelect } from '~/entities/taskSelect';
import styles from './KppView.module.css';

export const KppView: React.FC = () => {
  //

  const params = useParams();
  const id = Number(params.id);
  console.log(id);
  const [formData, setFormData] = useState(new FormData());

  const [updateKpp] = useUpdatekppMutation();

  const { data: kpp } = useGetkppByIdQuery(id);


  const handleSelectInputChange = (name: string, value: string | null, option?: ComboboxItem) => {
    if (option) {
      formData.append(name, option.value);
    } else {
      formData.append(name, value as string);
    }
    setFormData(formData);
  };

  const handleMultiSelectInputChange = (name: string, value: string[] | null, option?: ComboboxItem) => {
    if (option) {
      formData.append(name, option.value);
    } else {
      value?.forEach((manager) => {
        formData.append(name, manager);
      });
    }
    setFormData(formData);
  };

  const handleDateInput = (e: DateValue) => {
    const date = e?.getDate?.();
    if (date) {
      formData.append('date', date.toString());
    }
    setFormData(formData);
  }

  const handleFileInput = (files: File[]) => {
    files.forEach((file) => {
      formData.append('document', file);
    });
    setFormData(formData);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    formData.append(e.target.name, e.target.value);
    setFormData(formData);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    updateKpp({ id: id, data: formData });
  };

  return (
    <Card className={styles.kpp_form}>
      <form
        className={styles.CreateKpp}
        onSubmit={handleSubmit}
      >
        <div className={styles.inputs}>
          <div className={styles.inputs_block}>
            <TextInput value={kpp?.name_number} label='Номер' name='name_number' onChange={handleInputChange} />
            <TextInput value={kpp?.name} label='Наименование' name='name' onChange={handleInputChange} />
            <TextInput value={kpp?.description} label='Описание' name='description' onChange={handleInputChange} />
            <ConsigneeSelect label='Компания заказчика' name='consignee_details' onChange={(value, option) => handleSelectInputChange('consignee_details', value, option)} />
            <div className={styles.inputs}>
              <div className={styles.inputs_block}>
                <TextInput value={kpp?.tin} label='ИНН/КПП' name='tin' onChange={handleInputChange} />
              </div>
              <div className={styles.inputs_block}>
                <TextInput value={kpp?.kpp} label=' ' name='kpp' onChange={handleInputChange} />
              </div>
            </div>
            <TextInput value={kpp?.customer_contact_person} label='Представитель заказчика' name='customer_contact_person' onChange={handleInputChange} />
            <TextInput value={kpp?.customer_phone} label='Номер телефона представителя' name='customer_phone' onChange={handleInputChange} />
            <TextInput value={kpp?.customer_email} label='Почта представителя' name='customer_email' onChange={handleInputChange} />
            <DeliverySelect label='Способ доставки' name='delivery_method' onChange={(value, option) => handleSelectInputChange('delivery_method', value, option)} />
            <div className={styles.inputs}>
              <div className={styles.inputs_block}>
                <TextInput value={kpp?.contract} label='Договор' name='contract' onChange={handleInputChange} />
              </div>
              <div className={styles.inputs_block}>
                <DateInput valueFormat='DD.MM.YYYY' label='Срок окончания' name='date_end' onChange={handleDateInput} />
              </div>
            </div>
            <TextInput value={kpp?.bill} label='Счет' name='bill' onChange={handleInputChange} />
          </div>
          <div className={styles.inputs_block}>
            <TextInput value={kpp?.price} label='Стоимость' name='price' onChange={handleInputChange} />
            <TextInput value={kpp?.payment_terms} label='Реквизиты оплаты' name='payment_terms' onChange={handleInputChange} />
            <TextInput value={kpp?.payment_order} label='Заказ' name='payment_order' onChange={handleInputChange} />
            <UserSelect label='Менеджер' name='manager' onChange={(value) => handleMultiSelectInputChange('manager', value)} />
            <TextInput value={kpp?.priority} label='Приоритет' name='priority' onChange={handleInputChange} />
            <TextInput value={kpp?.difficulty} label='Сложность' name='difficulty' onChange={handleInputChange} />
            <TextInput label='Статус' name='status' onChange={handleInputChange} />
            <TaskSelect label='Задачи' name='task' onChange={(value) => handleMultiSelectInputChange('task', value)} />
            <EquipmentSelect label='Оборудование' name='equipment' onChange={(value) => handleMultiSelectInputChange('equipment', value)} />
            <FileInput label="Документы" name='document' multiple onChange={handleFileInput} />
          </div>
        </div>
        <Button fullWidth mt='xl' type='submit'>
          Создать кпп
        </Button>
      </form>
    </Card>
  );
};
