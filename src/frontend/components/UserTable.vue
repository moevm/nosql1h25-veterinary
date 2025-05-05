<template>
  <DataTable
    title="Пользователи"
    system-title="user"
    :items="items"
    :columns="columns"
    :filters="filters"
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
        { field: 'role', label: 'Роль' },
        { field: 'birth_date__start', label: 'Дата рождения (с)', type: 'date' },
        { field: 'birth_date__end', label: 'Дата рождения (по)', type: 'date' },
      ],
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return '';
      return new Date(date).toISOString().split('T')[0];
    },
  },
};
</script>
