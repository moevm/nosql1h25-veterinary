<template>
  <div>
    <Header />
    <div class="table-header">
      <h2>Филиалы</h2>
      <button class="add-button" @click="showAddOfficeModal = true">Добавить</button>
    </div>
    <OfficeTable :items="offices" :show-add-button="false" />

    <div v-if="showAddOfficeModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить филиал</h3>
        <form @submit.prevent="addOffice">
          <div class="form-group">
            <label for="name">Название</label>
            <input id="name" v-model="newOffice.name" required />

            <label for="address">Адрес</label>
            <input id="address" v-model="newOffice.address" required />

            <label for="phone">Телефон</label>
            <input id="phone" v-model="newOffice.phone_number" required />
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelAddOffice">Отмена</button>
            <button type="submit">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from './HeaderAdmin.vue';
import OfficeTable from '@/components/OfficeTable.vue';
import { filterEntity, addEntity } from '@/api/entity.js';

export default {
  components: { Header: HeaderAdmin, OfficeTable },
  data() {
    return {
      offices: [],
      showAddOfficeModal: false,
      newOffice: {
        name: '',
        address: '',
        phone_number: ''
      }
    };
  },
  methods: {
    async loadOffices() {
      this.offices = await filterEntity('office');
    },
    cancelAddOffice() {
      this.newOffice = { name: '', address: '', phone_number: '' };
      this.showAddOfficeModal = false;
    },
    async addOffice() {
      await addEntity('office', this.newOffice);
      await this.loadOffices();
      this.cancelAddOffice();
    }
  },
  created() {
    this.loadOffices();
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
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.add-button:hover {
  background-color: #0069d9;
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
