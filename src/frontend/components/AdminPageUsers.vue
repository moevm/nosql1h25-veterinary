<template>
  <div>
    <Header />
    <div class="table-header">
      <h2></h2>
      <button class="add-button" @click="showAddUserModal = true">Добавить</button>
    </div>
    <UserTable :items="users" :show-add-button="false" />

    <div v-if="showAddUserModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить пользователя</h3>
        <form @submit.prevent="addUser">
          <div class="form-group">
            <label for="login">Логин</label>
            <input id="login" v-model="newUser.login" required />

            <label for="second_name">Фамилия</label>
            <input id="second_name" v-model="newUser.second_name" required />

            <label for="first_name">Имя</label>
            <input id="first_name" v-model="newUser.first_name" required />

            <label for="last_name">Отчество</label>
            <input id="last_name" v-model="newUser.last_name" />

            <label for="email">Email</label>
            <input id="email" v-model="newUser.email" type="email" required />

            <label for="role">Роль</label>
            <select id="role" v-model="newUser.role" required>
              <option value="admin">admin</option>
              <option value="client">client</option>
              <option value="doctor">doctor</option>
            </select>

            <label for="birth_date">Дата рождения</label>
            <input id="birth_date" v-model="newUser.birth_date" type="date" required />
          </div>

          <div class="modal-actions">
            <button type="button" @click="cancelAddUser">Отмена</button>
            <button type="submit">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from './HeaderAdmin.vue';
import UserTable from '@/components/UserTable.vue';
import { filterEntity, addEntity } from '@/api/entity.js';

export default {
  components: { Header: HeaderAdmin, UserTable },
  data() {
    return {
      users: [],
      showAddUserModal: false,
      newUser: {
        login: '',
        second_name: '',
        first_name: '',
        last_name: '',
        email: '',
        role: '',
        birth_date: ''
      }
    };
  },
  methods: {
    async loadUsers() {
      this.users = await filterEntity('user');
    },
    cancelAddUser() {
      this.newUser = {
        login: '', second_name: '', first_name: '', last_name: '',
        email: '', role: '', birth_date: ''
      };
      this.showAddUserModal = false;
    },
    async addUser() {
      await addEntity('user', this.newUser);
      await this.loadUsers();
      this.cancelAddUser();
    }
  },
  created() {
    this.loadUsers();
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
