<template>
  <DataTable
    title="Филиалы"
    system-title="office"
    :items="items"
    :columns="columns"
    :filters="filters"
    :showAddButton="true"
    :addFormConfig="addFormConfig"
    @add="handleAddOffice"
  />
</template>

<script>
import DataTable from './DataTable.vue';
export default {
  components: { DataTable },
  props: ['items'],
  data() {
    return {
      columns: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
        { field: 'phone_number', label: 'Телефон' },
        { field: 'email', label: 'Email' },
        { field: 'opening_hours', label: 'Часы работы' },
        { field: 'meta', label: 'Метаданные' },
      ],
      filters: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
        { field: 'phone_number', label: 'Телефон' },
        { field: 'email', label: 'Email' },
        { field: 'opening_hours', label: 'Часы работы' },
        { field: 'meta', label: 'Метаданные' },
      ],
      addFormConfig: {
        name: { required: true },
        address: { required: true },
        phone_number: { required: true },
        email: { type: 'email', required: true },
        opening_hours: { required: true },
        meta: { required: false }
      }
    };
  },
  methods: {
    handleAddOffice(newOffice) {
      console.log('Добавление нового филиала:', newOffice);
      
    }
  }
};
</script>
