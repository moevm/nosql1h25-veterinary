<template>
  <div class="admin-tables">
    <DataTable
      title="Пользователи"
      :items="users"
      :columns="userColumns"
      :filters="userFilters"
      @add="addUser"
      @edit="editUser"
      @delete="deleteUser"
    />
    
    <DataTable
      title="Филиалы"
      :items="offices"
      :columns="officeColumns"
      :filters="officeFilters"
      @add="addOffice"
      @edit="editOffice"
      @delete="deleteOffice"
    />
    
    <DataTable
      title="Услуги"
      :items="procedures"
      :columns="procedureColumns"
      :filters="procedureFilters"
      @add="addProcedure"
      @edit="editProcedure"
      @delete="deleteProcedure"
    />
  </div>
</template>

<script>
import DataTable from './DataTable.vue';

export default {
  components: { DataTable },
  data() {
    return {
      users: [],
      offices: [],
      procedures: [],
      userColumns: [
        { field: 'login', label: 'Логин' },
        { field: 'second_name', label: 'Фамилия' },
        { field: 'first_name', label: 'Имя' },
        { field: 'last_name', label: 'Отчество' },
        { field: 'email', label: 'Email' },
        { field: 'role', label: 'Роль' },
      ],
      userFilters: [
        { field: 'login', label: 'Логин' },
        { field: 'second_name', label: 'Фамилия' },
        { field: 'role', label: 'Роль' },
      ],
      officeColumns: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
        { field: 'phone_number', label: 'Телефон' },
        { field: 'email', label: 'Email' },
      ],
      officeFilters: [
        { field: 'name', label: 'Название' },
        { field: 'address', label: 'Адрес' },
      ],
      procedureColumns: [
        { field: 'name', label: 'Название' },
        { field: 'cost', label: 'Стоимость' },
        { field: 'available', label: 'Доступна', formatter: (v) => v ? 'Да' : 'Нет' },
      ],
      procedureFilters: [
        { field: 'name', label: 'Название' },
        { field: 'available', label: 'Доступна', type: 'checkbox' },
      ],
    };
  },
  async created() {
    // Загрузка данных с сервера
    await this.loadData();
  },
  methods: {
    async loadData() {
      // Здесь должны быть запросы к API
      // this.users = await fetchUsers();
      // this.offices = await fetchOffices();
      // this.procedures = await fetchProcedures();
      
      // Заглушки данных для демонстрации
      this.users = [
        { id: 1, login: 'admin', second_name: 'Иванов', first_name: 'Иван', last_name: 'Иванович', email: 'admin@clinic.ru', role: 'Администратор' },
        { id: 2, login: 'doctor1', second_name: 'Петров', first_name: 'Петр', last_name: 'Петрович', email: 'doctor1@clinic.ru', role: 'Врач' },
      ];
      
      this.offices = [
        { id: 1, name: 'Центральный', address: 'ул. Центральная, 1', phone_number: '+79990001111', email: 'central@clinic.ru' },
        { id: 2, name: 'Северный', address: 'ул. Северная, 5', phone_number: '+79990002222', email: 'north@clinic.ru' },
      ];
      
      this.procedures = [
        { id: 1, name: 'Осмотр', cost: 1000, available: true },
        { id: 2, name: 'Вакцинация', cost: 1500, available: true },
        { id: 3, name: 'Стоматология', cost: 3000, available: false },
      ];
    },
    addUser() {
      console.log('Добавить пользователя');
    },
    editUser(user) {
      console.log('Редактировать пользователя', user);
    },
    deleteUser(user) {
      console.log('Удалить пользователя', user);
    },
    addOffice() {
      console.log('Добавить филиал');
    },
    editOffice(office) {
      console.log('Редактировать филиал', office);
    },
    deleteOffice(office) {
      console.log('Удалить филиал', office);
    },
    addProcedure() {
      console.log('Добавить услугу');
    },
    editProcedure(procedure) {
      console.log('Редактировать услугу', procedure);
    },
    deleteProcedure(procedure) {
      console.log('Удалить услугу', procedure);
    },
  },
};
</script>

<style scoped>
.admin-tables {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
</style>
