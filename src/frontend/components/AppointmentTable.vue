<template>
  <DataTable
    title="Записи"
    system-title="appointment"
    :items="appointments"
    :columns="columns"
    :filters="filters"
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
    };
  },
  methods: {
    formatStatus(status) {
      return AppointmentStatus[status] || status;
    },
    formatDateTime(date) {
      return new Date(date).toLocaleString();
    },
  },
};
</script>
