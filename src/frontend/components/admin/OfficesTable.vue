<template>
  <DataTable
    title="Филиалы"
    :items="offices"
    :columns="columns"
    :allow-create="true"
    :has-actions="true"
    @create="onCreateOffice"
    @edit="onEditOffice"
    @delete="onDeleteOffice"
  />
</template>

<script>
import DataTable from '../DataTable.vue';

export default {
  components: { DataTable },
  props: {
    offices: Array,
  },
  data() {
    return {
      columns: [
        { key: 'id', title: 'ID' },
        { key: 'name', title: 'Название' },
        { key: 'address', title: 'Адрес' },
        { key: 'phone_number', title: 'Телефон' },
        { key: 'email', title: 'Email' },
      ],
    };
  },
  methods: {
    onCreateOffice() {
      this.$emit('create-office');
    },
    onEditOffice(office) {
      this.$emit('edit-office', office);
    },
    onDeleteOffice(office) {
      this.$emit('delete-office', office);
    },
  },
};
</script>
