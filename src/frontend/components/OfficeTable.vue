<template>
  <DataTable
    title="Филиалы"
    system-title="office"
    :items="items"
    :columns="columns"
    :filters="filters"
    @add="$emit('addOffice')"
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
    };
  },
};
</script>
