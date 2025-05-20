<template>
  <div>
    <Header />
    <div class="table-header">
      <h2></h2>
      <button class="add-button" @click="showAddServiceModal = true">Добавить</button>
    </div>
    <ProcedureTable :items="services" :show-add-button="false" />

    <div v-if="showAddServiceModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить услугу</h3>
        <form @submit.prevent="addService">
          <div class="form-group">
            <label for="name">Название</label>
            <input id="name" v-model="newService.name" required />

            <label for="cost">Стоимость</label>
            <input id="cost" v-model.number="newService.cost" type="number" min="0" step="0.01" required />

            <label for="description">Описание</label>
            <input id="description" v-model="newService.description" required />
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelAddService">Отмена</button>
            <button type="submit">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from './HeaderAdmin.vue';
import ProcedureTable from '@/components/ProcedureTable.vue';
import { filterEntity, addEntity } from '@/api/entity.js';

export default {
  components: { Header: HeaderAdmin, ProcedureTable },
  data() {
    return {
      services: [],
      showAddServiceModal: false,
      newService: {
        name: '',
        cost: 0,
        description: ''
      }
    };
  },
  methods: {
    async loadServices() {
      this.services = await filterEntity('procedure');
    },
    cancelAddService() {
      this.newService = { name: '', cost: 0, description: '' };
      this.showAddServiceModal = false;
    },
    async addService() {
      await addEntity('procedure', this.newService);
      await this.loadServices();
      this.cancelAddService();
    }
  },
  created() {
    this.loadServices();
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
