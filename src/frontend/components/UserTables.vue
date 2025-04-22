<template>
  <div class="user-tables">
    <DataTable
      title="Мои питомцы"
      :items="pets"
      :columns="petColumns"
      :filters="petFilters"
      @add="addPet"
      @edit="editPet"
      @delete="deletePet"
    />
    
    <DataTable
      title="Мои записи"
      :items="appointments"
      :columns="appointmentColumns"
      :filters="appointmentFilters"
      @add="addAppointment"
      @edit="editAppointment"
      @delete="deleteAppointment"
    />
  </div>
</template>

<script>
import DataTable from './DataTable.vue';
import { AppointmentStatus } from '../models/AppointmentStatus';

export default {
  components: { DataTable },
  data() {
    return {
      pets: [],
      appointments: [],
      petColumns: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
        { field: 'pet_type.type_name', label: 'Вид' },
        { field: 'birthdate', label: 'Дата рождения', formatter: this.formatDate },
      ],
      petFilters: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
      ],
      appointmentColumns: [
        { field: 'date', label: 'Дата и время', formatter: this.formatDateTime },
        { field: 'doctor.second_name', label: 'Врач' },
        { field: 'office.name', label: 'Филиал' },
        { field: 'status', label: 'Статус', formatter: this.formatStatus },
        { field: 'reason', label: 'Причина' },
      ],
      appointmentFilters: [
        { field: 'doctor.second_name', label: 'Врач' },
        { field: 'status', label: 'Статус' },
        { field: 'date', label: 'Дата', type: 'date' },
      ],
    };
  },
  async created() {
    await this.loadData();
  },
  methods: {
    formatStatus(status) {
      return AppointmentStatus[status] || status;
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
    formatDateTime(date) {
      return new Date(date).toLocaleString();
    },
    async loadData() {
      // Заглушки данных
      this.pets = [
        { 
          id: 1, 
          name: 'Барсик', 
          breed: 'Британская', 
          birthdate: '2020-05-15',
          pet_type: { type_name: 'Кошка' }
        },
      ];
      
      this.appointments = [
        { 
          id: 1, 
          date: '2023-11-15 10:00', 
          status: 'CONFIRMED', 
          reason: 'Ежегодный осмотр',
          doctor: { second_name: 'Иванова', first_name: 'Мария' },
          office: { name: 'Центральный' }
        },
        { 
          id: 2, 
          date: '2023-12-10 14:00', 
          status: 'PENDING', 
          reason: 'Вакцинация',
          doctor: { second_name: 'Петров', first_name: 'Алексей' },
          office: { name: 'Северный' }
        },
      ];
    },
    addPet() {
      console.log('Добавить питомца');
    },
    editPet(pet) {
      console.log('Редактировать питомца', pet);
    },
    deletePet(pet) {
      console.log('Удалить питомца', pet);
    },
    addAppointment() {
      console.log('Добавить запись');
    },
    editAppointment(appointment) {
      console.log('Редактировать запись', appointment);
    },
    deleteAppointment(appointment) {
      console.log('Удалить запись', appointment);
    },
  },
};
</script>

<style scoped>
.user-tables {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
</style>
