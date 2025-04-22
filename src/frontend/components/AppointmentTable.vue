<template>
  <DataTable
    title="Мои записи"
    system-title="appointment"
    :items="appointments"
    :columns="columns"
    :filters="filters"
    :showAddButton="true"
    :addFormConfig="addFormConfig"
    @add="handleAddAppointment"
  />
</template>

<script>
import DataTable from './DataTable.vue';
import { AppointmentStatus } from '../models/AppointmentStatus';

export default {
  components: { DataTable },
  props: ['appointments'],
  data() {
    return {
      columns: [
        { field: 'date', label: 'Дата и время', formatter: this.formatDateTime },
        { field: 'status', label: 'Статус', formatter: this.formatStatus },
        { field: 'reason', label: 'Причина' },
        { field: 'comment', label: 'Комментарий' },
        { field: 'diagnosis', label: 'Диагноз' },
        { field: 'recommend', label: 'Рекомендации' },
      ],
      filters: [
        { field: 'date__start', label: 'Дата (от)', type: 'date' },
        { field: 'date__end', label: 'Дата (до)', type: 'date' },
        { field: 'status', label: 'Статус' },
        { field: 'reason', label: 'Причина' },
        { field: 'comment', label: 'Комментарий' },
        { field: 'diagnosis', label: 'Диагноз' },
        { field: 'recommend', label: 'Рекомендации' },
      ],
      addFormConfig: {
        date: { type: 'datetime-local', required: true },
        reason: { required: true },
        comment: { required: false },
        status: { 
          type: 'select', 
          options: Object.keys(AppointmentStatus).map(key => ({
            value: key,
            label: AppointmentStatus[key]
          })),
          required: true 
        }
      }
    };
  },
  methods: {
    formatStatus(status) {
      return AppointmentStatus[status] || status;
    },
    formatDateTime(date) {
      return new Date(date).toLocaleString();
    },
    handleAddAppointment(newAppointment) {
      console.log('Добавление новой записи:', newAppointment);

    }
  }
};
</script>
