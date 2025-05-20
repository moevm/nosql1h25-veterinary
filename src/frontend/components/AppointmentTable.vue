<template>
  <DataTable
    title="Записи"
    system-title="appointment"
    :items="appointments"
    :columns="columns"
    :filters="filters"
    :add-form-fields="addFormFields"
    @add="$emit('add')"
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
        // { field: 'date', label: 'Дата и время', formatter: this.formatDateTime },
        { field: 'status', label: 'Статус', formatter: this.formatStatus },
        { field: 'reason', label: 'Причина' },
        { field: 'comment', label: 'Комментарий' },
        { field: 'diagnosis', label: 'Диагноз' },
        { field: 'recommend', label: 'Рекомендации' },
      ],
      filters: [
        { field: 'status', label: 'Статус', type: 'select', options: [
        { label: 'Ожидает подтверждения', value: 'ожидает подтверждения' },
        { label: 'Подтвержден', value: 'подтвержден' },
        { label: 'Отменен', value: 'отменен' },
        { label: 'Проведен', value: 'проведен' },
        ] },
        { field: 'reason', label: 'Причина' },
        { field: 'comment', label: 'Комментарий' },
        { field: 'diagnosis', label: 'Диагноз' },
        { field: 'recommend', label: 'Рекомендации' },
      ],
      addFormFields: [
        { field: 'status', label: 'Статус', type: 'select', options: [
        { label: 'Ожидает подтверждения', value: 'PENDING' },
        { label: 'Подтвержден', value: 'CONFIRMED' },
        { label: 'Отменен', value: 'CANCELED' },
        { label: 'Проведен', value: 'COMPLETED' },
        ] },
        { field: 'reason', label: 'Причина' },
        { field: 'comment', label: 'Комментарий' },
        { field: 'diagnosis', label: 'Диагноз' },
        { field: 'recommend', label: 'Рекомендации' },
      ],
    };
  },
  methods: {
    formatStatus(status) {
      return AppointmentStatus[status] || status;
    },
    formatDateTime(date) {
      return new Date(date).toLocaleString();
    }
  },
};
</script>
