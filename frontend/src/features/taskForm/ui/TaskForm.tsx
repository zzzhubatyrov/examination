import React, { useState } from 'react';

import {Button, Card, ComboboxItem, FileInput, TextInput} from '@mantine/core';
import {DateInput, DateValue} from '@mantine/dates';
import { UserSelect } from '~/entities/userSelect';
import { FacilitiesSelect } from '~/entities/facilitySelect';
import styles from './TaskForm.module.css';
import {useCreateTaskMutation} from "~/shared/api/services/tasks";

export const TaskForm: React.FC = () => {
  const [createTask] = useCreateTaskMutation();

  const [formData, setFormData] = useState(new FormData());

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
    createTask(formData);
  };

  return (
    <Card className={styles.task_form}>
      <form
        className={styles.CreateTask}
        onSubmit={handleSubmit}
      >
        <div className={styles.inputs}>
          <div className={styles.inputs_block}>
            <TextInput label='Сервис' name='service' onChange={handleInputChange} />
            <TextInput label='Наименование' name='name' onChange={handleInputChange} />
            <TextInput label='Описание' name='description' onChange={handleInputChange} />
            <TextInput label='Сложность' name='labor_intensity' onChange={handleInputChange} />
            <FacilitiesSelect label='Объект' name='facility' onChange={(value, option) => handleSelectInputChange('facility', value, option)} />
            <FacilitiesSelect label='Адрес' name='address' onChange={(value, option) => handleSelectInputChange('address', value, option)} />
          </div>
          <div className={styles.inputs_block}>
            <UserSelect label='Заявитель' name='applicant' onChange={(value) => handleMultiSelectInputChange('applicant', value)} />
            <UserSelect label='Исполнитель' name='appointed' onChange={(value) => handleMultiSelectInputChange('appointed', value)} />
            <UserSelect label='Наблюдатель' name='spectator' onChange={(value) => handleMultiSelectInputChange('spectator', value)} />
            <TextInput label='Теги' name='tags' onChange={handleInputChange} />
            <DateInput valueFormat='DD.MM.YYYY' label='Срок выполнения' name='deadline' onChange={handleDateInput} />
            <DateInput valueFormat='DD.MM.YYYY' label='Срок окончания' name='tags' onChange={handleDateInput} />
            <FileInput label="Документы" name='document' multiple onChange={handleFileInput} />
          </div>
        </div>
        <Button fullWidth mt='xl' type='submit'>
          Создать задачу
        </Button>
      </form>
    </Card>
  );
};
