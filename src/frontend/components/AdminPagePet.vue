<template>
  <div>
    <Header />
    <div class="table-header">
      <h2>Питомцы</h2>
      <button class="add-button" @click="showAddPetModal = true">Добавить</button>
    </div>
    <PetTable :pets="pets" :show-add-button="false" />

    <div v-if="showAddPetModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить питомца</h3>
        <form @submit.prevent="addPet">
          <div class="form-group">
            <label for="name">Имя</label>
            <input id="name" v-model="newPet.name" required />

            <label for="breed">Порода</label>
            <input id="breed" v-model="newPet.breed" required />

            <label for="pet_type">Вид</label>
            <input id="pet_type" v-model="newPet.pet_type" required />

            <label for="birthdate">Дата рождения</label>
            <input id="birthdate" v-model="newPet.birthdate" type="date" required />

            <label for="gender">Пол</label>
            <select id="gender" v-model="newPet.gender" required>
              <option disabled value="">Выберите</option>
              <option value="Мужской">Мужской</option>
              <option value="Женский">Женский</option>
            </select>
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelAddPet">Отмена</button>
            <button type="submit">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from './HeaderAdmin.vue';
import PetTable from '@/components/PetTable.vue';
import { filterEntity, addEntity } from '@/api/entity.js';

export default {
  components: { Header: HeaderAdmin, PetTable },
  data() {
    return {
      pets: [],
      showAddPetModal: false,
      newPet: {
        name: '',
        breed: '',
        pet_type: '',
        birthdate: '',
        gender: ''
      }
    };
  },
  methods: {
    async loadPets() {
      this.pets = await filterEntity('pet');
    },
    cancelAddPet() {
      this.newPet = { name: '', breed: '', pet_type: '', birthdate: '', gender: '' };
      this.showAddPetModal = false;
    },
    async addPet() {
      await addEntity('pet', this.newPet);
      await this.loadPets();
      this.cancelAddPet();
    }
  },
  created() {
    this.loadPets();
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
  background-color: #17a2b8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.add-button:hover {
  background-color: #138496;
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
