<template>
  <DataTable
    title="Мои записи"
    :items="appointments"
    :columns="columns"
    :has-actions="true"
    @edit="onEditAppointment"
  />
</template>

<script>
import DataTable from '../DataTable.vue';
import { AppointmentStatus } from '../../models/AppointmentStatus';

export default {
  components: { DataTable },
  props: {
    appointments: Array,
  },
  data() {
    return {
      columns: [
        { key: 'id', title: 'ID' },
        { key: 'date', title: 'Дата и время' },
        { key: 'pet_name', title: 'Питомец' },
        { key: 'client_name', title: 'Клиент' },
        { key: 'status', title: 'Статус' },
        { key: 'reason', title: 'Причина' },
      ],
    };
  },
  methods: {
    onEditAppointment(appointment) {
      this.$emit('edit-appointment', appointment);
    },
    getStatusText(status) {
      return AppointmentStatus[status] || status;
    },
  },
};
</script>
