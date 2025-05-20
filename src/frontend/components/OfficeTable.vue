<template>
  <DataTable
    title="Филиалы"
    system-title="office"
    :items="items"
    :columns="columns"
    :filters="filters"
    :add-form-fields="addFormFields"
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
        { field: 'email', label: 'Email' }
      ],
      filters: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
        { field: 'phone_number', label: 'Телефон' },
        { field: 'email', label: 'Email' }
      ],
      addFormFields: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
        { field: 'phone_number', label: 'Телефон' },
        { field: 'email', label: 'Email', type: 'email' }
      ],
    };
  },
};
</script>
