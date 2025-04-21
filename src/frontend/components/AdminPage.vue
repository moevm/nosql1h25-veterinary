<template>
  <div>
    <Header :user="user" @logout="onLogout" />
    <div class="admin-container">
      <OfficesTable
        :offices="offices"
        @create-office="showOfficeModal"
        @edit-office="editOffice"
        @delete-office="deleteOffice"
      />
      <!-- Другие таблицы для администратора -->
    </div>
  </div>
</template>

<script>
import Header from './Header.vue';
import OfficesTable from './admin/OfficesTable.vue';

export default {
  components: { Header, OfficesTable },
  props: {
    user: Object,
    offices: Array,
  },
  methods: {
    onLogout() {
      this.$emit('logout');
    },
    showOfficeModal() {
      // Логика показа модального окна
    },
    editOffice(office) {
      // Логика редактирования
    },
    deleteOffice(office) {
      // Логика удаления
    },
  },
};
</script>

<style scoped>
.admin-container {
  padding: 20px;
}
</style>
