<template>
  <DataTable
    title="Пользователи"
    system-title="user"
    :items="items"
    :columns="columns"
    :filters="filters"
    :add-form-fields="addFormFields"
    @add="$emit('addUser')"
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
        { field: 'login', label: 'Логин' },
        { field: 'second_name', label: 'Фамилия' },
        { field: 'first_name', label: 'Имя' },
        { field: 'last_name', label: 'Отчество' },
        { field: 'email', label: 'Email' },
        { field: 'role', label: 'Роль' },
        { field: 'birth_date', label: 'Дата рождения', formatter: this.formatDate },
      ],
      filters: [
        { field: 'login', label: 'Логин' },
        { field: 'second_name', label: 'Фамилия' },
        { field: 'first_name', label: 'Имя' },
        { field: 'last_name', label: 'Отчество' },
        { field: 'email', label: 'Email' },
        { field: 'role', label: 'Роль', type: 'select', options: [
          { label: 'admin', value: 'admin' },
          { label: 'client', value: 'client' },
          { label: 'doctor', value: 'doctor' },
        ] },
        { field: 'birth_date__start', label: 'Дата рождения (с)', type: 'date' },
        { field: 'birth_date__end', label: 'Дата рождения (по)', type: 'date' },
      ],
      addFormFields: [
        { field: 'login', label: 'Логин' },
        { field: 'second_name', label: 'Фамилия' },
        { field: 'first_name', label: 'Имя' },
        { field: 'last_name', label: 'Отчество' },
        { field: 'email', label: 'Email', type: 'email' },
        { field: 'role', label: 'Роль', type: 'select', options: [
          { label: 'admin', value: 'admin' },
          { label: 'client', value: 'client' },
          { label: 'doctor', value: 'doctor' },
        ] },
        { field: 'birth_date', label: 'Дата рождения', type: 'date' },
      ],
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return '';
      const isoDate = new Date(date).toISOString().split('T')[0]; // yyyy-mm-dd
      const [year, month, day] = isoDate.split('-');
      return `${day}.${month}.${year}`; // dd.mm.yyyy
    }
  }
};
</script>
