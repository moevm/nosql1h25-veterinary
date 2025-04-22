<template>
  <DataTable
    title="Пользователи"
    system-title="user"
    :items="items"
    :columns="columns"
    :filters="filters"
    :showAddButton="true"
    :addFormConfig="addFormConfig"
    @add="handleAddUser"
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
      addFormConfig: {
        login: { required: true },
        password: { type: 'password', required: true },
        second_name: { required: true },
        first_name: { required: true },
        last_name: { required: false },
        email: { type: 'email', required: true },
        role: { 
          type: 'select', 
          options: ['admin', 'doctor', 'user'],
          required: true 
        },
        birth_date: { type: 'date', required: true },
        phone_number: { required: false }
      }
    };
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
    handleAddUser(newUser) {
      console.log('Добавление нового пользователя:', newUser);
     
    }
  }
};
</script>
