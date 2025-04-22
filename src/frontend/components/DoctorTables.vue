<template>
  <div class="doctor-tables">
    <DataTable
      title="Мои записи"
      :items="appointments"
      :columns="appointmentColumns"
      :filters="appointmentFilters"
      @edit="editAppointment"
    />
    
    <DataTable
      title="Мои пациенты"
      :items="pets"
      :columns="petColumns"
      :filters="petFilters"
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
      appointments: [],
      pets: [],
      appointmentColumns: [
        { field: 'date', label: 'Дата и время' },
        { field: 'pet.name', label: 'Питомец' },
        { field: 'pet.owner.second_name', label: 'Владелец' },
        { field: 'status', label: 'Статус', formatter: this.formatStatus },
        { field: 'reason', label: 'Причина' },
      ],
      appointmentFilters: [
        { field: 'pet.name', label: 'Питомец' },
        { field: 'status', label: 'Статус' },
        { field: 'date', label: 'Дата', type: 'date' },
      ],
      petColumns: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
        { field: 'pet_type.type_name', label: 'Вид' },
        { field: 'owner.second_name', label: 'Владелец' },
      ],
      petFilters: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
        { field: 'pet_type.type_name', label: 'Вид' },
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
    async loadData() {
      // Заглушки данных
      this.appointments = [
        { 
          id: 1, 
          date: '2023-11-15 10:00', 
          status: 'CONFIRMED', 
          reason: 'Ежегодный осмотр',
          pet: { 
            name: 'Барсик', 
            owner: { second_name: 'Сидоров', first_name: 'Сергей' } 
          }
        },
        { 
          id: 2, 
          date: '2023-11-16 14:00', 
          status: 'PENDING', 
          reason: 'Вакцинация',
          pet: { 
            name: 'Шарик', 
            owner: { second_name: 'Петров', first_name: 'Алексей' } 
          }
        },
      ];
      
      this.pets = [
        { 
          id: 1, 
          name: 'Барсик', 
          breed: 'Британская', 
          pet_type: { type_name: 'Кошка' },
          owner: { second_name: 'Сидоров', first_name: 'Сергей' }
        },
        { 
          id: 2, 
          name: 'Шарик', 
          breed: 'Лабрадор', 
          pet_type: { type_name: 'Собака' },
          owner: { second_name: 'Петров', first_name: 'Алексей' }
        },
      ];
    },
    editAppointment(appointment) {
      console.log('Редактировать запись', appointment);
    },
  },
};
</script>

<style scoped>
.doctor-tables {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
</style>
