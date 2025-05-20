<template>
  <div>
    <Header />
    <div class="table-header">
      <h2></h2>
      <button class="add-button" @click="showAddModal = true">Добавить</button>
    </div>
    <AppointmentTable :appointments="appointments" @add="addAppointment" />

    <div v-if="showAddModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить запись</h3>
        <form @submit.prevent="addAppointment">
          <div class="form-group">
            <label for="status">Статус</label>
            <select id="status" v-model="newAppointment.status" required>
              <option value="ожидает подтверждения">Ожидает подтверждения</option>
              <option value="подтвержден">Подтвержден</option>
              <option value="отменен">Отменен</option>
              <option value="проведен">Проведен</option>
            </select>

            <label for="reason">Причина</label>
            <input id="reason" v-model="newAppointment.reason" />

            <label for="comment">Комментарий</label>
            <input id="comment" v-model="newAppointment.comment" />

            <label for="diagnosis">Диагноз</label>
            <input id="diagnosis" v-model="newAppointment.diagnosis" />

            <label for="recommend">Рекомендации</label>
            <input id="recommend" v-model="newAppointment.recommend" />
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelAdd">Отмена</button>
            <button type="submit">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from './HeaderAdmin.vue';
import AppointmentTable from '@/components/AppointmentTable.vue';
import { addEntity, filterEntity } from '@/api/entity';

export default {
  components: {
    Header: HeaderAdmin,
    AppointmentTable,
  },
  data() {
    return {
      appointments: [],
      showAddModal: false,
      newAppointment: {
        date: '',
        status: '',
        reason: '',
        comment: '',
        diagnosis: '',
        recommend: ''
      }
    };
  },
  methods: {
    async loadAppointments() {
      this.appointments = await filterEntity('appointment');
    },
    cancelAdd() {
      this.newAppointment = {
        date: '',
        status: '',
        reason: '',
        comment: '',
        diagnosis: '',
        recommend: ''
      };
      this.showAddModal = false;
    },
    async addAppointment() {
      await addEntity('appointment', this.newAppointment);
      await this.loadAppointments();
      this.cancelAdd();
    }
  },
  created() {
    this.loadAppointments();
  }
};
</script>

<style scoped>
.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.add-button {
  padding: 0.5rem 1rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.add-button:hover {
  background-color: #218838;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 400px;
  max-width: 90%;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}
</style>