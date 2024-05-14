import React, { useState } from 'react';
import { Button, Card, ComboboxItem, FileInput, TextInput } from '@mantine/core';
import { DateInput, DateValue } from '@mantine/dates';
import { useCreatekppMutation } from '~/shared/api/services/kpps';
import { UserSelect } from '~/entities/userSelect';
import { ConsigneeSelect } from '~/entities/consigneeSelect';
import { DeliverySelect } from '~/entities/deliverySelect';
import { EquipmentSelect } from '~/entities/equipmentSelect';
import { TaskSelect } from '~/entities/taskSelect';
import styles from './KppForm.module.css';


export const KppForm: React.FC = () => {
    //
    const [createKpp] = useCreatekppMutation();

    const [formData, setFormData] = useState(new FormData());

    // const handleConsigneeInput = (e: SelectProps) => {
    //     formData.append('consignee_details', e.onChange?.value);
    //     setFormData(formData);
    // }
    // (property) SelectProps.onChange?: ((value: string | null, option: ComboboxItem) => void) | undefined

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
        createKpp(formData);
    };

    return (
        <Card className={styles.kpp_form}>
            <form
                className={styles.CreateKpp}
                onSubmit={handleSubmit}
            >
                <div className={styles.inputs}>
                    <div className={styles.inputs_block}>
                        <TextInput label='Номер' name='name_number' onChange={handleInputChange} />
                        <TextInput label='Наименование' name='name' onChange={handleInputChange} />
                        <TextInput label='Описание' name='description' onChange={handleInputChange} />
                        <ConsigneeSelect label='Компания заказчика' name='consignee_details' onChange={(value, option) => handleSelectInputChange('consignee_details', value, option)} />
                        <div className={styles.inputs}>
                          <div className={styles.inputs_block}>
                            <TextInput label='ИНН/КПП' name='tin' onChange={handleInputChange} />
                          </div>
                          <div className={styles.inputs_block}>
                            <TextInput label=' ' name='kpp' onChange={handleInputChange} />
                          </div>
                        </div>
                        <TextInput label='Представитель заказчика' name='customer_contact_person' onChange={handleInputChange} />
                        <TextInput label='Номер телефона представителя' name='customer_phone' onChange={handleInputChange} />
                        <TextInput label='Почта представителя' name='customer_email' onChange={handleInputChange} />
                        <DeliverySelect label='Способ доставки' name='delivery_method' onChange={(value, option) => handleSelectInputChange('delivery_method', value, option)} />
                        <div className={styles.inputs}>
                          <div className={styles.inputs_block}>
                            <TextInput label='Договор' name='contract' onChange={handleInputChange} />
                          </div>
                          <div className={styles.inputs_block}>
                            <DateInput valueFormat='DD.MM.YYYY' label='Срок окончания' name='date_end' onChange={handleDateInput} />
                          </div>
                        </div>
                        <TextInput label='Счет' name='bill' onChange={handleInputChange} />
                    </div>
                    <div className={styles.inputs_block}>
                        <TextInput label='Стоимость' name='price' onChange={handleInputChange} />
                        <TextInput label='Реквизиты оплаты' name='payment_terms' onChange={handleInputChange} />
                        <TextInput label='Заказ' name='payment_order' onChange={handleInputChange} />
                        <UserSelect label='Менеджер' name='manager' onChange={(value) => handleMultiSelectInputChange('manager', value)} />
                        <TextInput label='Приоритет' name='priority' onChange={handleInputChange} />
                        <TextInput label='Сложность' name='difficulty' onChange={handleInputChange} />
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
